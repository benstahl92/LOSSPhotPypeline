# internal imports
from LOSSPhotPypeline.image.Phot import Phot

def genconf(object = None, targetname = None, config_file = None):
    '''
    Generates template configuration file in current directory.

    Parameters
    ----------
    object : LPP instance, optional, default: None
        instance of LPP class from LOSSPhotPypeline.pipeline 
    targetname : str, optional, default: None
        name of sn
    config_file : str, optional, default: None
        name of configuration file to use
    '''

    if object is not None:
        targetname = object.targetname
        config_file = object.config_file
    elif (targetname is None) or (config_file is None):
        print('must either pass LPP object or both target and configuration file names')
        return

    with open(config_file, 'w') as f:
        f.write('{:<20}{}\n'.format('targetname', targetname))
        f.write('{:<20}\n'.format('targetra'))
        f.write('{:<20}\n'.format('targetdec'))
        f.write('{:<20}no\n'.format('photsub'))
        f.write('{:<20}apt\n'.format('calmethod'))
        f.write('{:<20}all\n'.format('photmethod'))
        f.write('{:<20}\n'.format('refname'))
        f.write('{:<20}{}.photlist\n'.format('photlistfile', targetname))
        f.write('{:<20}\nnone'.format('forcecalfit'))

def get_first_obs_date(object):
    '''
    Finds earliest image file (determined automatically if LPP pipeline is run from beginning).

    Parameters
    ----------
    object : LPP instance, optional, default: None
        instance of LPP class from LOSSPhotPypeline.pipeline 
    '''
    
    first_obs = None
    for fl in object.image_list:
        c = Phot(fl, object.radecfile)
        if (first_obs is None) or (c.mjd < first_obs):
            first_obs = c.mjd
    return first_obs

def get_color_term(fl):
    '''given an image file from kait or nickel, returns the color term'''

    # instantiate file object
    fl_obj = Phot(fl)

    # select color term based on telescope and date
    if fl_obj.telescope == 'kait':
        tel = 'kait'
        if fl_obj.mjd < 51229.0: # mjd of 1999-02-20
            tel += '1'
        elif fl_obj.mjd < 52163.0: # mjd of 2001-09-11
            tel += '2'
        elif fl_obj.mjd < 54232.0: # mjd of 2007-05-12
            tel += '3'
        else:
            tel += '4'
    elif fl_obj.telescope == 'Nickel':
        tel = 'nickel'
        if fl_obj.mjd < 54845.0: # mjd of 2009-01-14
            tel += 1
        else:
            tel += 2
    else:
        tel = None

    return tel
