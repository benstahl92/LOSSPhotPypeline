# standard imports
import pandas as pd
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import os
import pidly

# internal imports
from LOSSPhotPypeline.image.FileNames import FileNames
from LOSSPhotPypeline.image.FitsInfo import FitsInfo

class Phot(FitsInfo):

    def __init__(self, name, radecfile = None, radec = None, quiet_idl = True, idl = None):

        FitsInfo.__init__(self, name)

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

    def gen_obj_fl(self):
        '''generates obj file'''

        # convert to pixel coordinates in current image and save
        cs = WCS(header = self.hdulist[0].header)
        imagex, imagey = cs.all_world2pix(self.radec['RA'], self.radec['DEC'], 1)
        pd.DataFrame({'x': imagex, 'y': imagey}).to_csv(self.obj, sep = '\t', index=False, header = False, float_format='%9.4f')

    def do_photometry(self, method = 'psf', photsub = False, log = None):
        '''
        performs aperture/psf photometry by running shell scripts to generate needed files then wrapping an IDL procedure
        '''

        self.gen_obj_fl()

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

