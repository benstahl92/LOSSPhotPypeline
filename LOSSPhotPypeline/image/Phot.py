# standard imports
import pandas as pd
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import os

# internal imports
from LOSSPhotPypeline.image.FileNames import FileNames
from LOSSPhotPypeline.image.FitsInfo import FitsInfo
import LOSSPhotPypeline.utils as LPPu

class Phot(FitsInfo):

    def __init__(self, name, radecfile = None, radec = None):

        FitsInfo.__init__(self, name)

        self.radecfile = radecfile
        self.radec = radec

        if (self.radec is None) and (self.radecfile is not None):
            self.radec = pd.read_csv(self.radecfile, delim_whitespace=True, skiprows = (0,1,3,4,5), names = ['RA','DEC'])

        # get and set fwhm
        self.get_fwhm()

    def gen_obj_fl(self):
        '''generates obj file'''

        # convert to pixel coordinates in current image and save
        cs = WCS(header = self.header)
        imagex, imagey = cs.all_world2pix(self.radec['RA'], self.radec['DEC'], 1)
        pd.DataFrame({'x': imagex, 'y': imagey}).to_csv(self.obj, sep = '\t', index=False, header = False, float_format='%9.4f')

    def do_photometry(self, photsub = False, log = None):
        '''
        performs photometry by wrapping an IDL procedure
        '''

        # do necessary pre-steps
        self.gen_obj_fl()

        # formulate and run idl command
        if photsub is False:
            ps = ''
        else:
            ps = '/PHOTSUB, '
        idl_cmd = '''idl -e "lpp_phot_psf, '{}', fwhm = {}, exposures = {}, /SAVESKY, {}/OUTPUT"'''.format(self.cimg, self.fwhm, self.exptime, ps)
        LPPu.idl(idl_cmd, log = log)

        r1 = True
        if os.path.exists(self.psf) is False:
            r1 = False
        r2 = False
        if (photsub is True) and (os.path.exists(self.psfsub) is True):
            r2 = True

        return r1, r2

    def galaxy_subtract(self, template_images, log = None):

        if self.telescope.lower() == 'kait':
            cmd = 'lpp_kait_photsub'
        else:
            print('Telescope ({}) not implemented. Exiting.'.format(self.telescope))
            return

        # execute idl commmand
        idl_cmd = '''idl -e "{}, '{}', '{}', /OUTPUT"'''.format(cmd, self.cimg, template_images[self.filter.upper()])
        LPPu.idl(idl_cmd, log = log)

        # might want to add interactivity here to check the subtraction

