# standard imports
import subprocess
import shlex

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
        f.write('{:<20}\n'.format('targetra'))
        f.write('{:<20}\n'.format('targetdec'))
        f.write('{:<20}yes\n'.format('photsub'))
        f.write('{:<20}auto\n'.format('calsource'))
        f.write('{:<20}all\n'.format('photmethod'))
        f.write('{:<20}\n'.format('refname'))
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

def idl(idl_cmd, log = None):
    '''execute a given IDL command and do logging as needed'''

    p = subprocess.Popen(shlex.split(idl_cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)
    p.wait()
    if log is not None:
        log.debug('running IDL command: {}'.format(idl_cmd))
        stdout, stderr = p.communicate()
        log.debug(stdout)
        log.debug(stderr)
    del p
