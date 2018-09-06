# standard imports
import os
import pandas as pd
from astropy.io import fits
from astropy.wcs import WCS
import pidly

# internal imports
from LOSSPhotPypeline.image.FileNames import FileNames
from LOSSPhotPypeline.image.FitsInfo import FitsInfo

class Phot(FitsInfo,FileNames):

    def __init__(self, name, radecfile = None, quiet_idl = True, template_images = None):

        FitsInfo.__init__(self, name)
        FileNames.__init__(self, name)

        self.radecfile = radecfile
        self.template_images = template_images

        self.idl = pidly.IDL()
        if quiet_idl:
            self.idl('!quiet = 1')
            self.idl('!except = 0')

    def do_photometry(self, method = 'psf'):
        '''
        performs aperture/psf photometry by running shell scripts to generate needed files then wrapping an IDL procedure

        B. Stahl - June 20, 2018
        '''

        # generate fwhm file
        os.system('LPP_get_fwhm.sh {}'.format(self.cimg))

        # generate obj file

        # read radec file: later optimization store in memory so don't have to read every time
        radec = pd.read_csv(self.radecfile, delim_whitespace=True, skiprows = (0,1,3,4,5), names = ['RA','DEC'])

        # convert to pixel coordinates in current image and save
        im = fits.open(self.cimg)
        cs = WCS(header=im[0].header)
        imagex, imagey = cs.all_world2pix(radec['RA'], radec['DEC'], 1) # may need to manually remove points that are nan
        pd.DataFrame({'x': imagex, 'y': imagey}).to_csv(self.obj, sep = '\t', index=False, header = False, float_format='%9.4f')

        # select photometry method
        if 'psf' in method.lower():
            cmd = 'lpp_phot_psf'
        else:
            cmd = 'lpp_phot_apt'

        # run idl photometry routine
        self.idl.pro(cmd, self.cimg, exposures = self.exptime, savesky = True)

    def galaxy_subtract(self):

        if self.template_images is None:
            print('Missing dictionary of template images.')
            return

        if self.telescope.lower() == 'kait':
            cmd = 'lpp_kait_galaxy_subtract'
        else:
            print('Telescope ({}) not implemented. Exiting.'.format(self.telescope))
            return

        # execute idl commmand
        self.idl(cmd, self.cimg, self.template_images[self.filter])

        # might want to add interactivity here to check the subtraction

        # incomplete!!!
