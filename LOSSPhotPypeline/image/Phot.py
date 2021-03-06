# standard imports
import pandas as pd
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS, InvalidTransformError
import os
import matplotlib.pyplot as plt
from astropy.visualization import ZScaleInterval

# internal imports
from LOSSPhotPypeline.image.FileNames import FileNames
from LOSSPhotPypeline.image.FitsInfo import FitsInfo
import LOSSPhotPypeline.utils as LPPu

class Phot(FitsInfo):

    def __init__(self, name, radecfile = None, radec = None, wdir = '.', calmethod = 'psf'):

        FitsInfo.__init__(self, name)

        self.radecfile = radecfile
        self.radec = radec
        self.wdir = os.path.abspath(wdir)
        self.calmethod = calmethod
        self.phot_raw = None # internal dataframe representation of photometry for use during calibration
        self.phot_sub_raw = None

        if (self.radec is None) and (self.radecfile is not None):
            self.radec = pd.read_csv(self.radecfile, delim_whitespace=True, skiprows = (0,1,3,4,5), names = ['RA','DEC'])

        self.stat_err = 0
        self.cal_err = 0
        self.sim_err = 0

        # get and set fwhm
        self.get_fwhm()

    def gen_obj_fl(self):
        '''generates obj file'''

        # convert to pixel coordinates in current image and save
        try:
            cs = WCS(header = self.header)
            imagex, imagey = cs.all_world2pix(self.radec['RA'], self.radec['DEC'], 0)
            pd.DataFrame({'x': imagex, 'y': imagey}).to_csv(os.path.join(self.wdir, self.obj), sep = '\t', index=False, header = False, float_format='%9.4f')
            return True
        except InvalidTransformError:
            return False

    def galaxy_subtract(self, template_images, subreg = 0.9):
        '''perform galaxy subraction by wrapping IDL procedure'''

        selector = '{}_{}'.format(self.filter.upper(), self.telescope.lower())

        # execute idl commmand if possible, then store results
        if template_images[selector] is not None:
            idl_cmd = '''idl -e "lpp_kait_photsub, '{}', '{}', subreg={}, /OUTPUT"'''.format(self.cimg, template_images[selector], subreg)
            stdout, stderr = LPPu.idl(idl_cmd, wdir = self.wdir)
            sub_idl = (idl_cmd, stdout, stderr)
            return True, sub_idl
        else:
            return False, ('no IDL cmd due to missing template', None, None)

    def do_photometry(self, photsub = False, forcesky = False):
        '''performs photometry by wrapping IDL procedure'''

        # do necessary pre-steps
        succ = self.gen_obj_fl()
        if succ is False:
            return False, False, ('could not generate object file', None, None)

        # formulate and run idl command, then store results
        if photsub is False:
            ps = ''
        else:
            ps = '/PHOTSUB, '
        if forcesky is False:
            fs = ''
        else:
            fs = '/FORCESKY, '
        # note: exposure time hardcoded to 1s (not self.exptime) to address bug in LPP_NSTAR (from astro IDL)
        idl_cmd = '''idl -e "lpp_phot_psf, '{}', fwhm = {}, exposures = {}, /SAVESKY, {}{}/OUTPUT"'''.format(self.cimg, self.fwhm, 1, ps, fs)
        stdout, stderr = LPPu.idl(idl_cmd, wdir = self.wdir)
        phot_idl = (idl_cmd, stdout, stderr)

        r1 = True
        if os.path.exists(os.path.join(self.wdir, self.psf)) is False:
            r1 = False
        r2 = False
        if (photsub is True) and (os.path.exists(os.path.join(self.wdir, self.psfsub)) is True):
            r2 = True

        return r1, r2, phot_idl

    def calibrate(self, cal_IDs, cal_mags, cal_errs, sub = False, write_dat = False):

        # aperture names
        aps = ['3.5p', '5p', '7p', '9p', '1fh', '1.5fh', '2fh', 'psf']
        err_aps = [ap + '_err' for ap in aps]
        col_names = ('id','ximage','yimage') + tuple(('{}{}'.format(m, e) for m in aps for e in ('', '_err')))

        # load raw photometry
        if self.phot_raw is None:
            self.phot_raw = pd.read_csv(self.psf, header = None, delim_whitespace = True, comment = ';', index_col = 0, 
                            names = col_names, skiprows = 1)
            self.phot_raw.index = self.phot_raw.index - 2 # align with indexing of cal stars
            self.phot_raw = self.phot_raw.reindex(self.radec.index - 1) # make indexes match, so NaN if not in file
        if (self.phot_sub_raw is None) and (sub is True):
            self.phot_sub_raw = pd.read_csv(self.psfsub, header = None, delim_whitespace = True, comment = ';', index_col = 0, 
                                names = col_names, skiprows = 1)
            self.phot_sub_raw.index = self.phot_sub_raw.index - 2
            self.phot_sub_raw = self.phot_sub_raw.reindex(self.radec.index - 1)

        # ref stars in sub are the same as in un sub so only need to find cal mags once
        cal_mag_mean = cal_mags.loc[cal_IDs].mean()
        cal_mag_var = (cal_errs.loc[cal_IDs]**2).sum() / len(cal_IDs)**2 # error propagation of mean
        instrument_mag_mean = self.phot_raw.loc[cal_IDs, aps].mean(axis = 0)
        instrument_mag_var = (self.phot_raw.loc[cal_IDs, err_aps]**2).sum(axis = 0) / len(cal_IDs)**2
        zp_offset = cal_mag_mean - instrument_mag_mean
        zp_offset_var = cal_mag_var + instrument_mag_var

        # record uncertainty from photometry and calibration
        self.stat_err = self.phot_raw.loc[-1, self.calmethod + '_err']
        if sub is True:
            self.stat_err = self.phot_sub_raw.loc[-1, self.calmethod + '_err']
        self.cal_err = np.sqrt(zp_offset_var.loc[self.calmethod + '_err'])

        # get coords of ref stars in obs
        cs = WCS(header = self.header)
        ra, dec = cs.all_pix2world(self.phot_raw['ximage'], self.phot_raw['yimage'], 0)
        self.phot_raw.loc[:, 'RA_obs'] = ra
        self.phot_raw.loc[:, 'DEC_obs'] = dec

        # write psf zeropoint (only do once)
        with open(self.zerotxt, 'w') as f:
            f.write(str(25 + zp_offset['psf']))

        # calibrate photometry
        self.phot = self.phot_raw.copy(deep = True)
        self.phot.loc[:, aps] = self.phot.loc[:, aps] + zp_offset
        self.phot.loc[:, err_aps] = np.sqrt(self.phot.loc[:, err_aps]**2 + zp_offset_var)
        if sub is True:
            self.phot_sub = self.phot_sub_raw.copy(deep = True)
            self.phot_sub.loc[:, aps] = self.phot_sub.loc[:, aps] + zp_offset
            self.phot_sub.loc[:, err_aps] = np.sqrt(self.phot_sub.loc[:, err_aps]**2 + zp_offset_var)

        # determine which ref stars are in image
        self.phot.loc[:, 'ref_in'] = 1
        out = (self.phot['ximage'] < 0) | (self.phot['ximage'] > cs._naxis[0]) | (self.phot['yimage'] < 0) | (self.phot['yimage'] > cs._naxis[1])
        self.phot.loc[out, 'ref_in'] = 0

        # include color term
        self.phot.loc[:, 'system'] = self.color_term

        # write dat files if requested
        if write_dat is True:
            self.phot.index = self.phot.index + 2
            with open(self.psfdat, 'w') as outfile:
                outfile.write(''.join(['{:<8}'.format(ii) for ii in [';;id', 'ximage', 'yimage', '3.5p', 'err', '5p', 'err', '7p', 'err', '9p', 'err', '1fh', 'err', '1.5fh', 'err', '2fh', 'err', 'psf', 'err']]) + '\n')
                outfile.write(self.phot.loc[:,list(col_names)[1:]].to_string(header = False, index_names = False, float_format = '%.3f', col_space = 7))
            self.phot.index = self.phot.index - 2
            if sub is True:
                self.phot_sub.index = self.phot_sub.index + 2
                with open(self.psfsubdat, 'w') as outfile:
                    outfile.write(''.join(['{:<8}'.format(ii) for ii in [';;id', 'ximage', 'yimage', '3.5p', 'err', '5p', 'err', '7p', 'err', '9p', 'err', '1fh', 'err', '1.5fh', 'err', '2fh', 'err', 'psf', 'err']]) + '\n')
                    outfile.write(self.phot_sub.loc[:,list(col_names)[1:]].to_string(header = False, index_names = False, float_format = '%.3f', col_space = 7))
                self.phot_sub.index = self.phot_sub.index - 2

        # return photometry for checking
        return self.phot

    def display_image(self, ax = None, display = True):
        '''displays image'''

        with fits.open(self.oriname) as f:
            im = f[0].data

        if ax is None:
            fig, ax = plt.subplots(figsize = (8, 8))
        z = ZScaleInterval()
        zlim = z.get_limits(im.data)
        ax.imshow(-1*im, cmap = 'gray', vmin = -1*zlim[1], vmax = -1*zlim[0])
        if display:
            fig.show()
