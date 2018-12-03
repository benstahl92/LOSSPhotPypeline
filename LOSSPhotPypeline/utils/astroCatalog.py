# standard package imports
import requests
import pandas as pd
import numpy as np
import os
from astropy.io import ascii, fits
import warnings

# filter warnings on import
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from astroquery.sdss import SDSS

# separate out packages that may not be available
try:
    from astrosql.sqlconnector import connect
    from astrosql import AstroSQL
    apass = True
except ModuleNotFoundError:
    apass = False

# internal imports
from LOSSPhotPypeline.utils.LPP_utils import idl

class astroCatalog:
    '''
    handles calibration source selection from a variety of sources, writes cal file
        for ingestion by photometry pipeline, and wraps IDL procedures to convert
        to natural systems

    Implemented Sources : methods are <SOURCE>_get_calib()
    -------------------
    PanSTARRS (PS1)
    SDSS
    APASS

    Other Methods
    -------------
    to_natural : wraps IDL code to write magnitudes in needed natural systems

    B. Stahl - June 14, 2018
    '''

    def __init__(self, name, ra, dec, relative_path = ''):
        self.targetname = name
        self.targetra = ra
        self.targetdec = dec
        self.cal_source = None
        self.cal_filename = None
        self.relative_path = relative_path

    def PS1_get_calib(self, rad_deg = 0.1, tmp_fl = 'ps1.csv',
                      server='http://gsss.stsci.edu/webservices/vo/CatalogSearch.aspx'):
        '''
        Parameters
        ----------
        rad_deg (optional, int or float) : search radius in decimal degrees
        tmp_fl (optional, str) : temporary filename for unprocessed search results
        server (optional, str) : base url for search access

        Output
        ------
        file : writes processed calibration file and sets member variables
        '''

        # formulate and execute query
        params = {'RA': self.targetra, 'DEC': self.targetdec, 'SR': rad_deg,
                  'FORMAT': 'csv', 'CAT': 'PS1V3OBJECTS'}
        r = requests.get(server, params = params)

        # write results into temporary file
        with open(tmp_fl, 'w') as f:
            f.write(r.text)

        # define structures for column name conversion and rounding
        in_cols = ['raMean', 'decMean', 'gMeanPSFMag', 'gMeanPSFMagErr', 'rMeanPSFMag','rMeanPSFMagErr',
                   'iMeanPSFMag', 'iMeanPSFMagErr', 'zMeanPSFMag', 'zMeanPSFMagErr',
                   'yMeanPSFMag', 'yMeanPSFMagErr']
        out_cols = ['ra', 'dec', 'g', 'gErr', 'r', 'rErr', 'i', 'iErr', 'z', 'zErr', 'y', 'yErr']
        decimals = pd.Series([7,7,3,3,3,3,3,3,3,3,3,3], index = out_cols)

        # read desired columns in and format for calib file output, catch case where search fails
        try:
            data = pd.read_csv(tmp_fl, comment = '#', usecols = in_cols, na_values = -999)
            data.dropna(inplace = True)
            data.columns = out_cols
            os.system('rm {}'.format(tmp_fl)) # remove temp file
        except ValueError:
            print('Search of PS1 for calibration information failed...')
            os.system('rm {}'.format(tmp_fl)) # remove temp file
            return None

        self.cal_source = 'PS1'
        self.cal_filename = 'cal_{}_{}.dat'.format(self.targetname, self.cal_source)
        data.round(decimals).to_csv(os.path.join(self.relative_path, self.cal_filename), sep = '\t', index = False, header = True)

    def SDSS_get_calib(self, rad_min = 5):
        '''
        Parameters
        ----------
        rad_min (optional, int or float) : search radius in decimal arcminutes

        Output
        ------
        file : writes processed calibration file and sets member variables
        '''

        # formulate SQL query and execute
        query = '''SELECT p.ra, p.dec, p.u, p.Err_u, p.g, p.Err_g, p.r, p.Err_r, p.i, p.Err_i, p.z, p.Err_z
                    FROM fGetNearbyObjEq({},{},{}) n, PhotoPrimary p
                    WHERE n.objID = p.objID AND p.type = 6'''.format(self.targetra, self.targetdec, rad_min)
        data = SDSS.query_sql(query)

        # process and return results
        if data is None:
            print('Search of SDSS for calibration information failed...')
            return None

        for filt in 'ugriz':
            data.rename_column('Err_' + filt, filt + 'Err')

        self.cal_source = 'SDSS'
        self.cal_filename = 'cal_{}_{}.dat'.format(self.targetname, self.cal_source)
        ascii.write(data, os.path.join(self.relative_path, self.cal_filename))

    def APASS_get_calib(self, rad_min = 5):
        '''
        adapted from code originally written by K. Zhang

        Parameters
        ----------
        rad_min (optional, int or float) : search radius in decimal arcminutes

        Output
        ------
        file : writes processed calibration file and sets member variables
        '''

        if not apass:
            print('APASS not supported due to missing package')
            return

        # connect to APASS database
        connection = connect()
        db = AstroSQL(connection)
        table = db.get_table('apass')

        # search and format results
        dict_lst = db.get_by_radec(table, self.targetra, self.targetdec, rad_min)
        df = pd.DataFrame(data=dict_lst, columns=dict_lst[0].keys())
        df = df[['RA', 'DEC', 'V', 'Verr', 'B', 'Berr', 'g', 'gerr', 'r', 'rerr', 'i', 'ierr']]
        df = df.replace([99.9990], [np.nan])
        df = df.dropna()

        self.cal_source = 'APASS'
        self.cal_filename = 'cal_{}_{}.dat'.format(self.targetname, self.cal_source)
        df.to_csv(os.path.join(self.relative_path, self.cal_filename), sep = '\t', index=False, header = True, float_format='%9.4f')

    def get_cal(self, method = 'auto'):
        '''obtains calibration information from specified method or by trying sources in preferred order until data is obtained (auto mode)'''

        if method.lower() not in ['ps1','sdss','apass']:
            self.PS1_get_calib()
            if self.cal_filename is not None:
                return
            if self.cal_filename is None:
                self.SDSS_get_calib()
                if self.cal_filename is not None:
                    return
            if self.cal_filename is None:
                self.APASS_get_calib()
                return
            # if it gets to here, print warning
            print('warning: calibration data not found!!!')
            return
        elif method.lower() == 'ps1':
            self.PS1_get_calib()
        elif method.lower() == 'sdss':
            self.SDSS_get_calib()
        elif method.lower() == 'apass':
            self.APASS_get_calib()

    def to_natural(self):
        '''wraps the appropriate IDL procedure to convert calibration to natural systems'''

        # select appropriate IDL procedure
        pro = 'lpp_cal_dat2fit_{}'.format(self.cal_source.lower())

        # run IDL procedure
        idl_cmd = '''idl -e "{}, '{}'"'''.format(pro, os.path.join(self.relative_path, self.cal_filename))
        idl(idl_cmd)

    def get_cal_arrays(self, use = True):
        '''reads fits files generated by self.to_natural and returns a dictionary of relevant information'''

        cal_arrays = {} # will be keyed by color term
        to_retrieve = ['RA', 'DEC', 'B', 'EB', 'V', 'EV', 'R', 'ER', 'I', 'EI', 'CLEAR', 'ECLEAR']

        for cterm in ['kait1', 'kait2', 'kait3', 'kait4', 'nickel1', 'nickel1', 'Landolt']:
            if ('kait' in cterm) or ('nickel' in cterm):
                ct = cterm + '_natural'
            else:
                ct = cterm + '_standard'
            if use is True:
                use = '_use'
            else:
                use = ''
            with fits.open(os.path.join(self.relative_path, 'cal_{}_{}{}_{}.fit'.format(self.targetname, self.cal_source, use, ct))) as f:
                cal = f[1].data
                tmp = {}
                for key in to_retrieve:
                    tmp[key] = cal[key].byteswap().newbyteorder()
                cal_arrays[cterm] = pd.DataFrame(tmp)

        return cal_arrays

# provide script functionality via
# python astroCatalog.py name ra dec
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str, help='name of the object')
    parser.add_argument('ra', type=float, help='decimal RA of the object')
    parser.add_argument('dec', type=float, help='decimal DEC of the object')
    parser.add_argument('-s', '--source', dest='source', type=str, default = 'None', help='use specified source (default attempt order: PS1 > SDSS > APASS)')
    args = parser.parse_args()

    c = astroCatalog(args.name, args.ra, args.dec)
    if args.source.upper() == 'PS1':
        c.PS1_get_calib()
    elif args.source.upper() == 'SDSS':
        c.SDSS_get_calib()
    elif args.source.upper() == 'APASS':
        c.APASS_get_calib()
    else:
        c.get_cal()
    print('\ncalibration stars extracted from: {}'.format(c.cal_source))
    print('converting to natural system...\n')
    c.to_natural()
