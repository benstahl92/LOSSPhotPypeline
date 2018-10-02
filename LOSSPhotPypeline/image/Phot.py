# standard imports
import pandas as pd
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import inspect
import os
import pidly
import sewpy

# internal imports
import LOSSPhotPypeline
from LOSSPhotPypeline.image.FileNames import FileNames
from LOSSPhotPypeline.image.FitsInfo import FitsInfo

class Phot(FitsInfo, FileNames):

    def __init__(self, name, radecfile = None, radec = None, quiet_idl = True, idl = None):

        FitsInfo.__init__(self, name)
        FileNames.__init__(self, name)

        self.radecfile = radecfile
        self.radec = radec

        if (self.radec is None) and (self.radecfile is not None):
            self.radec = pd.read_csv(self.radecfile, delim_whitespace=True, skiprows = (0,1,3,4,5), names = ['RA','DEC'])

        # setup idl
        if type(idl) is pidly.IDL:
            self.idl = idl
        else:
            self.idl = pidly.IDL()
            if quiet_idl:
                self.idl('!quiet = 1')
                self.idl('!except = 0')

    def get_fwhm(self):
        '''runs SExtractor to determine and write fwhm file'''

        # get paths to needed files
        sxcp = os.path.join(os.path.dirname(inspect.getfile(LOSSPhotPypeline)), 'conf', 'sextractor_config')
        filt = os.path.join(sxcp, 'gauss_2.0_5x5.conv')
        par = os.path.join(sxcp, 'fwhm.par')
        star = os.path.join(sxcp, 'default.nnw')

        # set up configuration dictionary to override SExtractor defaults
        cf = {'PARAMETERS_NAME': par,
              'DETECT_MINAREA': 10,
              'DETECT_THRESH': 3,
              'ANALYSIS_THRESH': 3.5,
              'FILTER_NAME': filt,
              'DEBLEND_MINCOUNT': 0.0001,
              'MASK_TYPE': 'NONE',
              'SATUR_LEVEL': 36000.0,
              'MAG_ZEROPOINT': 25.0,
              'GAIN': 3,
              'PIXEL_SCALE': 0.7965,
              'SEEING_FWHM': 4.17,
              'STARNNW_NAME': star,
              'BACK_SIZE': 8,
              'BACKPHOTO_THICK': 24,
              'WEIGHT_TYPE': 'BACKGROUND',
              'WEIGHT_GAIN': 'Y'}

        # run SExtractor and get results
        sew = sewpy.SEW(config = cf, configfilepath = sxcp)
        res = sew(self.cimg)["table"]
        self.fwhm = np.median(res["FWHM_IMAGE"])

        # set in the fits image
        hdulist = fits.open(self.cimg, mode = 'update')
        hdulist[0].header['fwhm'] = self.fwhm
        hdulist.close(output_verify = 'ignore')

        # write output file
        with open(self.fwhm_fl, 'w') as f:
            f.write('{:.3f}'.format(self.fwhm))

    def do_photometry(self, method = 'psf', photsub = False, log = None):
        '''
        performs aperture/psf photometry by running shell scripts to generate needed files then wrapping an IDL procedure
        '''

        # generate fwhm file
        self.get_fwhm()

        # generate obj file --- convert to pixel coordinates in current image and save
        cs = WCS(header = self.hdulist[0].header)
        imagex, imagey = cs.all_world2pix(self.radec['RA'], self.radec['DEC'], 1)
        pd.DataFrame({'x': imagex, 'y': imagey}).to_csv(self.obj, sep = '\t', index=False, header = False, float_format='%9.4f')

        # select photometry method
        if 'psf' in method.lower():
            cmd = 'lpp_phot_psf'
        else:
            cmd = 'lpp_phot_apt'

        # run idl photometry routine
        if not photsub:
            self.idl.pro(cmd, self.cimg, exposures = self.exptime, savesky = True, output = True)
        else:
            self.idl.pro(cmd, self.cimg, exposures = self.exptime, savesky = True, photsub = True, output = True)

    def galaxy_subtract(self, template_images):

        if self.telescope.lower() == 'kait':
            cmd = 'lpp_kait_photsub'
        else:
            print('Telescope ({}) not implemented. Exiting.'.format(self.telescope))
            return

        # execute idl commmand
        self.idl.pro(cmd, self.cimg, template_images[self.filter], output = True)

        # might want to add interactivity here to check the subtraction

