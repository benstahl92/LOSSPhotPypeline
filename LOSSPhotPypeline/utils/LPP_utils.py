# standard imports
import subprocess
import shlex
import pandas as pd
import os

try:
    from pyzaphotdb import zaphot_search_by_radec, storelocation
    haveDB = True
except ModuleNotFoundError:
    haveDB = False

def genconf(obj = None, targetname = None, config_file = None, ra = '', dec = '', refname = ''):
    '''
    Generates template configuration file in current directory.

    Parameters
    ----------
    obj : LPP instance, optional, default: None
        instance of LPP class from LOSSPhotPypeline.pipeline 
    targetname : str, optional, default: None
        name of sn
    config_file : str, optional, default: None
        name of configuration file to use
    '''

    if obj is not None:
        targetname = obj.targetname
        config_file = obj.config_file
    elif (targetname is None) or (config_file is None):
        print('must either pass LPP object or both target and configuration file names')
        return

    with open(config_file, 'w') as f:
        f.write('{:<20}{}\n'.format('targetname', targetname))
        f.write('{:<20}{}\n'.format('targetra', ra))
        f.write('{:<20}{}\n'.format('targetdec', dec))
        f.write('{:<20}yes\n'.format('photsub'))
        f.write('{:<20}auto\n'.format('calsource'))
        f.write('{:<20}all\n'.format('photmethod'))
        f.write('{:<20}{}\n'.format('refname', refname))
        f.write('{:<20}{}.photlist\n'.format('photlistfile', targetname))
        f.write('{:<20}none\n'.format('forcecolorterm'))

def get_first_obs_date(obj):
    '''
    Finds earliest image file.

    Parameters
    ----------
    obj : LPP instance, optional, default: None
        instance of LPP class from LOSSPhotPypeline.pipeline 
    '''

    first_obs = None
    for instance in obj.phot_instances:
        if (first_obs is None) or (instance.mjd < first_obs):
            first_obs = instance.mjd
    return first_obs

def get_template_candidates(targetra, targetdec, disc_date_mjd, templates_dir, late_time_begin = 365):
    '''search database to identify candidate template images for galaxy subtraction'''

    if not haveDB:
        msg = 'Database unavailable. Exiting.'
        return msg

    cand = pd.DataFrame(zaphot_search_by_radec(targetra, targetdec, 3))

    # select only candidates that are before the first observation or at least one year later
    # further sub-select so that only condiering BVRI from Nickel and CLEAR from KAIT
    cand = cand[((cand.mjd < disc_date_mjd) | (cand.mjd > (disc_date_mjd + late_time_begin)))]
    cand = cand[((cand.telescope.str.lower() == 'kait') & cand['filter'].str.upper().isin(['CLEAR'])) | 
                ((cand.telescope.str.lower() == 'nickel') & cand['filter'].str.upper().isin(['B','V','R','I']))]

    get_templ_fl_msg = ''
    radecmsg = 'RA: {} DEC: {}'.format(targetra, targetdec)

    if len(cand['filter'].drop_duplicates()) == 0: # need at least one per pass band
        msg = 'no suitable candidates, schedule observations:\n{}'.format(radecmsg)
        with open('GET.TEMPLATES', 'w') as f:
            f.write(msg)
        return msg
    elif len(cand['filter'].drop_duplicates()) < 5:
        msg = 'not enough candidates (at least one per passband), schedule observations:\n{}'.format(radecmsg)
        with open('GET.TEMPLATES', 'w') as f:
            f.write(msg)

    # rank candidates, write to file
    if not os.path.isdir(templates_dir):
        os.makedirs(templates_dir)
    cand['fullpath'] = storelocation + cand['savepath'] + cand['uniformname']
    cols = ['fullpath','mjd','telescope','filter','fwhm','zeromag','limitmag']
    cand = cand[cols].sort_values(['filter', 'limitmag'], ascending = [True, False])
    cand.to_csv(os.path.join(templates_dir, 'template.candidates'), sep = '\t', index = False, na_rep = 'None')
    msg = 'template candidates written'

    return msg

def idl(idl_cmd, log = None):
    '''execute a given IDL command and do logging as needed'''

    p = subprocess.Popen(shlex.split(idl_cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)
    stdout, stderr = p.communicate()
    if log is not None:
        log.debug('running IDL command: {}'.format(idl_cmd))
        #stdout, stderr = p.communicate()
        log.debug(stdout)
        log.debug(stderr)
    p.wait()
    del p
