# standard imports
import os
import shutil
import inspect
from pprint import pprint
import pidly
import pickle as pkl
import copy
import pandas as pd
import numpy as np
from tqdm import tqdm
import logging
from contextlib import redirect_stdout
import subprocess
import warnings
from astropy.io import fits
from astropy.wcs import WCS
from astropy.utils.exceptions import AstropyWarning
warnings.simplefilter('ignore', category=AstropyWarning)

# try for packages that may not be available
try:
    from pyzaphotdb import zaphot_search_by_radec, storelocation
    haveDB = True
except ModuleNotFoundError:
    haveDB = False

# internal imports
import LOSSPhotPypeline
import LOSSPhotPypeline.utils as LPPu
from LOSSPhotPypeline.image import Phot, FitsInfo, FileNames

# setup tqdm for pandas
tqdm.pandas()

class LPP(object):
    '''Lick Observatory Supernova Search Photometry Reduction Pipeline'''

    def __init__(self, targetname, interactive = True, quiet_idl = True, cal_diff_tol = 0.20, force_color_term = False):
        '''Instantiation instructions'''

        # basics from instantiation
        self.targetname = targetname.lower().replace(' ', '')
        self.config_file = targetname + '.conf'
        self.interactive = interactive
        self.cal_diff_tol = cal_diff_tol

        # log file
        self.logfile = self.targetname.lower().replace(' ', '') + '.log'
        self.build_log()

        # setup idl
        self.idl = pidly.IDL()
        if quiet_idl:
            self.idl('!quiet = 1')
            self.idl('!except = 0')

        # to be sourced from configuration file
        self.targetra = None
        self.targetdec = None
        self.photsub = False
        self.photmethod = 'all'
        self.refname=''
        self.photlistfile=''

        # check if config file exists -- if not then generate template
        if not os.path.isfile(self.config_file):
            self.log.warn('No configuration file detected, complete template ({}) before proceeding.'.format(self.config_file + '.template'))
            LPPu.genconf(targetname = self.targetname, config_file = self.config_file + '.template')
            return

        # general variables
        self.filter_set_ref = ['B', 'V', 'R', 'I', 'CLEAR']
        self.filter_set = None
        self.filter_set_sub = None
        self.first_obs = None
        self.phot_cols = {'3.5p': 3, '5p': 5, '7p': 7, '9p': 9, '1fh': 11, '1.5fh': 13, '2fh': 15, 'psf': 17}
        self.calmethod = 'psf' # can be set to any key in phot_cols, but recommended is 'psf'
        self.image_list = []
        self.phot_instances = []
        self.phot_failed = []
        self.phot_sub_failed = []
        self.cal_failed = []
        self.cal_sub_failed = []
        self.no_obj = []
        self.no_obj_sub = []

        self.cal_source = 'auto'
        self.calfile=''
        self.calfile_use=''
        self.force_color_term = force_color_term

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

        # calibration variables
        self.calibration_dir = 'calibration'
        if not os.path.isdir(self.calibration_dir):
            os.makedirs(self.calibration_dir)
        self.radecfile = os.path.join(self.calibration_dir, self.targetname + '_radec.txt')
        #self.color_term = LPPu.get_color_term(self.refname)
        # keep track of counts of color terms
        self.color_terms = {'kait1': 0, 'kait2': 0, 'kait3': 0, 'kait4': 0,
                            'nickel1': 0, 'nickel2':,
                            'Landolt': 0}

        # lightcurve variables
        self.lc_dir = 'lightcurve'
        self.lc_base = None
        self.lc_raw = None
        self.lc_raw_sub = None
        self.lc_bin = None
        self.lc_bin_sub = None
        self.lc_group = None
        self.lc_group_sub = None
        self.lc = None
        self.lc_sub = None

        # galaxy subtraction variables
        self.template_images = None
        self.templates_dir = 'templates'

        # steps in standard reduction procedure
        self.current_step = 0
        self.steps = [self.find_ref_stars,
                      self.get_images,
                      self.do_galaxy_subtraction_all_image,
                      self.do_photometry_all_image,
                      self.do_calibration,
                      self.generate_lc]

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
        vs.pop('idl')
        vs.pop('log')
        vs.pop('phot_instances')
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
        self.phot_instances = self._im2inst(self.image_list, mode = 'quiet')
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
        '''
        identifies all suitable stars in reference image
        computes ra & dec positions
        writes radecfile and loads into memory
        '''

        # if radecfile already exist, no need to do it
        if os.path.isfile(self.radecfile):
            self.log.info('radecfile already exists, loading only')
            self.radec = pd.read_csv(self.radecfile, delim_whitespace=True, skiprows = (0,1,3,4,5), names = ['RA','DEC'])
            return
        if self.refname == '' :
            self.log.warn('refname has not been assigned, please do it first!')
            return

        # instantiate object to manage names
        nametmp=FileNames(self.refname)

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
                    '-CATALOG_NAME', nametmp.sobj,
                    '-CHECKIMAGE_NAME', nametmp.skyfit]
        p = subprocess.Popen(cmd_list, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        self.log.debug(p.communicate())

        # make sure process succeeded
        if not os.path.isfile(nametmp.sobj):
            self.log.warn('SExtractor failed --- no sobj file generated, check!')
            return

        # read sobj file of X_IMAGE and Y_IMAGE columns, as well as MAG_APER for sort
        with fits.open(nametmp.sobj) as hdul:
            data=hdul[1].data
        # sort according to magnitude, from small/bright to hight/faint
        data.sort(order='MAG_APER')
        imagex=data.X_IMAGE
        imagey=data.Y_IMAGE

        # transform to RA and DEC using ref image header information
        with fits.open(self.refname) as ref:
            cs = WCS(header=ref[0].header)
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

    def get_images(self):
        '''reads image list file to generate lists of file names and Phot instances'''

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

    def do_galaxy_subtraction_all_image(self, image_list = None):
        '''performs galaxy subtraction on all selected image files'''

        if not self.photsub:
            self.log.warn('not in photsub mode, skipping galaxy subtraction')
            return

        self.log.info('starting galaxy subtraction on all images')

        if image_list is None:
            image_list = self.image_list
        else:
            self.log.info('using argument supplied image list')

        if self.template_images is None:
            self.get_template_images()
            if self.template_images is None:
                self.log.warn('could not get suitable template images, running without galaxy subtraction')
                self.photsub = False
                return

        # iterate through image list and perform galaxy subtraction on each
        for fl in tqdm(image_list):
            c = Phot(fl)
            with redirect_stdout(self.log):
                if self.photsub:
                    c.galaxy_subtract(self.template_images)

        self.log.info('galaxy subtraction done')

    def do_photometry_all_image(self, image_list = None):
        '''performs photometry on all selected image files'''

        self.log.info('starting photometry on all images (galsub: {})'.format(self.photsub))

        if image_list is None:
            image_list = self.image_list
        else:
            self.log.info('using argument supplied image list')

        # iterate through image list and perform photometry on each
        # also determine date of first observation since already touching each file
        first_obs = None
        for idx, fl in tqdm(image_list.iteritems(), total = len(image_list)):
            img = self.phot_instances.loc[idx]
            with redirect_stdout(self.log):
                img.do_photometry(photsub = self.photsub, log = self.log)
            if (first_obs is None) or (img.mjd < first_obs):
                first_obs = img.mjd
            # check for success
            if os.path.exists(img.psf) is False:
                self.log.warn('photometry failed --- {} not generated'.format(img.psf))
                self.phot_failed.append(fl)
            if (self.photsub is True) and (os.path.exists(img.psfsub) is False):
                self.log.warn('photometry (sub) failed --- {} not generated'.format(img.psfsub))
                self.phot_sub_failed.append(fl)
        if self.first_obs is None:
            self.first_obs = first_obs

        # remove failures from image list where possible
        if self.photsub is False:
            self.image_list = self.image_list[~self.image_list.isin(pd.Series(self.phot_failed))]
        else:
            self.image_list = self.image_list[~self.image_list.isin(pd.Series(self.phot_failed)) & ~self.image_list.isin(pd.Series(self.phot_failed))]

        self.log.info('photometry done')

    def calibrate(self, second_pass = False, image_list = None):
        '''performs calibration on all images included in photlistfile, using outputs from do_photometry_all_image'''

        self.log.info('commencing calibration (second pass: {})'.format(second_pass))

        if image_list is None:
            image_list = self.image_list
        else:
            self.log.info('using argument supplied image list')

        # check for calibration data and download if it doesn't exist yet
        if not second_pass and ((not os.path.isfile(self.calfile)) or (self.calfile == '') or (self.cal_source == '')):
            catalog = LPPu.astroCatalog(self.targetname, self.targetra, self.targetdec, relative_path = self.calibration_dir)
            catalog.get_cal(method = self.cal_source)
            with redirect_stdout(self.log):
                catalog.to_natural()
            self.calfile = catalog.cal_filename
            self.cal_source = catalog.cal_source
            self.log.info('calibration data sourced')

        # otherwise if in second pass mode, perform second calibration using edited calibration list
        elif second_pass is True:
            catalog = LPPu.astroCatalog(self.targetname, self.targetra, self.targetdec, relative_path = self.calibration_dir)
            catalog.cal_filename = self.calfile_use
            catalog.cal_source = self.cal_source
            with redirect_stdout(self.log):
                catalog.to_natural()
            self.log.info('using edited calibration list')

        # iterate through image list and execute calibration script on each
        for idx, fl in tqdm(image_list.iteritems(), total = len(image_list)):

            # skip if photometry has failed
            if (fl in self.phot_failed) and (self.photsub is True) and (fl in self.phot_sub_failed):
                continue
            elif (fl in self.phot_failed) and (self.photsub is False):
                continue

            # instantiate file object
            img = self.phot_instances.loc[idx]

            # get color term and enforce only one color term per run if not forced
            if self.force_color_term is False:
                #tel = LPPu.get_color_term(fl)
                #if self.color_term is not None:
                #   assert self.color_term == tel
                #self.color_term = tel
                self.color_terms[img.color_term] += 1
            else:
                self.color_terms[self.force_color_term] += 1

            # execute idl calibration procedure
            with redirect_stdout(self.log):
                # set photsub mode appropriately
                do_photsub = self.photsub
                if (self.photsub is True) and (fl in self.phot_sub_failed):
                    do_photsub = False
                self.idl.pro('lpp_cal_instrumag', fl, img.filter.upper(), self.cal_source, os.path.join(self.calibration_dir, self._ct2cf(img.color_term)),
                              photsub = do_photsub, output = True)
                # also get zero value
                img.get_zeromag()

            # check for success
            if os.path.exists(img.psfdat) is False:
                self.log.warn('calibration failed --- {} not generated'.format(img.psfdat))
                self.cal_failed.append(fl)
            if (self.photsub is True) and (os.path.exists(img.psfsubdat) is False):
                self.log.warn('calibration (sub) failed --- {} not generated'.format(img.psfsubdat))
                self.cal_sub_failed.append(fl)

    def process_calibration(self, photsub_mode = False):
        '''combines all calibrated results (.dat files), grouped by filter, into data structure so that cuts can be made'''

        self.log.info('processing calibration')

        # underlying data structure for handling this will be dictionary keyed by filter
        # for each key, there is another dictionary keyed by ID with each value being a list of magnitudes
        results = {}

        self.calfile_use = self.calfile.replace('.dat', '_use.dat')

        # generate ordered calibration file
        with redirect_stdout(self.log):
            self.idl.pro('lpp_pick_good_refstars', list(range(225)), self.radecfile, os.path.join(self.calibration_dir, self.calfile), output = True)
            self.idl.pro('lpp_cal_dat2fit_{}'.format(self.cal_source.lower()), os.path.join(self.calibration_dir, self.calfile_use), output = True)

        # read ordered calibration file, using index offset to match
        cal = pd.read_csv(os.path.join(self.calibration_dir, self.calfile_use), delim_whitespace = True)
        IDs = cal['starID'] + 2

        # iterate through files and store photometry into data structure
        for idx, fl in tqdm(self.image_list.iteritems(), total = len(self.image_list)):

            # skip failed images
            if (fl in self.phot_failed) and (self.photsub is True) and (fl in self.phot_sub_failed):
                continue
            elif (fl in self.phot_failed) and (self.photsub is False):
                continue
            if fl in self.cal_failed:
                continue

            img = self.phot_instances.loc[idx]
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

        tmp = list(results.keys()).sort(key = lambda x: self.filter_set_ref.index(x))
        if photsub_mode is False:
            self.filter_set = tmp
        else:
            self.filter_set_sub = tmp

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

        self.calibrate()
        self.process_calibration()
        self.calibrate(second_pass = True)

        self.log.info('full calibration sequence completed')

    def generate_raw_lcs(self, color_term, photsub_mode = False, color_term = None):
        '''builds raw light curve files from calibrated results'''

        self.log.info('generating raw lightcurve(s)')

        columns = (';; MJD','etburst', 'mag', '-emag', '+emag', 'limmag', 'filter', 'imagename')
        lc = {name: [] for name in columns}
        lcs = {m: copy.deepcopy(lc) for m in self.photmethod}
        has_filt = np.array([False] * len(self.filter_set_ref))

        if color_term is None:
            iter_len = len(self.image_list)
        else:
            iter_len = self.color_terms[color_term]

        # iterate through files and extract LC information
        for idx, fl in tqdm(self.image_list.iteritems(), total = iter_len):

            img = self.phot_instances.loc[idx]

            # immediately skip if not the appropriate color term
            if (color_term != None) and (color_term != img.color_term):
                continue

            # skip failed images (some checks here should be redundant)
            if (fl in self.phot_failed) and (self.photsub is True) and (fl in self.phot_sub_failed):
                continue
            elif (fl in self.phot_failed) and (self.photsub is False):
                continue
            if (fl in self.cal_failed) and (photsub_mode is False):
                continue
            elif (fl in self.cal_sub_failed) and (photsub_mode is True):
                continue

            img.calc_limmag()

            # read photometry results
            cols = (0,) + sum(((self.phot_cols[m], self.phot_cols[m] + 1) for m in self.photmethod), ())
            col_names = ('ID',) + sum(((m + '_mag', m + '_err') for m in self.photmethod), ())

            if photsub_mode is False:
                dat = img.psfdat
            else:
                dat = img.psfsubdat

            d = pd.read_csv(dat, header = None, delim_whitespace = True, comment = ';', usecols=cols, names = col_names)

            if 1 not in d['ID'].values:
                self.log.warn('no object in calibrated photometry file: {}'.format(dat))
                if photsub_mode is False:
                    self.no_obj.append(fl)
                else:
                    self.no_obj_sub.append(fl)
            else:
                has_filt[np.array(self.filter_set_ref) == img.filter.upper()] = True

            for m in self.photmethod:
                lcs[m][';; MJD'].append(round(img.mjd, 6))
                lcs[m]['etburst'].append(round(img.exptime / (60 * 24), 5)) # exposure time in days
                lcs[m]['filter'].append(img.filter)
                lcs[m]['imagename'].append(fl)
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

        tmp = list(np.array(self.filter_set_ref)[has_filt])
        if photsub_mode is False:
            self.filter_set = tmp
        else:
            self.filter_set_sub = tmp

        for m in self.photmethod:
            if color_term is None:
                comp = ''
            else:
                comp = color_term + '_'
            if photsub_mode is False:
                lc_raw_name = self.lc_base + comp + m + '_natural_raw.dat'
                filter_set = self.filter_set
            else:
                lc_raw_name = self.lc_base + comp + m + '_natural_raw_sub.dat'
                filter_set = self.filter_set_sub
            lc_raw = pd.DataFrame(lcs[m])
            lc_raw.to_csv(lc_raw_name, sep = '\t', columns = columns, index = False, na_rep = 'NaN')
            p = LPPu.plotLC(lc_file = lc_raw_name, name = self.targetname, photmethod = m)
            p.plot_lc(extensions = ['.ps', '.png'])

        self.log.info('raw light curves generated')

    def generate_bin_lc(self, lc_file = None):
        '''wraps IDL lightcurve binning routine'''

        if lc_file is None:
            lc_file = self.lc_raw

        with redirect_stdout(self.log):
            self.idl.pro('lpp_dat_res_bin', lc_file, self.lc_bin, outfile = self.lc_bin, output = True)
            if self.photsub is True:
                self.idl.pro('lpp_dat_res_bin', self.lc_raw_sub, self.lc_bin_sub, outfile = self.lc_bin_sub, output = True)

        self.log.info('binned light curve(s) generated')

    def generate_group_lc(self, lc_file = None):
        '''wraps IDL lightcurve grouping routine'''

        if lc_file is None:
            lc_file = self.lc_bin

        with redirect_stdout(self.log):
            self.idl.pro('lpp_dat_res_group', lc_file, self.lc_group, outfile = self.lc_group)
            if self.photsub is True:
                self.idl.pro('lpp_dat_res_group', self.lc_bin_sub, self.lc_group_sub, outfile = self.lc_group_sub)

        self.log.info('grouped light curve(s) generated')

    def generate_final_lc(self, color_term = None, lc_table = None):
        '''wraps IDL routine to convert to natural system'''

        if lc_table is None:
            lc_table = self.lc_group

        with redirect_stdout(self.log):
            self.idl.pro('lpp_invert_natural_stand_objonly', lc_table, self.color_term, outfile = self.lc, output = True)
            if self.photsub is True:
                self.idl.pro('lpp_invert_natural_stand_objonly', self.lc_group_sub, color_term, outfile = self.lc_sub, output = True)

        self.log.info('final light curve(s) generated')

    def generate_lc(self):
        '''performs all functions to transform image photometry into calibrated light curve of target'''

        # set up file system
        if not os.path.isdir(self.lc_dir):
            os.makedirs(self.lc_dir)
        self.lc_base = os.path.join(self.lc_dir, 'lightcurve_{}_'.format(self.targetname))

        # run through all lc routines for all apertures, with all color terms used
        for ct in {key: self.color_terms[key] for in self.color_terms.keys() if self.color_terms[key] > 0}:
            self.generate_raw_lcs(color_term = ct)
            if self.photsub is True:
                self.generate_raw_lcs(photsub_mode = Truecolor_term = ct)
            for m in self.photmethod:
                self.lc_raw = self.lc_base + ct + '_' + m + '_natural_raw.dat'
                self.lc_bin = self.lc_base + ct + '_' + m + '_natural_bin.dat'
                self.lc_group = self.lc_base + ct + '_' + m + '_natural_group.dat'
                self.lc = self.lc_base + m + ct + '_' + '_standard.dat'
                if self.photsub is True:
                    self.lc_raw_sub = self.lc_base + ct + '_' + m + '_natural_raw_sub.dat'
                    self.lc_bin_sub = self.lc_base + ct + '_' + m + '_natural_bin_sub.dat'
                    self.lc_group_sub = self.lc_base + ct + '_' + m + '_natural_group_sub.dat'
                    self.lc_sub = self.lc_base + ct + '_' + m + '_standard_sub.dat'
                self.generate_bin_lc()
                self.generate_group_lc()
                self.generate_final_lc(ct)
                p = LPPu.plotLC(lc_file = self.lc, name = self.targetname, photmethod = m)
                p.plot_lc(extensions = ['.ps', '.png'])
                if self.photsub is True:
                    p = LPPu.plotLC(lc_file = self.lc_sub, name = self.targetname, photmethod = m)
                    p.plot_lc(extensions = ['.ps', '.png'])

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

        # update image list to include everything
        self.image_list = self.image_list.append(new_image_list, ignore_index = True)

        # perform photometry on new images
        self.do_photometry_all_image(image_list = new_image_list)

        # perform calibration
        full_cal = False
        if self.interactive:
            resp = input('\nperform full re-calibration? (y/[n]) > ')
            if 'y' in resp.lower():
                full_cal = True
        if full_cal:
            self.current_step = self.steps.index(self.do_photometry_all_image)
        else:
            self.calibrate(second_pass = False, image_list = new_image_list)
            self.current_step = self.steps.index(self.generate_lc)

        # run program after calibration has been completed
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

    def get_template_images(self, late_time_begin = 365):
        '''searches database to identify template images for galaxy subtraction'''

        if not haveDB:
            self.log.warn('Database unavailable. Exiting.')
            return

        if self.first_obs is None:
            self.first_obs = LPPu.get_first_obs_date(self)

        base_dir = storelocation

        # is this a good choice for the radius?
        cand = pd.DataFrame(zaphot_search_by_radec(self.targetra, self.targetdec, 3))

        # select only candidates that are before the first observation or at least one year later
        cand = cand[(cand.mjd < self.first_obs) | (cand.mjd > (self.first_obs + late_time_begin))]

        get_templ_fl_msg = ''
        radecmsg = 'RA: {} DEC: {}'.format(self.targetra, self.targetdec)

        if len(cand) == 0:
            msg = 'No suitable candidates in any band. Schedule observations:\n{}'.format(radecmsg)
            get_templ_fl_msg += msg
            self.log.warn(msg)
            with open('GET.TEMPLATES', 'w') as f:
                f.write(get_templ_fl_msg)
            return

        self.template_images = {filt: None for filt in self.filter_set}

        # iterate through filters to determine the best template for each
        for idx, filt in cand['filter'].drop_duplicates().iteritems():
            tmp = cand[cand['filter'] == filt]
            if len(tmp) == 0:
                msg = 'No suitable indidates in the {} band. Schedule an observation:\n{}'.format(filt, radecmsg)
                get_templ_fl_msg += msg + '\n'
                self.log.warn(msg)
            elif len(tmp) == 1:
                self.log.info('Only one candidate found in the {} band'.format(filt))
                if tmp.iloc[0]['telescope'].lower() != 'nickel':
                    msg1 = 'Not a Nickel image.'
                    msg2 = 'May want to schedule observation, but using in meantime.'
                    get_templ_fl_msg += msg1 + '\n' + msg2 + '\n'
                    self.log.warn('{}\n{}\n{}'.format(msg1, msg2, radecmsg))
                self.template_images[filt] = base_dir + tmp.iloc[0]['savepath'] + tmp.iloc[0]['uniformname']
            else:
                tmp = tmp.sort_values('limitmag', ascending=False)
                # compare the best two images
                if (tmp['fwhm'].iloc[0] - tmp['fwhm'].iloc[1] > 0.3) and (tmp['limitmag'].iloc[0] - tmp['limitmag'].iloc[1] < 3):
                    index_to_use = 1
                else:
                    index_to_use = 0
                if tmp.iloc[index_to_use]['telescope'].lower() != 'nickel':
                    msg1 = 'Best {} image is not from Nickel.'.format(filt)
                    msg2 = 'May want to schedule observation, but using in meantime.'
                    get_templ_fl_msg += msg1 + '\n' + msg2 + '\n'
                    self.log.warn('{}\n{}\n{}'.format(msg1, msg2, radecmsg))
                self.template_images[filt] = os.path.join(base_dir, tmp.iloc[index_to_use]['savepath'], tmp.iloc[index_to_use]['uniformname'])

        with open('GET.TEMPLATES', 'w') as f:
            f.write(get_templ_fl_msg)
            f.write(radecmsg)

        if not os.path.isdir(self.templates_dir):
            os.makedirs(self.templates_dir)

        # simple check for file existence and copy to templates dir
        for filt in self.template_images.keys():
            decomp = False
            if os.path.exists(self.template_images[filt]):
                pass
            elif os.path.exists(self.template_images[filt] + '.gz'):
                self.template_images[filt] += '.gz'
                decomp = True
            else:
                print('file format not recognized')
                return
            shutil.copy2(self.template_images[filt], os.path.join(self.templates_dir,self.template_images[filt].split('/')[-1]))
            self.template_images[filt] = os.path.join(self.templates_dir,self.template_images[filt].split('/')[-1])
            if decomp:
                subprocess.Popen(['gzip', '-d', '-q', '-f', self.template_images[filt]])
                self.template_images[filt] = self.template_images[filt][:-3]

        # rebin if needed
        for filt in self.template_images.keys():
            fl_obj = FitsInfo(self.template_images[filt])
            if (fl_obj.telescope.lower() == 'nickel') and ('kait' in self.color_term):
                self.idl.pro('lpp_rebin_nickel2kait', self.template_images[filt], savefile = self.template_images[filt])

        # optionally show template images
        if self.interactive:
            resp = input('\ndisplay template images? (y/[n]) > ')
            if 'y' in resp.lower():
                os.system('ds9 -zscale {} &'.format(' '.join([self.template_images[filt] for filt in self.template_images.keys()])))

        self.log.info('template images selected')

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

        if mode != 'quiet':
            return image_list.progress_apply(Phot, radec = self.radec, idl = self.idl)
        else:
            return image_list.apply(Phot, radec = self.radec, idl = self.idl)