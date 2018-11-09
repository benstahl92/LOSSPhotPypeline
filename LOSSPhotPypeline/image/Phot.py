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

