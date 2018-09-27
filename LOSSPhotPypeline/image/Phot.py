# standard imports
import pandas as pd
from astropy.io import fits
from astropy.wcs import WCS
import subprocess
import pidly

# internal imports
from LOSSPhotPypeline.image.FileNames import FileNames
from LOSSPhotPypeline.image.FitsInfo import FitsInfo

class Phot(FitsInfo,FileNames):

    def __init__(self, name, radecfile = None, radec = None, quiet_idl = True):

        FitsInfo.__init__(self, name)
        FileNames.__init__(self, name)

        self.radecfile = radecfile
        self.radec = radec

        if (self.radecfile is None) and (self.radec is None):
            print('must pass either radecfile or radec dataframe, exiting')
            return
        if self.radec is None:
            self.radec = pd.read_csv(self.radecfile, delim_whitespace=True, skiprows = (0,1,3,4,5), names = ['RA','DEC'])

        self.idl = pidly.IDL()
        if quiet_idl:
            self.idl('!quiet = 1')
            self.idl('!except = 0')

    def do_photometry(self, method = 'psf', photsub = False, log = None):
        '''
        performs aperture/psf photometry by running shell scripts to generate needed files then wrapping an IDL procedure

        B. Stahl - June 20, 2018
        '''

        # generate fwhm file
        p = subprocess.Popen(['LPP_get_fwhm.sh', self.cimg], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if log is None:
            print(p.communicate)
        else:
            log.debug(p.communicate())

        # generate obj file

        # convert to pixel coordinates in current image and save
        im = fits.open(self.cimg)
        cs = WCS(header=im[0].header)
        imagex, imagey = cs.all_world2pix(self.radec['RA'], self.radec['DEC'], 1) # may need to manually remove points that are nan
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

