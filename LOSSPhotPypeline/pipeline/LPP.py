# standard imports
import os
import glob
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
import itertools
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord, match_coordinates_sky
from astropy.visualization import ZScaleInterval
from astropy import units as u
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

    def __init__(self, targetname, interactive = True, parallel = True, cal_diff_tol = 0.05, force_color_term = False, max_display_phase = 120,
                 wdir = '.', cal_use_common_ref_stars = False, sep_tol = 8, pct_increment = 0.05, in_pct_floor = 0.8, autoloadsave = False):
        '''Instantiation instructions'''

        # basics from instantiation
        self.targetname = targetname.replace(' ', '')
        self.config_file = targetname + '.conf'
        self.interactive = interactive
        self.wdir = os.path.abspath(wdir) # working directory for running (particularly idl code)
        if (parallel is True) and (_parallel) is True:
            self.parallel = True
        else:
            self.parallel = False
        self.cal_diff_tol = cal_diff_tol # starting calibration difference tolerance
        self.abs_cal_tol = 0.2 # do not proceed with the pipeline if in non-interactive mode and cal tol exceeds this
        self.min_ref_num = 2 # minimum number of ref stars
        self.pct_increment = pct_increment # amount to increment percentage requirement down by if doing ref check
        self.in_pct_floor = in_pct_floor # minimum percentage of images ref stars must be in if doing ref check
        self.checks = ['filter', 'date'] # default checks to perform on image list
        self.phase_limits = (-60, 2*365) # phase bounds in days relative to disc. date to keep if "date" check performed
        self.cal_use_common_ref_stars = cal_use_common_ref_stars # override requirement that each image have all ref stars
        self.sep_tol = sep_tol # radius around target in arcseconds to exclude candidate reference stars from

        # log file
        self.logfile = self.targetname.replace(' ', '') + '.log'
        self.build_log()

        # sourced from configuration file
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
        self.mrIndex = pd.Index([]) # keep track of indices to remove manually
        self.run_success = False # track run success

        # calibration variables
        self.cal_source = 'auto'
        self.calfile = 'TBD'
        self.calfile_use = 'TBD'
        self.force_color_term = force_color_term
        self.calibration_dir = 'calibration'
        if not os.path.isdir(self.calibration_dir):
            os.makedirs(self.calibration_dir)
        self.radecfile = os.path.join(self.calibration_dir, self.targetname + '_radec.txt')
        self.radec = None
        self.cal_IDs = 'all'
        self.cal_arrays = None
        self.cal_force_clear = False
        self.max_display_phase = max_display_phase # num days to show rel to disc for interactive calibration

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
                       'standard': '_standard.dat',
                       'ul': '_natural_ul.dat'}

        # galaxy subtraction variables
        self.template_images = None
        self.templates_dir = 'templates'

        # data directories
        self.data_dir = os.path.dirname(self.refname)
        self.error_dir = self.data_dir + '_sim'

        # steps in standard reduction procedure
        self.current_step = 0
        self.steps = [self.load_images,
                      self.check_images,
                      self.find_ref_stars,
                      self.match_refcal_stars,
                      self.do_galaxy_subtraction_all_image,
                      self.do_photometry_all_image,
                      self.get_sky_all_image,
                      self.do_calibration,
                      self.get_zeromag_all_image,
                      self.get_limmag_all_image,
                      self.generate_lc,
                      self.write_summary]

        # save file
        self.savefile = self.targetname.replace(' ', '') + '.sav'
        if os.path.exists(self.savefile):
            if self.interactive:
                load = input('Load saved state from {}? ([y]/n) > '.format(self.savefile))
            else:
                load = 'n' # run fresh if in non-interactive mode
                if autoloadsave :
                        load = 'y' # run fresh if in non-interactive mode, unless this keyword is set
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
            print('cr --- cut points from specific raw light curve and regenerate subsequent light curves')
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
            elif (resp == 'c') or (resp == 'cr'):
                lc_file = input('enter light curve file (including relative path) to cut points from > ')
                regenerate = False
                if resp == 'cr':
                    regenerate = True
                self.cut_lc_points(lc_file, regenerate = True)
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

    def load(self, savefile = None, summary = True):
        '''re-initializes pipeline from saved state in file'''
        if savefile is None:
            savefile = self.savefile
        with open(savefile, 'rb') as f:
            vs = pkl.load(f)
        for v in vs.keys():
            s = 'self.{} = vs["{}"]'.format(v, v)
            exec(s)
        self.log.info('{} loaded'.format(savefile))
        if summary:
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
        self.phot_instances = self._im2inst(self.image_list) # radec is None if running in order

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

        # if there are none left, end pipeline
        if len(self.wIndex) == 0:
            self.log.warn('all images removed by checks --- cannot proceed')
            self.run_success = False
            self.current_step = self.steps.index(self.write_summary) - 1
            return

    def find_ref_stars(self):
        '''identify all suitable stars in ref image, compute ra & dec, write radecfile, store in instance'''

        # if radecfile already exists, no need to do it
        if os.path.exists(self.radecfile):
            self.log.info('radecfile already exists, loading only')
            self.radec = pd.read_csv(self.radecfile, delim_whitespace=True, skiprows = (0,1,3,4,5), names = ['RA','DEC'])
            # set radec in Phot instances
            for img in self.phot_instances.loc[self.wIndex]:
                img.radec = self.radec
            return
        if self.refname == '' :
            self.log.warn('refname has not been assigned, please do it first!')
            return

        # instantiate object to manage names
        ref = Phot(self.refname, calmethod = self.calmethod)

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
        imagera, imagedec = cs.all_pix2world(imagex, imagey, 0)

        # remove any identified "stars" that are too close to target
        coords = SkyCoord(imagera, imagedec, unit = (u.deg, u.deg))
        target_coords = SkyCoord(self.targetra, self.targetdec, unit = (u.deg, u.deg))
        offsets = coords.separation(target_coords).arcsecond
        imagera = imagera[offsets > self.sep_tol]
        imagedec = imagedec[offsets > self.sep_tol]

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

        # set radec in Phot instances
        for img in self.phot_instances.loc[self.wIndex]:
            img.radec = self.radec

    def match_refcal_stars(self):
        '''get calibration catalog, and match stars to ref stars -- only do if needed'''

        if os.path.exists(os.path.join(self.calibration_dir, self.calfile)) is False:

            # get calibration catalog
            catalog = LPPu.astroCatalog(self.targetname, self.targetra, self.targetdec, relative_path = self.calibration_dir)
            catalog.get_cal(method = self.cal_source)
            self.calfile = catalog.cal_filename
            self.cal_source = catalog.cal_source
            self.log.info('calibration data sourced')

        self.log.info('matching ref stars to catalog stars and selecting 40 brightest')
        self.get_cal_info()
        radec = SkyCoord(self.radec.loc[1:, 'RA'], self.radec.loc[1:, 'DEC'], unit = (u.deg, u.deg))
        cal_cat = pd.read_csv(os.path.join(self.calibration_dir, self.calfile), delim_whitespace = True)
        cal = SkyCoord(cal_cat.loc[:, 'ra'], cal_cat.loc[:, 'dec'], unit = (u.deg, u.deg))
        idx, d2d, d3d = match_coordinates_sky(cal, radec)
        cal_use = cal_cat.iloc[d2d.arcsecond < 5] # calibration stars that match within 5"
        cal_use.index = self.radec.loc[1:].iloc[idx[d2d.arcsecond < 5]].index - 1 # don't count sn and align indices with radecfile
        cal_use.insert(0, 'starID', cal_use.index)
        cal_use = cal_use.sort_values(by = 'r').drop_duplicates(subset = 'starID', keep = 'first')
        self.cal_use = cal_use.iloc[:40] # select top 40 brightest

        # write "use" files
        with open(os.path.join(self.calibration_dir, self.calfile_use), 'w') as outfile:
            outfile.write(self.cal_use.to_string(index = False))
        catalog = LPPu.astroCatalog(self.targetname, self.targetra, self.targetdec, relative_path = self.calibration_dir)
        catalog.cal_filename = self.calfile_use
        catalog.cal_source = self.cal_source
        catalog.to_natural()
        self.cal_arrays = catalog.get_cal_arrays(index_order = self.cal_use.index)

        # show ref stars (and cut if interactive mode)
        if self.interactive:
            self._display_refstars(icut = True)
        else:
            self._display_refstars()

    def do_galaxy_subtraction_all_image(self, subreg = 0.9):
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
        fn = lambda img: img.galaxy_subtract(ti, subreg = subreg)

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
            self.photsub = False

        self.log.info('galaxy subtraction done')

    def do_photometry_all_image(self, forcesky = False):
        '''performs photometry on all selected image files'''

        self.log.info('starting photometry (galsub: {})'.format(self.photsub))

        # set up for parallelization
        ps = self.photsub
        fn = lambda img: img.do_photometry(photsub = ps, forcesky = forcesky)

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

        if len(self.wIndex) == 0:
            self.log.warn('all images failed, cannot proceed')
            self.run_success = False
            self.current_step = self.steps.index(self.write_summary) - 1
            return

        self.log.info('photometry done')

    def get_sky_all_image(self):
        '''get and set sky value for every phot instance'''

        self.log.info('getting sky value for each image')
        self.phot_instances.loc[self.wIndex].progress_apply(lambda img: img.get_sky())

    def calibrate(self, final_pass = False):
        '''performs calibration on all images included in photlistfile, using outputs from do_photometry_all_image'''

        if not final_pass:
            self.log.info('performing calibration')
        else:
            self.log.info('doing final calibration')

        # reset trackers
        self.cfIndex = []
        self.csfIndex = []

        # calibration list
        cal_list = []

        # iterate through image list and execute calibration script on each
        for idx, img in tqdm(self.phot_instances.loc[self.wIndex].iteritems(), total = len(self.wIndex)):

            # set photsub mode appropriately
            if self.photsub is False:
                ps = False
            elif (self.photsub is True) and (idx in self.psfIndex):
                ps = False
            else:
                ps = True

            # do calibration
            phot = img.calibrate(self.cal_IDs, self.cal_arrays[img.color_term].loc[:, img.filter.upper()],
                                 self.cal_arrays[img.color_term].loc[:, 'E'+img.filter.upper()], sub = ps, write_dat = final_pass)
            phot.rename(columns = {self.calmethod: 'Mag_obs'}, inplace = True)

            # add comparison information
            phot.insert(0, 'Filter', img.filter.upper())
            phot.loc[self.cal_IDs, 'RA_cal'] = self.cal_arrays[img.color_term].loc[self.cal_IDs, 'RA']
            phot.loc[self.cal_IDs, 'DEC_cal'] = self.cal_arrays[img.color_term].loc[self.cal_IDs, 'DEC']
            phot.loc[self.cal_IDs, 'Mag_cal'] = self.cal_arrays[img.color_term].loc[self.cal_IDs, img.filter.upper()]
            phot.loc[self.cal_IDs, 'RA_diff'] = np.abs(phot.loc[self.cal_IDs, 'RA_obs'] - phot.loc[self.cal_IDs, 'RA_cal'])
            phot.loc[self.cal_IDs, 'DEC_diff'] = np.abs(phot.loc[self.cal_IDs, 'DEC_obs'] - phot.loc[self.cal_IDs, 'DEC_cal'])
            cal_list.append(phot.loc[self.cal_IDs, ['Filter', 'RA_diff', 'DEC_diff', 'Mag_obs', 'Mag_cal', 'ref_in', 'system']])

            # check for success if in final pass mode
            if final_pass:
                if (os.path.exists(img.psfdat) is False):
                    self.cfIndex.append(idx)
                if (self.photsub is True) and (os.path.exists(img.psfsubdat) is False):
                    self.csfIndex.append(idx)

        # organize calibrators and compute globabl metrics
        self.calibrators = pd.concat([df.loc[self.cal_IDs, :] for df in cal_list], keys = self.wIndex)
        self.calibrators['Mag_diff'] = self.calibrators['Mag_obs'] - self.calibrators['Mag_cal']

        # remove failures if in final pass mode
        if final_pass:
            self.cfIndex = pd.Index(self.cfIndex)
            self.csfIndex = pd.Index(self.csfIndex)
            self.log.warn('calibration failed on {} out of {} images'.format(len(self.cfIndex), len(self.wIndex)))
            self.wIndex = self.wIndex.drop(self.cfIndex) # processing based only on non-subtracted images
            if self.photsub is True:
                self.log.warn('calibration (sub) failed on {} out of {} images'.format(len(self.csfIndex), len(self.wIndex)))

        if len(self.wIndex) == 0:
            self.log.warn('all images failed, cannot proceed')
            self.run_success = False
            self.current_step = self.steps.index(self.write_summary) - 1
            return

    def do_calibration(self, use_filts = 'all', sig = 3, min_cut_diff = 0.5, quality_cuts = True):
        '''check calibration and make cuts as needed'''

        self.log.info('performing calibration')

        # get filters used
        self.filters = set(self.phot_instances.loc[self.wIndex].apply(lambda img: img.filter.upper()))
        if use_filts == 'all':
            use_filts = self.filters

        if self.cal_IDs == 'all':
            self.cal_IDs = self.cal_arrays['kait4'].index # choice of color term here is arbitrary

        # iterate until acceptable tolerance is reached
        accept_tol = False
        skip_calibrate = False
        iter_cnt = -1
        while not accept_tol:
            iter_cnt += 1

            # run calibration
            if not skip_calibrate:
                self.calibrate()
            skip_calibrate = False

            # find indices (img, cal_ID) where Mag_obs failed to measure
            locs = self.calibrators.loc[self.calibrators['Mag_obs'].isnull(), :].index
            # pct of succ meas as a function of img
            img_succ = (1 - locs.levels[0][locs.labels[0]].value_counts() / len(self.cal_IDs))
            # pct of succ meas as a function of cal_ID
            cal_succ = (1 - locs.levels[1][locs.labels[1]].value_counts() / len(self.wIndex))

            # run minimal quality cuts if requested --- these are the first and second iterations
            if (quality_cuts is True) and (iter_cnt < 2):
                # remove any cal IDs or images with a very low success rate
                ID_cut = cal_succ.index[cal_succ < 0.4]
                if (len(ID_cut) > 0) and (iter_cnt == 0):
                    self.cal_IDs = self.cal_IDs.drop(ID_cut)
                    self.log.info('cut ID(s): {} from minimal quality cut'.format(ID_cut))
                    continue
                elif iter_cnt == 0:
                    self.log.info('all IDs passed minimal quality cut')
                iter_cnt = 1
                img_cut = img_succ.index[img_succ < 0.4]
                if (len(img_cut) > 0) and (iter_cnt == 1):
                    self.manual_remove(img_cut)
                    self.log.info('cut image(s): {} from minimal quality cut'.format(img_cut))
                    continue
                elif iter_cnt == 1:
                    self.log.info('all images passed minimal quality cut')
                iter_cnt = 2
            elif iter_cnt < 2:
                iter_cnt = 2

            # cut to use common ref stars if requested --- these is the fourth iteration
            # iteration 3 is used to remove outlier images before applying this cut
            if (self.cal_use_common_ref_stars is True) and (iter_cnt == 3):
                self.log.info('finding common ref stars')
                accept = False
                cnt = 0
                while not accept:
                    current_pct = 1 - cnt * self.pct_increment
                    tmp = cal_succ[cal_succ >= current_pct]
                    if len(tmp) > self.min_ref_num:
                        self.log.info('{} ref stars are in at least {} pct of images, using these'.format(len(tmp), 100*current_pct))
                        accept = True
                    elif current_pct < self.in_pct_floor:
                        self.log.warn('reached minimum tolerance for pct image including ref stars, quitting')
                        self.run_succss = False
                        self.current_step = self.steps.index(self.write_summary) - 1
                        return
                    cnt += 1
                if len(tmp) < len(self.cal_IDs):
                    self.cal_IDs = tmp.index
                    continue

            # instantiate trackers
            cut_list = [] # store IDs that will be cut
            nan_list = [] # IDs of NaN to be cut immediately
            full_list = []
            bad_img_list = [] # indices of images that are <sig> outliers
            single_cut_idx = None
            tmp_max = self.cal_diff_tol
            df_list = []

            # group by filter and perform comparison
            for filt, group in self.calibrators.groupby('Filter', sort = False):
                # use specific filters if specified
                if filt not in use_filts:
                    continue
                # if clear is not the only filter, skip it in comparison unless forced to use
                if (len(self.filters) > 1) and ('CLEAR' in self.filters) and (filt == 'CLEAR') and (not self.cal_force_clear):
                    continue
                # compute metrics
                df = group.median(level = 1)
                df.loc[:, 'pct_im'] = group['Mag_obs'].notnull().sum(level=1) / len(group['Mag_obs'].groupby(level=0))
                df.loc[:, 'std_obs'] = group.std(level = 1).loc[:, 'Mag_obs']
                df = df.sort_index()
                df.loc[:, 'Diff'] = np.abs(df.loc[:, 'Mag_diff'])
                # identify possible exclusions
                cut_list.extend(list(df.index[df.loc[:, 'Diff'] > self.cal_diff_tol]))
                nan_list.extend(list(df.index[df.loc[:, 'Diff'].isnull()]))
                if len(nan_list) > 0:
                    break
                full_list = list(df.index) # ok to overwrite b/c same each time
                ## exclude outlier images by iterating through all cal IDs and finding images of <sig> outliers
                for id in self.cal_IDs:
                    selection = self.calibrators.loc[self.calibrators['Filter'] == filt, :].loc[(self.wIndex, id),['Mag_obs', 'system']]
                    for sys, grp in selection.groupby('system', sort = False):
                        grp = grp.loc[grp['Mag_obs'].notnull(), :]
                        mags = grp.loc[:, 'Mag_obs'].values
                        index = grp.index.levels[0][grp.index.labels[0]] # image indices
                        if len(mags) > 0:
                            bad_img_list.extend(index[np.abs(mags - mags.mean()) > np.max([min_cut_diff, sig * mags.std()])])

                if self.interactive:
                    print('\nFilter: {}'.format(filt))
                    print('*'*60)
                    rnd = pd.Series([2,4,4,3,3,3,3], index = ['pct_im', 'RA_diff', 'DEC_diff', 'Mag_cal', 'Mag_obs', 'std_obs', 'Mag_diff'])
                    print(df.loc[:, ['pct_im', 'RA_diff', 'DEC_diff', 'Mag_cal', 'Mag_obs', 'std_obs', 'Mag_diff']].round(rnd))
                else:
                    # find index and value of maximum diff
                    maxi = df.loc[:, 'Diff'].idxmax()
                    maxd = df.loc[maxi, 'Diff']
                    if maxd > tmp_max:
                        single_cut_idx = maxi
                        tmp_max = maxd
                df.insert(0, 'Filter', filt)
                df_list.append(df)
            cut_list = list(set(cut_list))
            bad_img_list = list(set(bad_img_list))

            # remove NaN
            if len(nan_list) > 0:
                self.log.info('cutting ID(s) {} for NaN'.format(', '.join([str(i) for i in nan_list])))
                self.cal_IDs = self.cal_IDs.drop(nan_list)
                continue

            # make cuts to refstars as needed
            if self.interactive:
                # show ref stars and calibrated light curves
                fig, ax = plt.subplots(1, 2, figsize = (12, 6))
                self._display_refstars(ax = ax[0], display = True)
                if self.photsub:
                    r = self.phot_instances.loc[self.wIndex].apply(lambda img: pd.Series([img.mjd, img.filter, img.phot_sub.loc[-1, self.calmethod],
                                                                   img.phot_sub.loc[-1, self.calmethod + '_err'], img.color_term]))
                else:
                    r = self.phot_instances.loc[self.wIndex].apply(lambda img: pd.Series([img.mjd, img.filter, img.phot.loc[-1, 'Mag_obs'],
                                                                   img.phot.loc[-1, self.calmethod + '_err'], img.color_term]))
                r.columns = ('mjd', 'filter', 'mag', 'emag', 'system')
                p = LPPu.plotLC(offset_scale = 2)
                for idx, ct in enumerate(set(r['system'])):
                    fs = 'full'
                    if 'nickel' in ct:
                        fs = 'none'
                    for filt in set(r['filter']):
                        selector = (r['filter'] == filt) & r['mag'].notnull() & (r['system'] == ct)
                        if (self.max_display_phase != 0) and (self.max_display_phase != 'all'):
                            selector = selector & (r['mjd'] - r['mjd'].min() < self.max_display_phase)
                        line, = ax[1].plot(r.loc[selector, 'mjd'], r.loc[selector, 'mag'] + p._offset(filt), c = p._color(filt),
                                           marker = ['o', 'D', 's', 'v', '^'][idx], linestyle = 'None', picker = 3,
                                           label = '{},{}'.format(filt, ct), fillstyle = fs)
                ax[1].invert_yaxis()
                ax[1].set_xticks(())
                ax[1].set_yticks(())
                x0, x1 = ax[1].get_xlim()
                y0, y1 = ax[1].get_ylim()
                ax[1].set_aspect(np.abs((x1-x0)/(y1-y0)))
                plt.tight_layout()
                def onpick(event):
                    ind = event.ind[0]
                    filt, sys = event.artist._label.split(',')
                    row = r.loc[(r['filter'] == filt) & (r['system'] == sys) & (r['mjd'] == event.artist._x[ind]), :]
                    id = row.index[0]
                    cal = self.phot_instances.loc[id].phot.loc[self.cal_IDs, 'Mag_obs']
                    print('\nClicked Point Information:')
                    print('\tImage ID: {}'.format(id))
                    print('\tImage Name: {}'.format(self.image_list.loc[id]))
                    print('\tMJD: {:.1f}'.format(row['mjd'].item()))
                    print('\tMag: {:.1f} pm {:.1f}'.format(row['mag'].item(), row['emag'].item()))
                    print('\tFilter: {}'.format(filt))
                    print('\tSystem: {}'.format(sys))
                    print('\tcal IDs used: {}/{}'.format(len(cal.loc[cal.notnull()]), len(cal)))
                    print('\tfailed cal IDs: {}'.format(', '.join([str(i) for i in sorted(cal.loc[cal.isnull()].index)])))
                    print('\nChoice >')
                cid = fig.canvas.mpl_connect('pick_event', lambda event: onpick(event))
                print('*'*60)
                nshow = np.min([len(cal_succ), len(img_succ), 10])
                if nshow > 0:
                    print('\nSuccess Rate Per (worst {})'.format(nshow))
                    print('{:<12} {:<12}'.format('cal ID', 'image'))
                    for c, i in itertools.zip_longest(cal_succ.iloc[:nshow].index, img_succ.iloc[:nshow].index):
                        print('{:<4} {:<7} {:<4} {:<7}'.format(c, round(cal_succ.loc[c], 3), i, round(img_succ.loc[i], 3)))
                # warn if any individual images have too few ref stars
                ref_counts = self.calibrators['Mag_obs'].notnull().sum(level = 0)
                if (ref_counts < self.min_ref_num).sum() > 0:
                    print('\nWarning - the following image(s) have below the minimum number of ref stars ({}):'.format(self.min_ref_num))
                    print(ref_counts.index[ref_counts < self.min_ref_num])
                if (ref_counts == self.min_ref_num).sum() > 0:
                    print('\nWarning - the following image(s) have the minimum number of ref stars ({}):'.format(self.min_ref_num))
                    print(ref_counts.index[ref_counts == self.min_ref_num])
                    print('\nDo not cut the following ID(s) to avoid falling below the minimum:')
                    idx_selector = (ref_counts.index[ref_counts == self.min_ref_num], self.cal_IDs)
                    num_affected = self.calibrators.loc[idx_selector, 'Mag_obs'].notnull().sum(level=1)
                    print(num_affected.index[num_affected > 0].sort_values())
                if len(bad_img_list) > 0:
                    print('\nWarning - the following image(s) are outliers:')
                    print(bad_img_list)
                print('\nAt tolerance {}, {} ID(s) (out of {}) will be cut'.format(self.cal_diff_tol, len(cut_list), len(full_list)))
                print(sorted(cut_list))
                print('\nSelect an option below (or click on light curve points to get info):')
                print('\tAccept cuts with tolerance of {} mag ([y])'.format(self.cal_diff_tol))
                print('\tAdjust tolerance [enter float between 0 and 1]')
                print('\tCut calibration star(s) by ID(s) [comma separated list of IDs to cut]')
                print('\tDisplay image ["d" followed by index (e.g. d162)]')
                print('\tCut image(s) ["c" followed by comma separated indexes (e.g. c162,163)]')
                print('\tView measured mags for specific cal star ["<passband>" followed by cal ID (e.g. B5)]')
                response = input('\nChoice > '.format(self.cal_diff_tol))
                fig.canvas.mpl_disconnect(cid)
                plt.ioff()
                plt.close()
                if (response == '') or ('y' in response.lower()):
                    self.cal_IDs = self.cal_IDs.drop(cut_list)
                    accept_tol = True
                elif '.' in response:
                    self.cal_diff_tol = float(response)
                    skip_calibrate = True
                elif response.lower()[0] == 'd':
                    self.compare_image2ref(int(response[1:]))
                    skip_calibrate = True
                elif (response.lower()[0] == 'c') and (response.lower()[1] != 'l'):
                    self.manual_remove([int(i) for i in response[1:].split(',')])
                elif response[0] in self.filters:
                    self._display_obs_cal_mags(response[0], int(response[1:]))
                    skip_calibrate = True
                elif response[:5].lower() == 'clear':
                    self._display_obs_cal_mags(response[:5], int(response[5:]))
                else:
                    self.cal_IDs = self.cal_IDs.drop([int(i) for i in response.split(',')])
            elif (len(bad_img_list) > 0):
                self.log.info('removing {} outlier image(s): {}'.format(len(bad_img_list), bad_img_list))
                self.manual_remove(bad_img_list)
            elif single_cut_idx is None:
                accept_tol = True
            elif len(full_list) > self.min_ref_num:
                self.log.info('cutting ID {} for exceeding tolerance and re-running calibration'.format(single_cut_idx))
                self.cal_IDs = self.cal_IDs.drop([single_cut_idx])
            elif self.cal_diff_tol <= self.abs_cal_tol:
                self.log.info('increasing tolerance to {} and re-running calibration'.format(self.cal_diff_tol))
                self.cal_diff_tol += 0.05
            else:
                self.log.warn('calibration tolerance exceeds {}, cannot proceed'.format(self.abs_cal_tol))
                self.run_success = False
                self.current_step = self.steps.index(self.write_summary) - 1
                return

        with open(os.path.join(self.calibration_dir, 'final_ref_stars.dat'), 'w') as outfile:
            outfile.write(pd.concat([df.loc[self.cal_IDs, :] for df in df_list], sort = False).to_string())

        # make final pass on calibration to track failures and write .dat files
        self.calibrate(final_pass = True)

        # write final "use" files
        with open(os.path.join(self.calibration_dir, self.calfile_use), 'w') as outfile:
            outfile.write(self.cal_use.loc[self.cal_IDs, :].to_string(index = False))
        catalog = LPPu.astroCatalog(self.targetname, self.targetra, self.targetdec, relative_path = self.calibration_dir)
        catalog.cal_filename = self.calfile_use
        catalog.cal_source = self.cal_source
        catalog.to_natural()

        # show new ref stars
        plt.ioff()
        self._display_refstars()

    def get_zeromag_all_image(self):
        '''get and set zeromag for every phot instance'''

        self.log.info('getting zeromag for each image')
        self.phot_instances.loc[self.wIndex].progress_apply(lambda img: img.get_zeromag())

    def get_limmag_all_image(self):
        '''get and set limiting mag for every phot instance'''

        self.log.info('getting limiting mag for each image')
        self.phot_instances.loc[self.wIndex].progress_apply(lambda img: img.calc_limmag())

    def generate_raw_lcs(self, color_term, photsub_mode = False):
        '''builds raw light curve files from calibrated results'''

        # light curve containers
        columns = (';; MJD','etburst', 'mag', '-emag', '+emag', 'limmag', 'filter', 'imagename')
        lc = {name: [] for name in columns}
        lcs = {m: copy.deepcopy(lc) for m in self.photmethod}

        # limiting mag containers
        lm = {name: [] for name in columns}
        lms = {m: copy.deepcopy(lm) for m in self.photmethod}

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
                    self.noIndex.append(idx)
                else:
                    self.nosIndex.append(idx)

            # setup columns for each raw file
            for m in self.photmethod:
                if 1 not in d['ID'].values:
                    continue # skip these ones
                mag = d[d['ID'] == 1][m + '_mag'].item()
                err = d[d['ID'] == 1][m + '_err'].item()
                if np.isnan(mag):
                    record = lms[m]
                else:
                    record = lcs[m]
                record['mag'].append(round(mag,5))
                record['-emag'].append(round(mag - err,5))
                record['+emag'].append(round(mag + err,5))
                record[';; MJD'].append(round(img.mjd, 6))
                record['etburst'].append(round(img.exptime / (60 * 24), 5)) # exposure time in days
                record['filter'].append(img.filter.upper())
                record['imagename'].append(img.cimg)
                record['limmag'].append(round(img.limmag, 5))

        # write raw lc files
        for m in self.photmethod:
            lc_raw_name = self._lc_fname(color_term, m, 'raw', sub = photsub_mode)
            lc_raw = pd.DataFrame(lcs[m])
            lc_raw.to_csv(lc_raw_name, sep = '\t', columns = columns, index = False, na_rep = 'NaN')
            lm_raw_name = self._lc_fname(color_term, m, 'ul', sub = photsub_mode)
            lm_raw = pd.DataFrame(lms[m])
            lm_raw.to_csv(lm_raw_name, sep = '\t', columns = columns, index = False, na_rep = 'NaN')
            p = LPPu.plotLC(lc_file = lc_raw_name, lm_file = lm_raw_name, name = self.targetname, photmethod = m)
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
        if (', not doing group' in stdout) or (os.path.exists(outfile) is False):
            return False
        else:
            return True

    def generate_final_lc(self, color_term, infile, outfile):
        '''wraps IDL routine to convert from natural system'''

        idl_cmd = '''idl -e "lpp_invert_natural_stand_objonly, '{}', '{}', OUTFILE='{}', /OUTPUT"'''.format(infile, color_term, outfile)
        stdout, stderr = LPPu.idl(idl_cmd)
        self._log_idl(idl_cmd, stdout, stderr)
        if not os.path.exists(outfile):
            return False
        else:
            return True

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
        grp_result = self.generate_group_lc(binfile, groupfile)
        if grp_result is False:
            self.log.warn('no groupfile generated, skipping')
            return False, False
        std_result = self.generate_final_lc(ct, groupfile, lc)
        if std_result is False:
            self.log.warn('no standard lc generated, skipping')
            return True, False

        # plot
        p = LPPu.plotLC(lc_file = lc, name = self.targetname, photmethod = m)
        p.plot_lc(extensions = ['.ps', '.png'])

        return True, True

    def get_color_term_used(self):
        '''get dictionary counting use of each color term'''

        ct = self.phot_instances.loc[self.wIndex].apply(lambda img: img.color_term)
        self.color_terms_used = dict(ct.value_counts())

    def generate_lc(self, sub = False):
        '''performs all functions to transform image photometry into calibrated light curve of target'''

        self.log.info('generating and plotting light curves (sub mode: {})'.format(sub))

        # set up file system
        if not os.path.isdir(self.lc_dir):
            os.makedirs(self.lc_dir)

        self.get_color_term_used()

        # generate raw light curves
        self.log.info('generating raw light curves for the following color terms: {}'.format(', '.join(self.color_terms_used.keys())))
        for ct in tqdm(self.color_terms_used.keys()):
            self.generate_raw_lcs(ct, photsub_mode = sub)

        # generate intermediate and final light curves
        self.log.info('generating "standard" light curves')
        for m in tqdm(self.photmethod):
            all_nat = []
            all_std = []
            for ct in self.color_terms_used.keys():
                group_succ, standard_succ = self.raw2standard_lc(self._lc_fname(ct, m, 'raw', sub = sub))
                # only add group and standard if group has been updated
                if group_succ is True:
                    all_nat.append((ct, self._lc_fname(ct, m, 'group', sub = sub)))
                if standard_succ is True:
                    all_std.append(self._lc_fname(ct, m, 'standard', sub = sub))
            # make "all" light curves
            lc_nat = self._lc_fname('all', m, 'group', sub = sub)
            concat_list = []
            for row in all_nat:
                tmp = pd.read_csv(row[1], delim_whitespace = True)
                tmp.insert(3, 'SYSTEM', row[0])
                concat_list.append(tmp)
            if len(concat_list) > 0:
                pd.concat(concat_list, sort = False).to_csv(lc_nat, sep = '\t', na_rep = 'NaN', index = False, float_format = '%6.3f')
                p = LPPu.plotLC(lc_file = lc_nat, name = self.targetname, photmethod = m)
                p.plot_lc(extensions = ['.ps', '.png'])
            lc = self._lc_fname('all', m, 'standard', sub = sub)
            concat_list = []
            for fl in all_std:
                concat_list.append(pd.read_csv(fl, delim_whitespace = True))
            if len(concat_list) > 0:
                pd.concat(concat_list, sort = False).to_csv(lc, sep = '\t', na_rep = 'NaN', index = False, float_format = '%6.3f')
                p = LPPu.plotLC(lc_file = lc, name = self.targetname, photmethod = m)
                p.plot_lc(extensions = ['.ps', '.png'])

        self.log.info('done with light curves')
        self.run_success = True

        # use recursion to handle sub if needed
        if (self.photsub is True) and (sub is False):
            self.generate_lc(sub = True)

    def get_errors(self, method = 'sn6', kpix_rad = 20, skip_photsub = False, photsub = 'auto', ps = 0.7965,
                   host_ra = None, host_dec = None, rseed = None):
        '''inject artificial stars of same mag as SN at each epoch and compute mags'''

        self.log.info('doing artificial star simulation to determine errors')

        # set seed
        if rseed is not None:
            np.random.seed(rseed)

        # make directory for new generated data
        if not os.path.exists(self.error_dir):
            os.makedirs(self.error_dir)

        if (photsub == 'auto') or (type(photsub) != type(True)):
            photsub = self.photsub

        # hard coded
        n_stars = 30

        # compute coords of n_stars around host
        def handle_img(img, ret_xy = False, method = method):
            cs = WCS(header = img.header)

            # get pix coords of sn
            sn_x, sn_y = cs.all_world2pix(self.targetra, self.targetdec, 0)

            # select appropriate method
            if method == 'snhost':
                # ring of radius equal to distance between sn and nucleus
                n_stars = 10
                host_x, host_y = cs.all_world2pix(host_ra, host_dec, 0)
                theta_sn = np.arctan2(sn_y - host_y, sn_x - host_x) # angle relative to hose
                # coordinates of artificial stars
                dtheta = np.linspace(2*np.pi/n_stars, 2*np.pi - 2*np.pi/n_stars, n_stars)
                x = host_x + np.sqrt((sn_y - host_y)**2 + (sn_x - host_x)**2) * np.cos(theta_sn + dtheta)
                y = host_y + np.sqrt((sn_y - host_y)**2 + (sn_x - host_x)**2) * np.sin(theta_sn + dtheta)
            elif method == 'squares':
                # square distribution as discussed w/ zwk and TdG
                x_comp = np.cos(np.linspace(np.pi/4, 2*np.pi - np.pi / 4, 4))
                x = sn_x + (kpix_rad * ps / img.pixscale) * np.concatenate([x_comp, 2 * x_comp, 2 * np.cos(np.pi/4) * np.array([1,0,-1,0])])
                y_comp = np.sin(np.linspace(np.pi/4, 2*np.pi - np.pi / 4, 4))
                y = sn_y + (kpix_rad * ps / img.pixscale) * np.concatenate([y_comp, 2 * y_comp, 2 * np.sin(np.pi/4) * np.array([0,1,0,-1])])
                n_stars = len(x)
            else:
                # preferred method of concentric hexagons with radius increments of 20 KAIT pixels
                dtheta = np.linspace(0, 2*np.pi, 7)[:-1]
                x = sn_x + (kpix_rad * ps / img.pixscale) * np.concatenate((np.cos(dtheta), 2 * np.cos(dtheta + np.pi/6), 3 * np.cos(dtheta),
                                                                      4 * np.cos(dtheta + np.pi/6), 5 * np.cos(dtheta)))
                y = sn_y + (kpix_rad * ps / img.pixscale) * np.concatenate((np.sin(dtheta), 2 * np.sin(dtheta + np.pi/6), 3 * np.sin(dtheta),
                                                                      4 * np.sin(dtheta + np.pi/6), 5 * np.sin(dtheta)))
                n_stars = len(x)

            # if just want pixel coords, return them along with WCS instance
            if ret_xy is True:
                return cs, x, y

            # get magnitude of sn at this epoch
            mag = np.nan
            try:
                if photsub is False:
                    mag = img.phot_raw.loc[-1, self.calmethod]
                    emag = img.phot_raw.loc[-1, self.calmethod + '_err']
                else:
                    mag = img.phot_sub_raw.loc[-1, self.calmethod]
                    emag = img.phot_sub_raw.loc[-1, self.calmethod + '_err']
            except AttributeError:
                pass
            if (np.isnan(mag)) or (np.isinf(mag)):
                return False, None

            # if random seed given, injected mags drawn from a gaussian of width set by uncertainty
            if rseed is None:
                inj_mags = [mag]*n_stars
            else:
                inj_mags = np.random.normal(mag, emag, n_stars).tolist()

            assert n_stars == len(x)

            # IDL call leads to new images in new directory
            idl_cmd = '''idl -e "lpp_sim_fake_star, '{}', {}, {}, {}, OUTFILE='{}', PSFFITARRFILE='{}', /USENATURALMAG"'''.format(img.cimg, 
                      x.tolist(), y.tolist(), inj_mags, os.path.join(self.error_dir, os.path.basename(img.cimg)), img.psffitarr)
            stdout, stderr = LPPu.idl(idl_cmd)
            self._log_idl(idl_cmd, stdout, stderr)

            # do checks on success then return
            if os.path.exists(os.path.join(self.error_dir, os.path.basename(img.cimg))):
                return True, inj_mags
            else:
                return False, None

        self.log.info('creating images with artificial stars')
        succ = []
        mags = []
        for img in tqdm(self.phot_instances.loc[self.wIndex].tolist()):
            s, m = handle_img(img)
            succ.append(s)
            if m is not None:
                mags.append(m)
        # drop images with no mag
        self.wIndex = self.wIndex[pd.Series(succ)]

        # instantiate pipeline instance and inherit many parent attributes
        sn = LPP(self.targetname, interactive = False, parallel = self.parallel, cal_diff_tol = self.cal_diff_tol, force_color_term = self.force_color_term,
                 wdir = self.wdir, cal_use_common_ref_stars = self.cal_use_common_ref_stars, autoloadsave = False, sep_tol = self.sep_tol)
        vs = vars(self).copy()
        vs.pop('steps')
        vs.pop('log')
        vs.pop('phot_instances')
        for v in vs.keys():
            s = 'sn.{} = vs["{}"]'.format(v, v)
            exec(s)
        sn.interactive = False

        self.log.info('running pipeline steps on images with artificial stars')
        # change image paths and load instances
        sn.image_list = sn.image_list.apply(lambda fl: os.path.join(self.error_dir, os.path.basename(fl)))
        sn.phot_instances = sn._im2inst(sn.image_list.loc[sn.wIndex], mode = 'quiet')

        # include artificial stars in radec
        cs, x, y = handle_img(Phot(self.refname, calmethod = self.calmethod), ret_xy = True)
        fake_ra, fake_dec = cs.all_pix2world(x, y, 0)
        for img in sn.phot_instances.loc[sn.wIndex]:
            img.radec = self.radec.append(pd.DataFrame({'RA': fake_ra, 'DEC': fake_dec}), ignore_index = True)

        # run needed pipeline steps on those new images
        if (skip_photsub is False) and (photsub is True):
            sn.do_galaxy_subtraction_all_image()
        sn.do_photometry_all_image()
        sn.get_sky_all_image()
        sn.calibrate(final_pass = True) # don't really care about calibration, but need to do to read results

        # gather, organize and write
        sn.lc_dir = self.lc_dir + '_sim'
        sn.lc_base = os.path.join(sn.lc_dir, 'lightcurve_{}_'.format(self.targetname))
        if not os.path.exists(sn.lc_dir):
            os.makedirs(sn.lc_dir)
        def get_res(idx, ps):
            img = sn.phot_instances.loc[idx]
            if ps is False:
                #tmp = img.phot.iloc[-n_stars:].loc[:, 'Mag_obs']
                tmp = img.phot_raw.iloc[-n_stars:].loc[:, sn.calmethod]
            else:
                #tmp = img.phot_sub.iloc[-n_stars:].loc[:, sn.calmethod]
                tmp = img.phot_sub_raw.iloc[-n_stars:].loc[:, sn.calmethod]
            self.phot_instances.loc[idx].sim_err = tmp.std()
            return tmp
        res = []
        for idx in sn.wIndex:
            res.append(get_res(idx, photsub))
        res = pd.DataFrame(res, index = sn.wIndex)
        res.columns = sn.phot_instances.loc[sn.wIndex[0]].phot.index[-n_stars:]

        # put mags into DataFrame
        mags = pd.DataFrame(mags, index = self.wIndex)
        mags.columns = sn.phot_instances.loc[sn.wIndex[0]].phot.index[-n_stars:]

        # write results
        with open(os.path.join(sn.lc_dir, 'sim_{}_injmags.dat'.format(sn.calmethod)), 'w') as f:
            f.write(mags.to_string())
        with open(os.path.join(sn.lc_dir, 'sim_{}_recmags.dat'.format(sn.calmethod)), 'w') as f:
            f.write(res.to_string())

        # write updated errors to lc
        self.write_sim_lc(sn = sn, mags = mags, res = res, photsub = photsub)

        # save image with inj stars labeled
        sn._display_refstars(x = x, y = y, labels = res.columns, save_fig = os.path.join(sn.lc_dir, 'inj_stars.png'))

        sn.savefile = sn.savefile.replace('.sav', '_sim.sav')
        sn.save()
        self.save()

    def write_sim_lc(self, sn = None, mags = None, res = None, photsub = 'auto', drop_inj = []):
        '''write sim errs to light curves'''

        if (photsub == 'auto') or (type(photsub) != type(True)):
            photsub = self.photsub

        # instantiate if needed
        if sn is None:
            sn = LPP(self.targetname, interactive = False)
            sn.savefile = sn.savefile.replace('.sav', '_sim.sav')
            sn.load()

        # read mags and sim results if needed
        if mags is None:
            mags = pd.read_csv(os.path.join(sn.lc_dir, 'sim_{}_injmags.dat'.format(sn.calmethod)), delim_whitespace = True, index_col = 0)
            mags.columns = mags.columns.astype('int')
        if res is None:
            res = pd.read_csv(os.path.join(sn.lc_dir, 'sim_{}_recmags.dat'.format(sn.calmethod)), delim_whitespace = True, index_col = 0)
            res.columns = res.columns.astype('int')

        # drop any specied injected stars
        mags = mags.drop(drop_inj, axis = 1)
        res = res.drop(drop_inj, axis = 1)

        # compute result metrics
        residuals = mags.loc[sn.wIndex] - res.loc[sn.wIndex]
        r = pd.concat([sn.image_list.loc[sn.wIndex], res.mean(axis = 1), res.median(axis = 1), res.std(axis = 1), residuals.mean(axis = 1)], axis = 1)
        r.columns = ('imagename', 'sim_mean_mag', 'sim_med_mag', 'sim_std_mag', 'mean_residual')
        with open(os.path.join(sn.lc_dir, 'sim_{}_results.dat'.format(sn.calmethod)), 'w') as f:
            f.write(r.to_string(index = False))
        with open(os.path.join(sn.lc_dir, 'sim_{}_summary.dat'.format(sn.calmethod)), 'w') as f:
            f.write(r.describe().round(3).to_string())
        with open(os.path.join(sn.lc_dir, 'sim_{}_rec_mean_mags.dat'.format(sn.calmethod)), 'w') as f:
            f.write(res.mean(axis = 0).round(3).to_string())
        r['imagename'] = r['imagename'].str.replace(self.error_dir, self.data_dir)

        # do all light curves (with full uncertainty as quadrature sum of three sources)
        all_nat = []
        all_std = []
        columns = (';; MJD', 'etburst', 'mag', '-emag', '+emag', 'limmag', 'filter', 'imagename')
        ps_choice = photsub
        self.log.info('updating LC errors')
        for ct in tqdm(self.color_terms_used.keys()):
            # generate raw light curves
            lc = pd.read_csv(self._lc_fname(ct, sn.calmethod, 'raw', sub = ps_choice), delim_whitespace = True, comment = ';', names = columns)
            tmp = pd.merge(lc, r, on = 'imagename', how = 'left')
            orig_stat_err = (tmp['+emag'] - tmp['-emag'])/2
            new_err = np.sqrt(orig_stat_err**2 + tmp['sim_std_mag']**2)
            tmp['-emag'] = round(tmp['mag'] - new_err, 5)
            tmp['+emag'] = round(tmp['mag'] + new_err, 5)
            lc_raw_name = sn._lc_fname(ct, sn.calmethod, 'raw', sub = ps_choice)
            tmp.drop(['sim_mean_mag', 'sim_med_mag', 'sim_std_mag', 'mean_residual'], axis = 'columns').to_csv(lc_raw_name, sep = '\t', columns = columns,
                                                                                                          index = False, na_rep = 'NaN')
            p = LPPu.plotLC(lc_file = lc_raw_name, name = self.targetname, photmethod = self.calmethod)
            p.plot_lc(extensions = ['.ps', '.png'])

            # generate remaining light curves
            group_succ, standard_succ = self.raw2standard_lc(lc_raw_name)
            if group_succ is True:
                all_nat.append((ct, sn._lc_fname(ct, sn.calmethod, 'group', sub = ps_choice)))
            if standard_succ is True:
                all_std.append(sn._lc_fname(ct, sn.calmethod, 'standard', sub = ps_choice))
        # make "all" light curves
        lc_nat = sn._lc_fname('all', sn.calmethod, 'group', sub = ps_choice)
        concat_list = []
        for row in all_nat:
            tmp = pd.read_csv(row[1], delim_whitespace = True)
            tmp.insert(3, 'SYSTEM', row[0])
            concat_list.append(tmp)
        if len(concat_list) > 0:
            pd.concat(concat_list, sort = False).to_csv(lc_nat, sep = '\t', na_rep = 'NaN', index = False, float_format = '%6.3f')
            p = LPPu.plotLC(lc_file = lc_nat, name = self.targetname, photmethod = self.calmethod)
            p.plot_lc(extensions = ['.ps', '.png'])
        lc = sn._lc_fname('all', self.calmethod, 'standard', sub = ps_choice)
        concat_list = []
        for fl in all_std:
            concat_list.append(pd.read_csv(fl, delim_whitespace = True))
        if len(concat_list) > 0:
            pd.concat(concat_list, sort = False).to_csv(lc, sep = '\t', na_rep = 'NaN', index = False, float_format = '%6.3f')
            p = LPPu.plotLC(lc_file = lc, name = self.targetname, photmethod = self.calmethod)
            p.plot_lc(extensions = ['.ps', '.png'])

    def write_summary(self):
        '''write summary file'''

        # get filters used
        self.filters = set(self.phot_instances.loc[self.wIndex].apply(lambda img: img.filter.upper()))
        ctu = self.color_terms_used
        if ctu is not None:
            ctu = ', '.join(ctu.keys())
        stars = self.cal_IDs
        if stars != 'all':
            stars = ', '.join(self.cal_IDs.astype(str))

        self.summary_file = self.targetname + '.summary'
        with open(self.summary_file, 'w') as f:
            f.write('{:<25}{}\n'.format('targetname', self.targetname))
            f.write('{:<25}{}\n'.format('photsub', self.photsub))
            f.write('{:<25}{}\n'.format('filters', ', '.join(self.filters)))
            f.write('{:<25}{}\n'.format('apertures', ', '.join(self.photmethod)))
            f.write('{:<25}{}\n'.format('calmethod', self.calmethod))
            f.write('{:<25}{}\n'.format('color_terms', ctu))
            f.write('{:<25}{}\n'.format('num images', len(self.phot_instances)))
            f.write('{:<25}{}\n'.format('num failures', len(self.aIndex) - len(self.wIndex)))
            f.write('{:<25}{}\n'.format('num non-sup. filt.', len(self.bfIndex)))
            f.write('{:<25}{}\n'.format('num excl. by date', len(self.bdIndex)))
            f.write('{:<25}{}\n'.format('num phot failures', len(self.pfIndex)))
            f.write('{:<25}{}\n'.format('num cal failures', len(self.cfIndex)))
            f.write('{:<25}{}\n'.format('num no obj', len(self.noIndex)))
            f.write('{:<25}{}\n'.format('num manually removed', len(self.mrIndex)))
            f.write('{:<25}{}\n'.format('cal source', self.cal_source))
            f.write('{:<25}{}\n'.format('cal stars', stars))
            f.write('{:<25}{}\n'.format('cal tolerance', round(self.cal_diff_tol, 2)))
            f.write('{:<25}{}\n'.format('run successful', self.run_success))

        self.log.info('pipeline complete, summary file written')
        self.save()

    def get_host_photometry(self, tel = 'nickel'):
        '''do photometry of the host galaxy'''

        # instantiate pipeline instance and inherit many parent attributes
        sn = LPP(self.targetname, interactive = False, parallel = False, cal_diff_tol = self.cal_diff_tol, force_color_term = self.force_color_term,
                 wdir = self.wdir, cal_use_common_ref_stars = self.cal_use_common_ref_stars, autoloadsave = False, sep_tol = self.sep_tol)

        # setup
        sn.radec = self.radec
        sn.image_list = pd.Series([self.template_images['{}_{}'.format(filt, tel)] for filt in 'B V R I'.split(' ')])
        sn.phot_instances = sn._im2inst(sn.image_list, mode = 'quiet')
        sn.wIndex = sn.image_list.index
        sn.cal_arrays = self.cal_arrays
        sn.cal_IDs = self.cal_IDs

        # do photometry
        sn.photsub = False
        sn.do_photometry_all_image(forcesky = True)
        sn.get_sky_all_image()
        sn.calibrate(final_pass = True)
        sn.get_zeromag_all_image()
        sn.get_limmag_all_image()

        # set all images to have the same epoch
        for img in sn.phot_instances.loc[sn.wIndex]:
            img.mjd = 0

        sn.lc_dir = 'host_photometry'
        sn.lc_base = os.path.join(sn.lc_dir, 'lightcurve_{}_host_'.format(sn.targetname))
        sn.lc_ext = {'raw': '_natural_raw.dat',
                       'bin': '_natural_bin.dat',
                       'group': '_natural_group.dat',
                       'standard': '_standard.dat',
                       'ul': '_natural_ul.dat'}
        sn.generate_lc()

    ###################################################################################################
    #          Utility Methods
    ###################################################################################################

    def manual_remove(self, id, save_img = True):
        '''manually remove an index (or list of indices) from consideration'''

        if type(id) is int:
            id = [id]
        id = pd.Index(id)
        self.mrIndex = self.mrIndex.append(id)
        self.wIndex = self.wIndex.drop(id)
        if save_img:
            for img_id in id:
                self._display_refstars(imname = self.image_list.loc[img_id], imidx = img_id)

    def process_new_images(self, new_image_file = None, new_image_list = []):
        '''processes images obtained after initial processing'''

        self.log.info('processing new images')

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

        # only proceed if any images remain
        if len(new_image_list) == 0:
            self.log.warn('all images in new image list have already been processed, exiting')
            return

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
            self.calibrate(final_pass = True)
            self.get_zeromag_all_image()
            self.get_limmag_all_image()
            self.current_step = self.steps.index(self.generate_lc)

        # run program after calibration has been completed (on all images)
        self.aIndex = self.aIndex.append(self.wIndex)
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
            templates = glob.glob('{}/*c.fit'.format(self.templates_dir))
            if len(templates) == 0:
                msg = 'no templates available'
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
                    if not os.path.exists(self.template_images['{}_kait'.format(filt)]):
                        succ = False
                        msg = 'rebinning of templates from nickel to kait failed, cannot do photsub'
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

    def cut_lc_points(self, lc_file, regenerate = False):
        '''interactively cut points from each band in input lc file'''

        if ('_all_' in lc_file) and ('_raw' in lc_file):
            self.cut_raw_all_lc_points(lc_file)
            return

        self.log.info('interactively cutting points from light curve file')

        self.log.info('working on {}'.format(lc_file))
        p = LPPu.plotLC(lc_file = lc_file)
        cut_images = p.plot_lc(icut = True)
        if cut_images is not None:
            self.manual_remove(self.aIndex[self.image_list.isin(cut_images)])
        del p
        p = LPPu.plotLC(lc_file = lc_file)
        p.plot_lc(extensions = ['.ps', '.png'])

        if regenerate is True:
            return self.raw2standard_lc(lc_file)

    def cut_raw_all_lc_points(self, infile):
        '''given "all" raw filename (need not exist), do cutting on relevant raw files and regenerate "all" files'''

        # assign convenience variables
        tmp = infile.split('_')
        m = tmp[tmp.index('natural') - 1] # get phot aperture
        groupfile = infile.replace('raw', 'group')#.replace('.dat', '_cut.dat')
        lc = groupfile.replace('natural_group', 'standard')

        all_nat = []
        all_std = []
        for ct in self.color_terms.keys():
            raw = infile.replace('all', ct)
            if os.path.exists(raw):
                group_succ, std_succ = self.cut_lc_points(raw, regenerate = True)
                if group_succ:
                    all_nat.append((ct, groupfile.replace('all', ct)))
                if std_succ:
                    all_std.append(lc.replace('all', ct))
        concat_list = []
        for row in all_nat:
            tmp = pd.read_csv(row[1], delim_whitespace = True)
            tmp.insert(3, 'SYSTEM', row[0])
            concat_list.append(tmp)
        if len(concat_list) > 0:
            pd.concat(concat_list, sort = False).to_csv(groupfile, sep = '\t', na_rep = 'NaN', index = False, float_format = '%6.3f')
            p = LPPu.plotLC(lc_file = groupfile, name = self.targetname, photmethod = m)
            p.plot_lc(extensions = ['.ps', '.png'])
        concat_list = []
        for fl in all_std:
            if os.path.exists(fl):
                concat_list.append(pd.read_csv(fl, delim_whitespace = True))
        if len(concat_list) > 0:
            pd.concat(concat_list, sort = False).to_csv(lc, sep = '\t', na_rep = 'NaN', index = False, float_format = '%6.3f')
            p = LPPu.plotLC(lc_file = lc, name = self.targetname, photmethod = m)
            p.plot_lc(extensions = ['.ps', '.png'])

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
                return image_list.progress_apply(Phot, radec = self.radec, wdir = self.wdir, calmethod = self.calmethod)
            else:
                return image_list.apply(Phot, radec = self.radec, wdir = self.wdir, calmethod = self.calmethod)

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
            dt = self.first_obs
        else:
            dt = self.disc_date_mjd

        result = LPPu.get_template_candidates(self.targetra, self.targetdec, dt, self.templates_dir)
        self.log.info(result)

    def _reset_cal(self, reusecal_IDs = False):
        '''resets calibration to initial state, makes copy to revert'''
        self.cal_IDs_bak = self.cal_IDs.copy()
        self.mrIndex_bak = self.mrIndex.copy()
        self.wIndex_bak = self.wIndex.copy()
        if not reusecal_IDs:
            self.cal_IDs = 'all'
        self.wIndex = self.wIndex.append(self.mrIndex)
        self.mrIndex = pd.Index([])

    def _revert_cal(self):
       '''undoes effects of _reset_cal'''
       self.cal_IDs = self.cal_IDs_bak.copy()
       self.wIndex = self.wIndex_bak.copy()
       self.mrIndex = self.mrIndex_bak.copy()

    def _log_idl(self, idl_cmd, stdout, stderr):
        '''log info regarding external idl calls'''

        self.log.debug('output of IDL command: {}'.format(idl_cmd))
        self.log.debug('STDOUT----\n{}'.format(stdout))
        self.log.debug('STDERR----\n{}'.format(stderr))

    def _display_refstars(self, imname = None, imidx = None, icut = False, display = False, save_fig = None,
                          ax = None, x = None, y = None, labels = None):
        '''show (reference) image and plot selected reference stars'''

        def onpick(event, cut_list, ref, refp, fig):
            '''get index, append appropriate index to cut_list and remove star'''
            ind = event.ind[0]
            cut_list.append(ref.index.drop(cut_list)[ind])
            refp.set_data(ref.loc[ref.index.drop(cut_list), 'x'], ref.loc[ref.index.drop(cut_list), 'y'])
            fig.canvas.draw()

        # set calibration IDs if necessary
        if self.cal_IDs == 'all':
            self.cal_IDs = self.cal_use.index

        # read needed information from image
        if imname is None:
            imname = self.refname
        with fits.open(imname) as f:
            im = f[0].data
            head = f[0].header

        # find pixel locations of sn, reference stars, and radec stars
        cs = WCS(header = head)
        sn_x, sn_y = cs.all_world2pix(self.targetra, self.targetdec, 0)
        ref_x, ref_y = cs.all_world2pix(self.cal_use.loc[self.cal_IDs, 'ra'], self.cal_use.loc[self.cal_IDs, 'dec'], 0)
        ref = pd.DataFrame({'x': ref_x, 'y': ref_y}, index = self.cal_IDs)
        rd_x, rd_y = cs.all_world2pix(self.radec.loc[1:, 'RA'], self.radec.loc[1:, 'DEC'], 0)

        # plot (including interactive step if requested)
        if ax is None:
            fig, ax = plt.subplots(figsize = (8, 8))
        z = ZScaleInterval()
        zlim = z.get_limits(im.data)
        ax.imshow(-1*im, cmap = 'gray', vmin = -1*zlim[1], vmax = -1*zlim[0])
        ax.plot(sn_x, sn_y, 'mD', markersize = 15, mfc = 'none', mew = 2)
        if (x is not None) and (y is not None):
            ax.plot(x, y, 'bs', markersize = 15, mfc = 'none', mew = 2)
            if labels is not None:
                for ii in range(len(x)):
                    ax.annotate(labels[ii], (x[ii] + 20, y[ii]), color = 'b', size = 12)
        else:
            ax.plot(rd_x, rd_y, 'bs', markersize = 15, mfc = 'none', mew = 2)
            refp, = ax.plot(ref['x'], ref['y'], 'ro', markersize = 15, mfc = 'none', picker = 14, mew = 2)
            for idx, row in ref.iterrows():
                ax.annotate(idx, (row['x'] + 20*head['NAXIS1']/1024, row['y']), color = 'r', size = 12)
        ax.set_xticks(())
        ax.set_yticks(())
        if icut == True:
            cut_list = []
            plt.ion()
            cid = fig.canvas.mpl_connect('pick_event', lambda event: onpick(event, cut_list, ref, refp, fig))
            fig.show()
            input('click on circled reference stars to be removed [hit "enter" when done]')
            fig.canvas.mpl_disconnect(cid)
            plt.ioff()
            self.cal_IDs = self.cal_IDs.drop(cut_list)
        if display is True:
            plt.ion()
            plt.show()
        elif save_fig is not None:
            plt.savefig(save_fig)
        else:
            if imidx is None:
                plt.savefig(os.path.join(self.calibration_dir, 'ref_stars.png'))
            else:
                plt.savefig(os.path.join(self.calibration_dir, 'cut_img_{}.png'.format(imidx)))
            plt.close()

    def _display_obs_cal_mags(self, filt, id, sig = 3):
        '''show all observed mags of a given calibration star in a given passband'''

        # select relevant data
        selection = self.calibrators.loc[self.calibrators['Filter'] == filt, :].loc[(self.wIndex, id),['Mag_obs', 'system']]

        fig, ax = plt.subplots(1, 1, figsize = (7, 3))

        def onpick(event):
            '''get index, append appropriate index to cut_list and remove star'''
            ind = event.ind[0]
            ids = event.artist._x
            mags = event.artist._y
            print('\nIndex of clicked image mag: {}'.format(int(ids[ind])))
            sub = mags[ids != ids[ind]]
            print('Without this image: {:.2f} pm {:.2f}'.format(np.median(sub), np.std(sub)))

        colors = ('b','r','g','k','m')
        cnt = 0
        for sys, group in selection.groupby('system', sort = False):
            group = group.loc[group['Mag_obs'].notnull(), :]
            mags = group.loc[:, 'Mag_obs'].values
            ids = group.index.levels[0][group.index.labels[0]]
            line, = ax.plot(ids, mags, '{}.'.format(colors[cnt]), label = sys, picker = 5)
            ax.plot([ids.min(), ids.max()], [np.mean(mags)]*2, '{}--'.format(colors[cnt]),
                       label = '${:.2f} \pm {:.2f}$'.format(np.mean(mags), np.std(mags)))
            ax.plot([ids.min(), ids.max()], [np.mean(mags) + sig * np.std(mags)]*2, '{}:'.format(colors[cnt]),
                    label = '${}\sigma$ boundary'.format(sig))
            ax.plot([ids.min(), ids.max()], [np.mean(mags) - sig * np.std(mags)]*2, '{}:'.format(colors[cnt]))
            cnt += 1

        ax.set_title('Filter: {} Cal ID: {}'.format(filt, id))
        ax.legend(bbox_to_anchor = (1.01, 0.5), loc = 'center left')
        plt.tight_layout()
        cid = fig.canvas.mpl_connect('pick_event', lambda event: onpick(event))
        plt.show()
        fig.canvas.mpl_disconnect(cid)

    def compare_image2ref(self, idx):
        '''plot ref image and selected image side by side'''

        fig = plt.figure(figsize = (12, 6))
        ref = Phot(self.refname)
        wcs1 = WCS(header = ref.header)
        ax1 = fig.add_subplot(1, 2, 1, projection = wcs1)
        self._display_refstars(ax = ax1)
        wcs2 = WCS(header = self.phot_instances.loc[idx].header)
        ax2 = fig.add_subplot(1, 2, 2, projection = wcs2)
        self.phot_instances.loc[idx].display_image(ax = ax2, display = False)
        fig.show()

# provide script functionality via
# python LPP.py name
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type = str, help = 'name of the object')
    parser.add_argument('-a', '--add-images(s)', dest = 'new', type = str, default = False,
                        help = 'new image(s) or photlist to process')
    parser.add_argument('-i', '--interactive', dest = 'interactive', action = 'store_const',
                        const = True, default = False, help = 'run in interactive mode')
    parser.add_argument('-ct', '--force-color-term', dest = 'force_color_term', type = str, 
                        default = False, help = 'force to use specified color term')
    parser.add_argument('-dd', '--disc-date-mjd', dest = 'disc_date_mjd', type = float,
                        default = None, help = 'mjd of discovery')
    parser.add_argument('-c', '--cut-lc-points', dest = 'lc_file', type = str,
                        default = None, help = 'light curve file to cut points from')
    parser.add_argument('-cr', '--cut-raw-lc-points-and-regenerate', dest = 'raw_lc_file', type = str,
                        default = None, help = 'light curve file to cut points from')
    args = parser.parse_args()

    pipeline = LPP(args.name, interactive = args.interactive, force_color_term = args.force_color_term)
    pipeline.disc_date_mjd = args.disc_date_mjd
    if (args.new is False) and (args.lc_file is None) and (args.raw_lc_file is None):
        pipeline.run()
    elif (args.new is False) and (args.lc_file is not None):
        pipeline.cut_lc_points(args.lc_file)
    elif (args.new is False) and (args.raw_lc_file is not None):
        pipeline.load()
        pipeline.cut_lc_points(args.raw_lc_file, regenerate = True)
        pipeline.save()
        pipeline.write_summary()
    else:
        pipeline.load() # load from sav file
        if '_c.fit' in args.new:
            new_images = [fl.strip() for fl in args.new.replace(',', ' ').split(' ')]
            pipeline.process_new_images(new_image_list = new_images)
        else: # otherwise it is a photlist
            pipeline.process_new_images(new_image_file = args.new)
