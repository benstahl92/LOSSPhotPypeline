# standard imports
import os
import glob
import shutil
import inspect
from pprint import pprint
import pickle as pkl
import copy
import pandas as pd
import numpy as np
from tqdm import tqdm
import logging
import subprocess
import warnings
from astropy.io import fits
from astropy.wcs import WCS
from astropy.utils.exceptions import AstropyWarning
warnings.simplefilter('ignore', AstropyWarning)

try:
    from p_tqdm import p_map
    _parallel = True
except ModuleNotFoundError:
    print('package "p_tqdm" not installed, cannot do parallel processing')
    _parallel = False

# internal imports
import LOSSPhotPypeline
import LOSSPhotPypeline.utils as LPPu
from LOSSPhotPypeline.image import Phot, FitsInfo, FileNames

# setup tqdm for pandas
tqdm.pandas()

class LPP(object):
    '''Lick Observatory Supernova Search Photometry Reduction Pipeline'''

    def __init__(self, targetname, interactive = True, parallel = True, cal_diff_tol = 0.05, force_color_term = False):
        '''Instantiation instructions'''

        # basics from instantiation
        self.targetname = targetname.lower().replace(' ', '')
        self.config_file = targetname + '.conf'
        self.interactive = interactive
        if (parallel is True) and (_parallel) is True:
            self.parallel = True
        else:
            self.parallel = False
        self.cal_diff_tol = cal_diff_tol
        self.abs_cal_tol = 0.2 # do not proceed with the pipeline if in non-interactive mode and cal tol exceeds this
        self.min_ref_num = 3 # minimum number of ref stars
        self.checks = ['filter', 'date'] # default checks to perform on image list
        self.phase_limits = (-60, 2*365) # phase bounds in days relative to disc. date to keep if "date" check performed

        # log file
        self.logfile = self.targetname.lower().replace(' ', '') + '.log'
        self.build_log()

        # to be sourced from configuration file
        self.targetra = None
        self.targetdec = None
        self.photsub = False
        self.photmethod = 'all'
        self.refname = 'TBD'
        self.photlistfile = 'TBD'

        # discovery date (mjd)
        self.disc_date_mjd = None

        # check if config file exists -- if not then generate template
        if not os.path.exists(self.config_file):
            self.log.warn('No configuration file detected, complete template ({}) before proceeding.'.format(self.config_file + '.template'))
            LPPu.genconf(targetname = self.targetname, config_file = self.config_file + '.template')
            return

        # general variables
        self.filter_set_ref = ['B', 'V', 'R', 'I', 'CLEAR']
        self.first_obs = None
        self.phot_cols = {'3.5p': 3, '5p': 5, '7p': 7, '9p': 9, '1fh': 11, '1.5fh': 13, '2fh': 15, 'psf': 17}
        self.calmethod = 'psf' # can be set to any key in phot_cols, but recommended is 'psf'
        self.image_list = [] # list of image file names
        self.phot_instances = [] # Phot instance for each image
        self.aIndex = [] # indices of all images in phot_instances
        self.wIndex = [] # subset of aIndex to work on
        self.bfIndex = [] # indices of images with unsupported filters
        self.ucIndex = [] # indices of WCS fail images, even though _c
        self.bdIndex = [] # indices of images with dates outside of phase boundaries
        self.pfIndex = [] # indices of photometry failures
        self.psfIndex = [] # indices of photometry (sub) failures
        self.cfIndex = [] # indices of calibration failures
        self.csfIndex = [] # indices of calibration (sub) failures
        self.noIndex = []
        self.nosIndex = []

        # calibration variables
        self.cal_source = 'auto'
        self.calfile = 'TBD'
        self.calfile_use = 'TBD'
        self.force_color_term = force_color_term
        self.calibration_dir = 'calibration'
        if not os.path.isdir(self.calibration_dir):
            os.makedirs(self.calibration_dir)
        self.radecfile = os.path.join(self.calibration_dir, self.targetname + '_radec.txt')

        # keep track of counts of color terms
        self.color_terms = {'kait1': 0, 'kait2': 0, 'kait3': 0, 'kait4': 0,
                            'nickel1': 0, 'nickel2': 0,
                            'Landolt': 0}
        self.color_terms_used = None

        # load configuration file
        loaded = False
        while not loaded:
            try:
                self.loadconf()
                loaded = True
            except FileNotFoundError:
                LPPu.genconf(targetname = self.targetname, config_file = self.config_file + '.template')
                print('Configuration could not be loaded. Template generated: {}'.format(self.config_file + '.template'))
                response = input('Specify configuration file (*****.conf) or q to quit > ')
                if 'q' == response.lower():
                    return
                else:
                    self.config_file = response

        # lightcurve variables
        self.lc_dir = 'lightcurve'
        self.lc_base = os.path.join(self.lc_dir, 'lightcurve_{}_'.format(self.targetname))
        self.lc_ext = {'raw': '_natural_raw.dat',
                       'bin': '_natural_bin.dat',
                       'group': '_natural_group.dat',
                       'standard': '_standard.dat'}

        # galaxy subtraction variables
        self.template_images = None
        self.templates_dir = 'templates'

        # steps in standard reduction procedure
        self.current_step = 0
        self.steps = [self.find_ref_stars,
                      self.load_images,
                      self.check_images,
                      self.do_galaxy_subtraction_all_image,
                      self.do_photometry_all_image,
                      self.get_sky_all_image,
                      self.do_calibration,
                      self.get_limmag_all_image,
                      self.generate_lc,
                      self.write_summary]

        # save file
        self.savefile = self.targetname.lower().replace(' ', '') + '.sav'
        if os.path.exists(self.savefile):
            if self.interactive:
                load = input('Load saved state from {}? ([y]/n) > '.format(self.savefile))
            else:
                load = 'y'
            if 'n' not in load.lower():
                self.load()

        # make sure that the selected calmethod is one of the photmethods
        if self.calmethod not in self.photmethod:
            self.log.warn('Calibration method must be one of the photometry methods. Exiting.')
            return

    ###################################################################################################
    #          Configuration File Methods
    ###################################################################################################

    def loadconf(self):
        '''
        reads config file and sets class attributes accordingly
        the most accurate accounting of system state is stored in the binary savefile
        '''

        # load config file and try to standardize keys
        conf = pd.read_csv(self.config_file, header = None, delim_whitespace = True, comment = '#',
                           index_col = 0, squeeze = True).replace(np.nan, '')
        conf.index = conf.index.str.lower()

        # read and set values (including the type)
        self.targetra = float(conf['targetra'])
        self.targetdec = float(conf['targetdec'])
        if conf['photsub'].lower() == 'yes': # defaults to False in all other cases
            self.photsub = True 
        if conf['calsource'].lower() in ['psf','sdss','apass']: # only set if a known source is specified
            self.cal_source = conf['calsource'].lower() 
        if conf['photmethod'].lower() == 'all':
            self.photmethod = list(self.phot_cols.keys())
        elif ',' not in conf['photmethod'].lower():
            if conf['photmethod'].lower().strip() in self.phot_cols.keys():
                self.photmethod = [conf['photmethod'].lower().strip()]
            else:
                print('{} is not a valid photometry method. Available options are:'.format(conf['photmethod'].strip()))
                print(', '.join(self.phot_col.keys()))
                self.photmethod = input('Enter selection(s) > ').strip().replace(' ', '').split(',')
        else:
            proposed = conf['photmethod'].strip().split(',')
            if set(proposed).issubset(set(self.phot_cols.keys())):
                self.photmethod = proposed
            else:
                print('At least one of {} is not a valid photometry method. Available options are:'.format(conf['photmethod'].strip()))
                print(', '.join(self.phot_cols.keys()))
                self.photmethod = input('Enter selection(s) > ').strip().replace(' ', '').split(',')

        self.refname = conf['refname']
        self.photlistfile = conf['photlistfile']

        if conf['forcecolorterm'].strip() in self.color_terms.keys():
            self.force_color_term = conf['forcecolorterm'].strip()

        self.log.info('{} loaded'.format(self.config_file))

    ###################################################################################################
    #          Logging
    ###################################################################################################

    def build_log(self):
        '''starts and sets up log'''

        self.log = logging.getLogger('LOSSPhotPypeline')
        self.log.setLevel(logging.DEBUG)

        # don't duplicate entries
        if self.log.hasHandlers():
            self.log.handlers.clear()

        # internal logging
        fh = logging.FileHandler(self.logfile)
        fh.setFormatter(logging.Formatter('%(asctime)s in %(funcName)s with level %(levelname)s ::: %(message)s'))
        self.log.addHandler(fh)

        # if in interactive mode, print log at or above INFO on screen
        if self.interactive:
             sh = logging.StreamHandler()
             sh.setLevel(logging.INFO)
             sh.setFormatter(logging.Formatter('\n'+'*'*60+'\n%(message)s\n'+'*'*60))
             self.log.addHandler(sh)

        # used by contextlib to log all idl and bash outputs, while hiding from screen
        self.log.write = lambda msg: self.log.debug('[external] ' + msg) if msg != '\n' else None

        self.log.info('Welcome to the LOSS Photometry Pypeline (LPP)')

    ###################################################################################################
    #          UI / Automation Methods
    ###################################################################################################

    def __iter__(self):
        return self

    def next(self, *args, **kwargs):
        '''performs next reduction step (arguments for that step can be passed through)'''
        if self.current_step < len(self.steps):
            self.steps[self.current_step](*args, **kwargs)
            self.current_step += 1
            self.save()
            self.summary()
        else:
            raise StopIteration

    def skip(self):
        '''skip current step'''
        self.log.info('skipping step: {}'.format(self.steps[self.current_step].__name__))
        self.go_to(self.current_step + 1)
        self.summary()

    def go_to(self, step = None):
        '''go to specified step, or choose interactively'''
        if type(step) == int:
            self.current_step = step
            self.summary()
        else:
            self.summary()
            print('\nChoose an option:\n')
            print('primary reduction steps:')
            for i, step in enumerate(self.steps):
                if i == self.current_step:
                    print('{} --- {} (current step)'.format(i, step.__name__))
                else:
                    print('{} --- {}'.format(i, step.__name__))
            print('\nadditional options:')
            print('n  --- add new image(s) by filename(s)')
            print('nf --- add new images from file of names')
            print('p  --- plot light curve from file')
            print('c  --- cut points from specific light curve')
            print('cr --- cut points from raw light curves')
            print('cs --- cut points from standard light curves')
            print('q  --- quit\n')
            resp = input('selection > ').lower()
            if 'n' == resp:
                new_images = input('enter name(s) or new images (comma separated) > ')
                if ',' not in new_images:
                    new_image_list = [new_images]
                else:
                    new_image_list = [fl.strip() for fl in new_images.split(',')]
                self.process_new_images(new_image_list = new_image_list)
            elif 'nf' == resp:
                new_image_file = input('enter name of new image file > ')
                self.process_new_images(new_image_file = new_image_file)
            elif 'p' == resp:
                lc_file = input('enter light curve file (including relative path) to plot > ')
                self.plot_lc([lc_file])
            elif 'c' == resp:
                lc_file = input('enter light curve file (including relative path) to cut points from > ')
                self.cut_lc_points([lc_file])
            elif 'cr' == resp:
                lc_list = [os.path.join(self.lc_dir, fl) for fl in os.listdir(self.lc_dir) if ('raw' in fl) and ('cut' not in fl) and ('.dat' in fl)]
                self.cut_lc_points(lc_list)
            elif 'cs' == resp:
                lc_list = [os.path.join(self.lc_dir, fl) for fl in os.listdir(self.lc_dir) if ('standard' in fl) and ('cut' not in fl) and ('.dat' in fl)]
                self.cut_lc_points(lc_list)
            else:
                try:
                    self.current_step = int(resp)
                except ValueError:
                    return
            self.summary()

    def save(self):
        '''saves current state of pipeline'''
        vs = vars(self).copy()
        vs.pop('steps')
        vs.pop('log')
        with open(self.savefile, 'wb') as f:
            pkl.dump(vs, f)
        self.log.info('{} written'.format(self.savefile))

    def load(self, savefile = None):
        '''re-initializes pipeline from saved state in file'''
        if savefile is None:
            savefile = self.savefile
        with open(savefile, 'rb') as f:
            vs = pkl.load(f)
        for v in vs.keys():
            s = 'self.{} = vs["{}"]'.format(v, v)
            exec(s)
        self.log.info('{} loaded'.format(savefile))
        self.summary()

    def summary(self):
        '''print summary of pipeline status'''
        print('\n' + '*'*60)
        print('Reduction status for {}'.format(self.targetname))
        print('Interactive: {}'.format(self.interactive))
        print('Photsub Mode: {}'.format(self.photsub))
        print('*'*60 + '\n')
        if self.current_step == 0:
            print('Beginning of reduction pipeline.\n')
        else:
            print('Previous step: {}'.format(self.steps[self.current_step - 1].__name__))
            print(self.steps[self.current_step - 1].__doc__ + '\n')
        try:
            print('--> Next step: {}'.format(self.steps[self.current_step].__name__))
            print(self.steps[self.current_step].__doc__ + '\n')
        except IndexError:
            print('End of reduction pipeline.')
            self.save()
            return
        try:
            print('----> Subsequent step: {}'.format(self.steps[self.current_step + 1].__name__))
            print(self.steps[self.current_step + 1].__doc__ + '\n')
        except IndexError:
            print('End of reduction pipeline.')

    def run(self, skips = []):
        '''run through reduction steps'''
        while True:
            if self.current_step in skips:
                self.skip()
            else:
                try:
                    self.next()
                except StopIteration:
                    break

    def show_variables(self):
        '''prints instance variables'''
        pprint(vars(self))

    def show_methods(self):
        '''show available methods'''
        print('method: docstring')
        for name in LPP.__dict__.keys():
            if name[:2] != '__' and name != 'show_methods':
                print('{}: {}'.format(name, LPP.__dict__[name].__doc__))

    ###################################################################################################
    #          Reduction Pipeline Methods
    ###################################################################################################

    def find_ref_stars(self):
        '''identify all suitable stars in ref image, compute ra & dec, write radecfile, store in instance'''

        # if radecfile already exists, no need to do it
        if os.path.exists(self.radecfile):
            self.log.info('radecfile already exists, loading only')
            self.radec = pd.read_csv(self.radecfile, delim_whitespace=True, skiprows = (0,1,3,4,5), names = ['RA','DEC'])
            return
        if self.refname == '' :
            self.log.warn('refname has not been assigned, please do it first!')
            return

        # instantiate object to manage names
        ref = Phot(self.refname)

        # use sextractor to extract all stars to be used as refstars
        sxcp = os.path.join(os.path.dirname(inspect.getfile(LOSSPhotPypeline)), 'conf', 'sextractor_config')
        config = os.path.join(sxcp, 'kait.sex')
        filt = os.path.join(sxcp, 'gauss_2.0_5x5.conv')
        par = os.path.join(sxcp, 'kait.par')
        star = os.path.join(sxcp, 'default.nnw')
        cmd_list = ['sex', self.refname,
                    '-c', config,
                    '-PARAMETERS_NAME', par,
                    '-FILTER_NAME', filt,
                    '-STARNNW_NAME', star, 
                    '-CATALOG_NAME', ref.sobj,
                    '-CHECKIMAGE_NAME', ref.skyfit]
        p = subprocess.Popen(cmd_list, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)
        stdout, stderr = p.communicate()
        self.log.debug(stdout)
        self.log.debug(stderr)

        # make sure process succeeded
        if not os.path.exists(ref.sobj):
            self.log.warn('SExtractor failed --- no sobj file generated, check!')
            return

        # read sobj file of X_IMAGE and Y_IMAGE columns, as well as MAG_APER for sort
        with fits.open(ref.sobj) as hdul:
            data = hdul[1].data
        # sort according to magnitude, from small/bright to hight/faint
        data.sort(order = 'MAG_APER')
        imagex = data.X_IMAGE
        imagey = data.Y_IMAGE

        # transform to RA and DEC using ref image header information
        cs = WCS(header = ref.header)
        imagera, imagedec = cs.all_pix2world(imagex, imagey, 1)

        # write radec file
        with open(self.radecfile, 'w') as f:
            f.write('TARGET\n')
            f.write('          RA          DEC\n')
            f.write('   {:.7f}  {:.7f}\n'.format(self.targetra, self.targetdec))
            f.write('\nREFSTARS\n')
            f.write('          RA          DEC\n')
            for i in range(len(imagera)):
                f.write('   {:.7f}  {:.7f}\n'.format(imagera[i], imagedec[i]))

        self.log.info('{} written'.format(self.radecfile))
        self.radec = pd.read_csv(self.radecfile, delim_whitespace=True, skiprows = (0,1,3,4,5), names = ['RA','DEC'])

    def load_images(self):
        '''reads image list file to generate lists of image names and Phot instances'''

        self.image_list = pd.read_csv(self.photlistfile, header = None, delim_whitespace = True,
                                      comment = '#', squeeze = True)

        if self.interactive:
            print('\nSelected image files')
            print('*'*60 + '\n')
            print(self.image_list)
            print('\n')

        self.log.info('image list loaded from {}'.format(self.photlistfile))

        self.log.info('generating list of Phot instances from image list')
        self.phot_instances = self._im2inst(self.image_list)

        # set indices
        self.aIndex = self.image_list.index
        self.wIndex = self.aIndex

    def check_images(self):
        '''only keep images that are in a supported filter and without file format issues'''

        # filter check
        if 'filter' in self.checks:
            filter_check = lambda img: True if img.filter.upper() in self.filter_set_ref else False
            self.log.info('checking filters')
            bool_idx = self.phot_instances.loc[self.wIndex].progress_apply(filter_check)
            self.bfIndex = self.wIndex[~pd.Series(bool_idx)]
            self.log.info('dropping {} images due to unsupported filter'.format(len(self.bfIndex)))
            self.wIndex = self.wIndex.drop(self.bfIndex)

        # uncal check
        if 'uncal' in self.checks:
            cal_check = lambda img: True if ('RADECSYS' not in img.header) else (False if (img.header['RADECSYS'] == '-999') else True)
            self.log.info('checking images for WCS')
            bool_idx = self.phot_instances.loc[self.wIndex].progress_apply(cal_check)
            self.ucIndex = self.wIndex[~pd.Series(bool_idx)]
            self.log.info('dropping {} images for failed WCS'.format(len(self.ucIndex)))
            self.wIndex = self.wIndex.drop(self.ucIndex)

        if 'date' in self.checks:
            if self.disc_date_mjd is None:
                self.log.warn('discovery date not set, cannot do date check')
                return
            date_check = lambda img: True if ((img.mjd >= (self.disc_date_mjd + self.phase_limits[0])) and 
                         (img.mjd <= (self.disc_date_mjd + self.phase_limits[1]))) else False
            self.log.info('checking phases')
            bool_idx = self.phot_instances.loc[self.wIndex].progress_apply(date_check)
            self.bdIndex = self.wIndex[~pd.Series(bool_idx)]
            self.log.info('dropping {} images that are outside of phase bounds'.format(len(self.bdIndex)))
            self.wIndex = self.wIndex.drop(self.bdIndex)

    def do_galaxy_subtraction_all_image(self):
        '''performs galaxy subtraction on all selected image files'''

        if not self.photsub:
            self.log.warn('not in photsub mode, skipping galaxy subtraction')
            return

        self.log.info('starting galaxy subtraction')

        if self.template_images is None:
            self.load_templates()
            if self.template_images is None:
                self.log.warn('could not get suitable template images, running without galaxy subtraction')
                self.photsub = False
                return

        # set up for parallelization
        ti = self.template_images
        fn = lambda img: img.galaxy_subtract(ti)

        # do galaxy subtraction in the appropriate mode
        if self.parallel is True:
            res = p_map(fn, self.phot_instances.loc[self.wIndex].tolist())
        else:
            res = []
            for img in tqdm(self.phot_instances.loc[self.wIndex].tolist()):
                res.append(fn(img))

        # extract results, log, and determine if successful
        res = pd.DataFrame(res, columns = ['success', 'log'])
        res['log'].apply(lambda log_entry: self._log_idl(*log_entry))
        if not res['success'].all():
            self.log.warn('photsub failed (probably b/c of missing templates), running without galaxy subtraction')
            self._get_template_candidates()

        self.log.info('galaxy subtraction done')

    def do_photometry_all_image(self):
        '''performs photometry on all selected image files'''

        self.log.info('starting photometry (galsub: {})'.format(self.photsub))

        # set up for parallelization
        ps = self.photsub
        fn = lambda img: img.do_photometry(photsub = ps)

        # do photometry in the appropriate mode
        if self.parallel is True:
            res = p_map(fn, self.phot_instances.loc[self.wIndex].tolist())
        else:
            res = []
            for img in tqdm(self.phot_instances.loc[self.wIndex].tolist()):
                res.append(fn(img))

        # extract results, log, and remove failures
        res = pd.DataFrame(res, columns = ['unsub', 'sub', 'log'])
        res['log'].apply(lambda log_entry: self._log_idl(*log_entry))
        self.pfIndex = self.wIndex[~res['unsub']]
        self.log.warn('photometry failed on {} out of {} images'.format(len(self.pfIndex), len(self.wIndex)))
        if self.photsub is False:
            self.wIndex = self.wIndex.drop(self.pfIndex)
        else:
            self.psfIndex = self.wIndex[~res['sub']]
            self.log.warn('photometry (sub) failed on {} out of {} images'.format(len(self.psfIndex), len(self.wIndex)))
            self.wIndex = self.wIndex.drop(self.pfIndex.intersection(self.psfIndex))

        self.log.info('photometry done')

    def get_sky_all_image(self):
        '''get and set sky value for every phot instance'''

        self.log.info('getting sky value for each image')
        self.phot_instances.loc[self.wIndex].progress_apply(lambda img: img.get_sky())

    def calibrate(self, second_pass = False):
        '''performs calibration on all images included in photlistfile, using outputs from do_photometry_all_image'''

        self.log.info('commencing calibration (second pass: {})'.format(second_pass))

        # reset color term counts
        self.color_terms = {key: 0 for key in self.color_terms.keys()}

        # check if calibration files have been obtained and parse if so, otherwise generate
        if (second_pass is False) and (os.path.exists(os.path.join(self.calibration_dir, self.calfile)) is False):
            catalog = LPPu.astroCatalog(self.targetname, self.targetra, self.targetdec, relative_path = self.calibration_dir)
            catalog.get_cal(method = self.cal_source)
            if os.path.exists(os.path.join(self.calibration_dir, self._ct2cf('kait4'))) is False:
                catalog.to_natural()
            self.calfile = catalog.cal_filename
            self.cal_source = catalog.cal_source
        if (second_pass is True) and (os.path.exists(os.path.join(self.calibration_dir, self._ct2cf('kait4', use = True))) is False):
            catalog = LPPu.astroCatalog(self.targetname, self.targetra, self.targetdec, relative_path = self.calibration_dir)
            catalog.cal_filename = self.calfile_use
            catalog.cal_source = self.cal_source
            catalog.to_natural()
        self.log.info('calibration data sourced')

        # iterate through image list and execute calibration script on each
        for idx, img in tqdm(self.phot_instances.loc[self.wIndex].iteritems(), total = len(self.wIndex)):

            # count usage of color terms
            if self.force_color_term is False:
                self.color_terms[img.color_term] += 1
            else:
                self.color_terms[self.force_color_term] += 1

            # execute idl calibration procedure
            # set photsub mode appropriately
            if self.photsub is False:
                ps = ''
            elif (self.photsub is True) and (idx in self.psfIndex):
                ps = ''
            else:
                ps = '/PHOTSUB, '
            idl_cmd = '''idl -e "lpp_cal_instrumag, '{}', '{}', '{}', '{}', {}/OUTPUT"'''.format(img.cimg, img.filter.upper(), self.cal_source,
                     os.path.join(self.calibration_dir, self._ct2cf(img.color_term, use = second_pass)), ps)
            stdout, stderr = LPPu.idl(idl_cmd)
            self._log_idl(idl_cmd, stdout, stderr)

            # also get zero value
            img.get_zeromag()

            # check for success
            if (os.path.exists(img.psfdat) is False) and (second_pass is False):
                self.cfIndex.append(idx)
            if (self.photsub is True) and (os.path.exists(img.psfsubdat) is False) and (second_pass is False):
                self.csfIndex.append(idx)

        if second_pass is False:
            self.get_cal_info()
            self.cfIndex = pd.Series(self.cfIndex)
            self.csfIndex = pd.Series(self.csfIndex)
            self.log.warn('calibration failed on {} out of {} images'.format(len(self.cfIndex), len(self.wIndex)))
            self.wIndex = self.wIndex.drop(self.cfIndex) # processing based only on non-subtracted images
            if self.photsub is True:
                self.log.warn('calibration (sub) failed on {} out of {} images'.format(len(self.csfIndex), len(self.wIndex)))

    def process_calibration(self):#, photsub_mode = False):
        '''combines all calibrated results (.dat files), grouped by filter, into data structure so that cuts can be made'''

        self.log.info('processing calibration')

        # underlying data structure for handling this will be dictionary keyed by filter
        # for each key, there is another dictionary keyed by ID with each value being a list of magnitudes
        results = {}

        # generate ordered calibration file
        idl_cmd = '''idl -e "lpp_pick_good_refstars, INDGEN(225), '{}', '{}', /OUTPUT"'''.format(self.radecfile, os.path.join(self.calibration_dir, self.calfile))
        stdout, stderr = LPPu.idl(idl_cmd)
        self._log_idl(idl_cmd, stdout, stderr)
        idl_cmd = '''idl -e "lpp_cal_dat2fit_{}, '{}', /OUTPUT"'''.format(self.cal_source.lower(), os.path.join(self.calibration_dir, self.calfile_use))
        stdout, stderr = LPPu.idl(idl_cmd)
        self._log_idl(idl_cmd, stdout, stderr)

        # read ordered calibration file, using index offset to match
        cal = pd.read_csv(os.path.join(self.calibration_dir, self.calfile_use), delim_whitespace = True)
        IDs = cal['starID'] + 2

        # iterate through files and store photometry into data structure
        for idx, img in tqdm(self.phot_instances.loc[self.wIndex].iteritems(), total = len(self.wIndex)):

            filt = img.filter.upper()

            # add second level dictionary if needed
            if filt not in results.keys():
                results[filt] = {}

            # read file (using selected columns corresponding to desired photometry method(s))
            cols = (0,) + tuple((self.phot_cols[m] for m in self.photmethod))
            col_names = ('id',) + tuple((m for m in self.photmethod))
            d = pd.read_csv(img.psfdat, header = None, delim_whitespace = True, comment = ';', index_col = 0, usecols=cols, names = col_names)

            # populate results dict from file
            for idx, row in d.iterrows():
                if (idx in IDs.values) and (~np.isnan(row[self.calmethod])):
                    if idx not in results[filt].keys():
                        results[filt][idx] = [row[self.calmethod]]
                    else:
                        results[filt][idx].append(row[self.calmethod])

        # compute summary results, thereby allowing for cuts to be made
        # also include calibration magnitudes and differences

        # use "use" calfit file with color term that represents the most images
        ct = max(self.color_terms, key = lambda k: self.color_terms[k])
        cf = self._ct2cf(ct, use = True)
        im = fits.open(os.path.join(self.calibration_dir, cf))
        accept_tol = False
        while not accept_tol:
            summary_results = {}
            cut_list = [] # store IDs that will be cut
            full_list = []
            for filt in results.keys():
                if filt not in summary_results.keys():
                    summary_results[filt] = {}
                for ID in results[filt].keys():
                    if len(im[1].data[filt][cal['starID'] == (ID-2)]) > 0:
                        obs = np.median(results[filt][ID])
                        ref = im[1].data[filt][cal['starID'] == (ID - 2)].item()
                        diff = np.abs(obs - ref)
                        summary_results[filt][ID] = [obs, ref, diff]
                        if diff > self.cal_diff_tol:
                            cut_list.append(ID - 2)
                        full_list.append(ID - 2)

            cut_list = list(set(cut_list))
            full_list = list(set(full_list))
            if not self.interactive:
                if len(full_list) - len(cut_list) < self.min_ref_num:
                    self.cal_diff_tol += 0.05
                    if self.cal_diff_tol > self.abs_cal_tol:
                        self.log.warn('calibration tolerance exceeds {}, cannot proceed'.format(self.abs_cal_tol))
                        self.current_step = self.steps.index(self.write_summary)
                        self.run()
                        return
                else:
                    accept_tol = True
            else:
                print('\nCalibration Summary')
                print('*'*60)
                for filt in summary_results.keys():
                    print('\nFilter: {}'.format(filt))
                    print('*'*60)
                    print(pd.DataFrame.from_dict(summary_results[filt], orient = 'index', columns = ['Obs Mag', 'Cal Mag', 'Diff']).sort_index())

                print('\nAt tolerance {}, {} IDs (out of {}) will be cut'.format(self.cal_diff_tol, len(cut_list), len(full_list)))
                print('*'*60)
                print([i + 2 for i in sorted(cut_list)])
                response = input('\nAccept cuts with tolerance of {} mag ([y])? If not, enter new tolerance > '.format(self.cal_diff_tol))
                if (response == '') or ('y' in response.lower()):
                    accept_tol = True
                else:
                    self.cal_diff_tol = float(response)

        im.close()
        self.log.info('processing done, cutting IDs {} due to tolerance: {}'.format(np.array(cut_list) + 2, self.cal_diff_tol))

        # write new calibration file
        os.system('mv {} tmp.tmp'.format(os.path.join(self.calibration_dir, self.calfile_use)))
        with open('tmp.tmp', 'r') as infile:
            with open(os.path.join(self.calibration_dir, self.calfile_use), 'w') as outfile:
                for idx, line in enumerate(infile):
                    if idx == 0:
                        outfile.write(line)
                    else:
                        ID = int(line.split(' ')[0])
                        if ID not in cut_list:
                            outfile.write(line)
        os.system('rm tmp.tmp')

    def do_calibration(self):
        '''executes full calibration routine'''

        # if calfile_use exists, first pass and cuts have been done
        self.get_cal_info()
        if os.path.exists(os.path.join(self.calibration_dir, self.calfile_use)) is False:
            self.calibrate()
            self.process_calibration()
        self.calibrate(second_pass = True)

        self.log.info('full calibration sequence completed')

    def get_limmag_all_image(self):
        '''get and set limiting mag for every phot instance'''

        self.log.info('getting limiting mag for each image')
        self.phot_instances.loc[self.wIndex].progress_apply(lambda img: img.calc_limmag())

    def generate_raw_lcs(self, color_term, photsub_mode = False):
        '''builds raw light curve files from calibrated results'''

        columns = (';; MJD','etburst', 'mag', '-emag', '+emag', 'limmag', 'filter', 'imagename')
        lc = {name: [] for name in columns}
        lcs = {m: copy.deepcopy(lc) for m in self.photmethod}

        # iterate through files and extract LC information
        for idx, img in self.phot_instances.loc[self.wIndex].iteritems():

            # immediately skip if not the appropriate color term unless being forced
            if (color_term != img.color_term) and (self.force_color_term is False):
                continue

            # skip failed images
            if (idx in self.cfIndex) and (photsub_mode is False):
                continue
            elif ((idx in self.psfIndex) or (idx in self.csfIndex)) and (photsub_mode is True):
                continue

            # read photometry results
            cols = (0,) + sum(((self.phot_cols[m], self.phot_cols[m] + 1) for m in self.photmethod), ())
            col_names = ('ID',) + sum(((m + '_mag', m + '_err') for m in self.photmethod), ())
            if photsub_mode is False:
                dat = img.psfdat
            else:
                dat = img.psfsubdat
            d = pd.read_csv(dat, header = None, delim_whitespace = True, comment = ';', usecols=cols, names = col_names)

            # detect if no target in file
            if 1 not in d['ID'].values:
                self.log.warn('no object in calibrated photometry file: {}'.format(dat))
                if photsub_mode is False:
                    self.no_obj.append(idx)
                else:
                    self.no_obj_sub.append(idx)

            # setup columns for each raw file
            for m in self.photmethod:
                lcs[m][';; MJD'].append(round(img.mjd, 6))
                lcs[m]['etburst'].append(round(img.exptime / (60 * 24), 5)) # exposure time in days
                lcs[m]['filter'].append(img.filter)
                lcs[m]['imagename'].append(img.cimg)
                lcs[m]['limmag'].append(round(img.limmag, 5))
                if 1 not in d['ID'].values:
                    mag = np.nan
                    err = np.nan
                else:
                    mag = d[d['ID'] == 1][m + '_mag'].item()
                    err = d[d['ID'] == 1][m + '_err'].item()
                lcs[m]['mag'].append(round(mag,5))
                lcs[m]['-emag'].append(round(mag - err,5))
                lcs[m]['+emag'].append(round(mag + err,5))

        # write raw lc files
        for m in self.photmethod:
            lc_raw_name = self._lc_fname(color_term, m, 'raw', sub = photsub_mode)
            lc_raw = pd.DataFrame(lcs[m])
            lc_raw.to_csv(lc_raw_name, sep = '\t', columns = columns, index = False, na_rep = 'NaN')
            p = LPPu.plotLC(lc_file = lc_raw_name, name = self.targetname, photmethod = m)
            p.plot_lc(extensions = ['.ps', '.png'])

    def generate_bin_lc(self, infile, outfile):
        '''wraps IDL lightcurve binning routine'''

        idl_cmd = '''idl -e "lpp_dat_res_bin, '{}', '{}', OUTFILE='{}', /OUTPUT"'''.format(infile, outfile, outfile)
        stdout, stderr = LPPu.idl(idl_cmd)
        self._log_idl(idl_cmd, stdout, stderr)

    def generate_group_lc(self, infile, outfile):
        '''wraps IDL lightcurve grouping routine'''

        idl_cmd = '''idl -e "lpp_dat_res_group, '{}', '{}', OUTFILE='{}'"'''.format(infile, outfile, outfile)
        stdout, stderr = LPPu.idl(idl_cmd)
        self._log_idl(idl_cmd, stdout, stderr)

    def generate_final_lc(self, color_term, infile, outfile):
        '''wraps IDL routine to convert to natural system'''

        idl_cmd = '''idl -e "lpp_invert_natural_stand_objonly, '{}', '{}', OUTFILE='{}', /OUTPUT"'''.format(infile, color_term, outfile)
        stdout, stderr = LPPu.idl(idl_cmd)
        self._log_idl(idl_cmd, stdout, stderr)

    def raw2standard_lc(self, infile):
        '''wrap intermediate steps that transform light curves from "raw" to "standard"'''

        # assign convenience variables
        tmp = infile.split('_')
        ct = tmp[tmp.index('natural') - 2] # get color term
        m = tmp[tmp.index('natural') - 1] # get phot aperture
        binfile = infile.replace('raw', 'bin')
        groupfile = binfile.replace('bin', 'group')
        lc = groupfile.replace('natural_group', 'standard')

        # do intermediate light curve steps
        self.generate_bin_lc(infile, binfile)
        self.generate_group_lc(binfile, groupfile)
        self.generate_final_lc(ct, groupfile, lc)

        # plot
        p = LPPu.plotLC(lc_file = lc, name = self.targetname, photmethod = m)
        p.plot_lc(extensions = ['.ps', '.png'])

    def generate_lc(self, sub = False):
        '''performs all functions to transform image photometry into calibrated light curve of target'''

        self.log.info('generating and plotting light curves (sub mode: {})'.format(sub))

        # set up file system
        if not os.path.isdir(self.lc_dir):
            os.makedirs(self.lc_dir)

        # select only colors terms that are used
        self.color_terms_used = {key: self.color_terms[key] for key in self.color_terms.keys() if self.color_terms[key] > 0}

        # generate raw light curves
        self.log.info('generating raw light curves for the following color terms: {}'.format(', '.join(self.color_terms_used.keys())))
        for ct in tqdm(self.color_terms_used.keys()):
            self.generate_raw_lcs(ct, photsub_mode = sub)

        # generate intermediate and final light curves
        self.log.info('generating "standard" light curves')
        for m in tqdm(self.photmethod):
            all_tmp = []
            for ct in self.color_terms_used.keys():
                self.raw2standard_lc(self._lc_fname(ct, m, 'raw', sub = sub))
                all_tmp.append(self._lc_fname(ct, m, 'standard', sub = sub))
            # make "all" light curves
            lc = self._lc_fname('all', m, 'standard', sub = sub)
            concat_list = []
            for fl in all_tmp:
                concat_list.append(pd.read_csv(fl, delim_whitespace = True))
            pd.concat(concat_list, sort = False).to_csv(lc, sep = '\t', na_rep = 'NaN', index = False)
            p = LPPu.plotLC(lc_file = lc, name = self.targetname, photmethod = m)
            p.plot_lc(extensions = ['.ps', '.png'])

        self.log.info('done with light curves')

        # use recursion to handle sub if needed
        if (self.photsub is True) and (sub is False):
            self.generate_lc(sub = True)

    def write_summary(self):
        '''write summary file'''

        if self.current_step != (len(self.steps) - 1):
            print('processing must be done before summary can be written')
            return

        # get filters used
        self.filters = set(self.phot_instances.loc[self.wIndex].apply(lambda img: img.filter.upper()))

        self.summary_file = self.targetname + '.summary'
        with open(self.summary_file, 'w') as f:
            f.write('{:<25}{}\n'.format('targetname', self.targetname))
            f.write('{:<25}{}\n'.format('photsub', self.photsub))
            f.write('{:<25}{}\n'.format('filters', ', '.join(self.filters)))
            f.write('{:<25}{}\n'.format('apertures', ', '.join(self.photmethod)))
            f.write('{:<25}{}\n'.format('calmethod', ', '.join(self.calmethod)))
            f.write('{:<25}{}\n'.format('color_terms',', '.join(self.color_terms_used.keys())))
            f.write('{:<25}{}\n'.format('num images', len(self.phot_instances)))
            f.write('{:<25}{}\n'.format('num failures', len(self.aIndex) - len(self.wIndex)))
            f.write('{:<25}{}\n'.format('num non-sup. filt.', len(self.bfIndex)))
            f.write('{:<25}{}\n'.format('num w/ bad WCS', len(self.ucIndex)))
            f.write('{:<25}{}\n'.format('cal source', self.cal_source))
            f.write('{:<25}{}\n'.format('cal tolerance', round(self.cal_diff_tol, 2)))

        self.log.info('pipeline complete, summary file written')
        self.save()

    ###################################################################################################
    #          Utility Methods
    ###################################################################################################

    def process_new_images(self, new_image_file = None, new_image_list = []):
        '''processes images obtained after initial processing'''

        # read in new images to list
        if (new_image_file is not None) and (new_image_list == []):
            new_image_list = pd.read_csv(new_image_file, header = None, delim_whitespace = True,
                                          comment = '#', squeeze = True)
        elif new_image_list != []:
            new_image_list = pd.Series(new_image_list)

        # remove any images from new list that have already been processed
        new_image_list = new_image_list[~new_image_list.isin(self.image_list)]
        offset = self.aIndex[-1] + 1
        tmp = self.wIndex
        self.wIndex = pd.RangeIndex(start = offset, stop = offset + len(new_image_list))

        # update image list to include everything, and update phot_instances
        self.log.info('loading new images')
        self.image_list = self.image_list.append(new_image_list, ignore_index = True)
        self.phot_instances = self.phot_instances.append(self._im2inst(new_image_list), ignore_index = True)

        # perform galaxy_subtraction and photometry on new images
        self.do_galaxy_subtraction_all_image()
        self.do_photometry_all_image()
        self.get_sky_all_image()

        # perform calibration
        full_cal = False
        if self.interactive:
            resp = input('\nperform full re-calibration? (y/[n]) > ')
            if 'y' in resp.lower():
                full_cal = True
        if full_cal:
            self.current_step = self.steps.index(self.do_calibration)
        else:
            self.calibrate(second_pass = True)
            self.get_limmag_all_image()
            self.current_step = self.steps.index(self.generate_lc)

        # run program after calibration has been completed (on all images)
        self.wIndex = tmp.append(self.wIndex)
        self.run()

        # add to original image file and remove new file
        if new_image_file is not None:
            ow = True
            if self.interactive:
                resp = input('\nadd {} to {} and then remove {}? (y/[n]) > '.format(new_image_file, self.photlistfile, new_image_file))
                if 'y' not in resp.lower():
                    ow = False
            if ow:
                os.system('cat {} >> {}'.format(new_image_file, self.photlistfile))
                os.system('rm {}'.format(new_image_file))

        self.log.info('new images processed')

    def load_templates(self):
        '''search templates dir, setup, and convert formats as needed'''

        succ = True
        self.template_images = {'{}_{}'.format(f, tel): None for f in ['B', 'V', 'R', 'I'] for tel in ['kait', 'nickel']}
        self.template_images['CLEAR_kait'] = None # no clear for Nickel

        if os.path.exists(self.templates_dir) is False:
            succ = False
            msg = 'no templates directory, cannot do photsub'
        else:
            templates = glob.glob('{}/*.fit'.format(self.templates_dir))
            if len(templates) == 0:
                succ = False

        if succ is True:
            if len(templates) < 5: # 5 passbands
                # warn if not enough templates found (but may be ok if not all needed)
                msg = 'warning: did not find templates for every passband'

            for templ in templates:
                ti = FitsInfo(templ)
                filt = ti.filter.upper()
                if (ti.telescope.lower() == 'nickel') and (filt != 'CLEAR') and ('n2k_c.fit' not in templ):
                    self.template_images['{}_nickel'.format(filt)] = ti.cimg
                    # also rebin for kait
                    self.template_images['{}_kait'.format(filt)] = ti.cimg.replace('c.fit', 'n2k_c.fit')
                    idl_cmd = '''idl -e "lpp_rebin_nickel2kait, '{}', SAVEFILE='{}'"'''.format(ti.cimg, self.template_images['{}_kait'.format(filt)])
                    stdout, stderr = LPPu.idl(idl_cmd)
                    self._log_idl(idl_cmd, stdout, stderr)
                elif (ti.telescope.lower() == 'kait') and (filt == 'CLEAR') and ('n2k_c.fit' not in templ):
                    self.template_images['CLEAR_kait'] = ti.cimg
                elif 'n2k_c.fit' in templ:
                    pass
                else:
                    succ = False
                    msg = 'either BVRI templates are not from Nickel or CLEAR template is not from KAIT, cannnot do photsub'
                    break

        if succ is True:
            self.log.info('templates loaded')
            return

        # otherwise process is not a success, search for candidates but proceed without photsub
        self.log.warning(msg)
        self.log.warning('switching to non-subtraction mode, but searching for template candidates')
        self.template_images = None
        self.photsub = False
        self._get_template_candidates()

    def get_cal_info(self):
        '''checks for existence of calibration files and writes them if found'''

        calfile = 'cal_{}_PS1.dat'.format(self.targetname)
        if os.path.exists(os.path.join(self.calibration_dir, calfile)):
            self.calfile = calfile
            self.cal_source = 'PS1'
        elif os.path.exists(os.path.join(self.calibration_dir, calfile.replace('PS1', 'SDSS'))):
            self.calfile = calfile.replace('PS1', 'SDSS')
            self.cal_source = 'SDSS'
        elif os.path.exists(os.path.join(self.calibration_dir, calfile.replace('PS1', 'APASS'))):
            self.calfile = calfile.replace('PS1', 'APASS')
            self.cal_source = 'APASS'
        self.calfile_use = self.calfile.replace('.dat', '_use.dat')

    def cut_lc_points(self, lc_list):
        '''interactively cut points from each band in each lc file from the input list'''

        self.log.info('interactively cutting points from light curve files')

        for fl in lc_list:
            self.log.info('working on {}'.format(fl))
            p = LPPu.plotLC(lc_file = fl)
            p.plot_lc(icut = True, extensions = ['.ps', '.png'])

    def plot_lc(self, lc_list):
        '''plots each light curve from the input list'''

        for fl in lc_list:
            self.log.info('plotting {}'.format(fl))
            p = LPPu.plotLC(lc_file = fl)
            p.plot_lc(extensions = ['.ps', '.png'])

    def _ct2cf(self, color_term, use = False):
        '''return "calfit" filename associated with input color term'''

        base = self.calfile.split('.')[0]
        if color_term != 'Landolt':
            cal_nat_fit = base + '_{}_natural.fit'.format(color_term)
        else:
            cal_nat_fit = base + '_Landolt_standard.fit'
        if use is False:
            return cal_nat_fit
        else:
            return cal_nat_fit.replace('_{}_'.format(self.cal_source), '_{}_use_'.format(self.cal_source))

    def _im2inst(self, image_list, mode = 'progress'):
        '''create a series of Phot instances from input image list (also a series)'''

        # hide astropy warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', AstropyWarning)
            if mode != 'quiet':
                return image_list.progress_apply(Phot, radec = self.radec)
            else:
                return image_list.apply(Phot, radec = self.radec)

    def _lc_fname(self, cterm, pmethod, lc_type, sub = False):
        '''return light curve filename'''

        if self.lc_base is None:
            print('set lc_base first')
            return

        full_base = self.lc_base + cterm + '_' + pmethod
        lc_fname = full_base + self.lc_ext[lc_type]
        if sub is True:
            lc_fname = lc_fname.replace('.dat', '_sub.dat')

        return lc_fname

    def _get_template_candidates(self):
        '''wrap LPPu function to get template candidates'''

        self.log.info('searching for galaxy subtraction template images')

        # fall back on first obs date if don't know discovery date
        if self.disc_date_mjd is None:
            if self.first_obs is None:
                self.first_obs = LPPu.get_first_obs_date(self)
            dt = first_obs
        else:
            dt = self.disc_date_mjd

        result = LPPu.get_template_candidates(self.targetra, self.targetdec, dt, self.templates_dir)
        self.log.info(result)

    def _log_idl(self, idl_cmd, stdout, stderr):
        '''log info regarding external idl calls'''

        self.log.debug('output of IDL command: {}'.format(idl_cmd))
        self.log.debug('STDOUT----\n{}'.format(stdout))
        self.log.debug('STDERR----\n{}'.format(stderr))

# provide script functionality via
# python LPP.py name
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type = str, help = 'name of the object')
    parser.add_argument('-i', '--interactive', dest = 'interactive', action = 'store_const',
                        const = True, default = False, help = 'run in interactive mode')
    parser.add_argument('-ct', '--force-color-term', dest = 'force_color_term', type = str, 
                        default = False, help = 'force to use specified color term')
    parser.add_argument('-dd', '--disc-date-mjd', dest = 'disc_date_mjd', type = float,
                        default = None, help = 'mjd of discovery')
    args = parser.parse_args()

    pipeline = LPP(args.name, interactive = args.interactive, force_color_term = args.force_color_term)
    pipeline.disc_date_mjd = args.disc_date_mjd
    pipeline.run()


