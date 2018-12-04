# standard imports
import pandas as pd
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS, InvalidTransformError
import os

# internal imports
from LOSSPhotPypeline.image.FileNames import FileNames
from LOSSPhotPypeline.image.FitsInfo import FitsInfo
import LOSSPhotPypeline.utils as LPPu

class Phot(FitsInfo):

    def __init__(self, name, radecfile = None, radec = None, wdir = '.'):

        FitsInfo.__init__(self, name)

        self.radecfile = radecfile
        self.radec = radec
        self.wdir = os.path.abspath(wdir)
        self.phot_raw = None # internal dataframe representation of photometry for use during calibration
        self.phot_sub_raw = None

        if (self.radec is None) and (self.radecfile is not None):
            self.radec = pd.read_csv(self.radecfile, delim_whitespace=True, skiprows = (0,1,3,4,5), names = ['RA','DEC'])

        # get and set fwhm
        self.get_fwhm()

    def gen_obj_fl(self):
        '''generates obj file'''

        # convert to pixel coordinates in current image and save
        try:
            cs = WCS(header = self.header)
            imagex, imagey = cs.all_world2pix(self.radec['RA'], self.radec['DEC'], 1)
            pd.DataFrame({'x': imagex, 'y': imagey}).to_csv(os.path.join(self.wdir, self.obj), sep = '\t', index=False, header = False, float_format='%9.4f')
            return True
        except InvalidTransformError:
            return False

    def galaxy_subtract(self, template_images):
        '''perform galaxy subraction by wrapping IDL procedure'''

        selector = '{}_{}'.format(self.filter.upper(), self.telescope.lower())

        # execute idl commmand if possible, then store results
        if template_images[selector] is not None:
            idl_cmd = '''idl -e "lpp_kait_photsub, '{}', '{}', /OUTPUT"'''.format(self.cimg, template_images[selector])
            stdout, stderr = LPPu.idl(idl_cmd, wdir = self.wdir)
            sub_idl = (idl_cmd, stdout, stderr)
            return True, sub_idl
        else:
            return False, ('no IDL cmd due to missing template', None, None)

    def do_photometry(self, photsub = False):
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
        # note: exposure time hardcoded to 1s (not self.exptime) to address bug in LPP_NSTAR (from astro IDL)
        idl_cmd = '''idl -e "lpp_phot_psf, '{}', fwhm = {}, exposures = {}, /SAVESKY, {}/OUTPUT"'''.format(self.cimg, self.fwhm, 1, ps)
        stdout, stderr = LPPu.idl(idl_cmd, wdir = self.wdir)
        phot_idl = (idl_cmd, stdout, stderr)

        r1 = True
        if os.path.exists(os.path.join(self.wdir, self.psf)) is False:
            r1 = False
        r2 = False
        if (photsub is True) and (os.path.exists(os.path.join(self.wdir, self.psfsub)) is True):
            r2 = True

        return r1, r2, phot_idl

    def calibrate(self, cal_IDs, cal_mags, sub = False, write_dat = False):

        # aperture names
        aps = ['3.5p', '5.0p', '7.0p', '9.0p', '1.0fh', '1.5fh', '2.0fh', 'psf']
        col_names = ('id','ximage','yimage') + tuple(('{}{}'.format(m, e) for m in aps for e in ('', '_err')))

        # load raw photometry
        if self.phot_raw is None:
            self.phot_raw = pd.read_csv(self.psf, header = None, delim_whitespace = True, comment = ';', index_col = 0, 
                            names = col_names, skiprows = 1)
            self.phot_raw.index = self.phot_raw.index - 2 # align with indexing of cal stars
        if (self.phot_sub_raw is None) and (sub is True):
            self.phot_sub_raw = pd.read_csv(self.psfsub, header = None, delim_whitespace = True, comment = ';', index_col = 0, 
                                names = col_names, skiprows = 1)
            self.phot_sub_raw.index = self.phot_sub_raw.index - 2

        # ref stars in sub are the same as in un sub so only need to find cal mags once
        cal_mag_mean = cal_mags.loc[cal_IDs].mean()
        instrument_mag_mean = self.phot_raw.loc[cal_IDs, aps].mean(axis = 0)
        zp_offset = cal_mag_mean - instrument_mag_mean

        # get coords of ref stars in obs
        cs = WCS(header = self.header)
        ra, dec = cs.all_pix2world(self.phot_raw['ximage'], self.phot_raw['yimage'], 1)
        self.phot_raw.loc[:, 'RA_obs'] = ra
        self.phot_raw.loc[:, 'DEC_obs'] = dec

        # write psf zeropoint (only do once)
        with open(self.zerotxt, 'w') as f:
            f.write(str(25 + zp_offset['psf']))

        # calibrate photometry
        self.phot = self.phot_raw.copy(deep = True)
        self.phot.loc[:, aps] = self.phot.loc[:, aps] + zp_offset
        if sub is True:
            self.phot_sub = self.phot_sub_raw.copy(deep = True)
            self.phot_sub.loc[:, aps] = self.phot_sub.loc[:, aps] + zp_offset

        # write dat files if requested
        if write_dat is True:
            self.phot.index = self.phot.index + 2
            with open(self.psfdat, 'w') as outfile:
                outfile.write(''.join(['{:<8}'.format(ii) for ii in [';;id', 'ximage', 'yimage', '3.5p', 'err', '5.0p', 'err', '7.0p', 'err', '9.0p', 'err', '1.0fh', 'err', '1.5fh', 'err', '2.0fh', 'err', 'psf', 'err']]) + '\n')
                outfile.write(self.phot.loc[:,list(col_names)[1:]].to_string(header = False, index_names = False, float_format = '%.3f', col_space = 7))
            self.phot.index = self.phot.index - 2
            if sub is True:
                self.phot_sub.index = self.phot_sub.index + 2
                with opne(self.psfsubdat, 'w') as outfile:
                    outfile.write(''.join(['{:<8}'.format(ii) for ii in [';;id', 'ximage', 'yimage', '3.5p', 'err', '5.0p', 'err', '7.0p', 'err', '9.0p', 'err', '1.0fh', 'err', '1.5fh', 'err', '2.0fh', 'err', 'psf', 'err']]) + '\n')
                    outfile.write(self.phot_sub.loc[:,list(col_names)[1:]].to_string(header = False, index_names = False, float_format = '%.3f', col_space = 7))
                self.phot_sub.index = self.phot_sub.index - 2

        # return photometry for checking
        return self.phot
