# standard package imports
import copy
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def onpick(event, df, drop_dict, filt, cut, fig, offset):
    '''
    Handles click events by plot_lc.

    Parameters
    ----------
    event : matplotlib click event
    df : pandas.DataFrame
        internal light curve format with non-null magnitude values in 'filt'
    drop_dict : dict
        dict of format filt: [<indices to be cut from df>]
    cut : matplotlib plot instance
        plot to add cut points to
    fig : matplotlib figure
        figure instance
    offset : int or float
        (filter dependent) magnitude offset
    '''

    # get index of event and use it to add appropriate id to drop_dict
    ind = event.ind[0]
    drop_dict[filt].append(df.index[ind])

    # plot the location
    x = df['t_rel'].loc[drop_dict[filt]]
    y = df[filt].loc[drop_dict[filt]] + offset
    cut.set_data(x, y)
    fig.canvas.draw()

class plotLC:
    '''Light curve plotting for LOSSPhotPypeline outputs'''

    def __init__(self, lc = None, lc_raw = None, lc_file = None, tref = 'min', filters = ('B','V','R','I','CLEAR'), 
                 offset_scale = 1, style = 'white', context = 'notebook', name = None, photmethod = None):
        '''
        instantiation instructions

        Parameters
        ----------
        lc : pandas.DataFrame, optional, default: None
            internal representation of light curve
            must have columns: MJD, B, EB, V, EV, R, ER, I, EI, CLEAR, ECLEAR
        lc_raw : pandas.DataFrame, optional, default: None
            dataframe in "raw" light curve format
        lc_file : str, optional, default: None
            name of file containing light curve to plot
        tref : int or float, optional, default: 'min'
            time to reference all others to
        filters : iterable, optional, default: ('B','V','R','I','CLEAR')
            photometric passbands to plot
        offset_scale : int or float, optional, default: 1
            multiplicative factor to set magnitude offset scale
        style : str, optional, default: 'white'
            seaborn plot style to use
        context : str, optional, default: 'notebook'
            seaborn context to use
        name : str, optional, default: None
            name of object
        photmethod : str, optional, default: None
            photometry method used in generating light curve
        '''

        self.lc = lc
        self.raw = lc_raw
        self.lc_file = lc_file
        self.tref = tref
        self.offset_scale = offset_scale
        self.style = style
        self.context = context
        self.name = name
        self.photmethod = photmethod

        self.tset = False
        self.lc_cut = None

        filters = [filt.upper() for filt in filters]
        if set(filters).issubset(('B','V','R','I','CLEAR')) is False:
            print('provided filter set is not supported, exiting')
            return
        self.filters = filters

        if (self.lc is None) and (self.raw is None) and (self.lc_file is not None):
            self.load_lc(self.lc_file)
            self._set_t()

    def _color(self, filt):
        '''returns color to plot for given filter'''
        if filt == 'B':
            return 'blue'
        elif filt == 'V':
            return 'green'
        elif filt == 'R':
            return 'red'
        elif filt == 'I':
            return 'darkred'
        else:
            return 'black'

    def _offset(self, filt):
        '''returns magnitude offset for given filter'''
        if filt == 'B':
            return 2*self.offset_scale
        elif filt == 'V':
            return 1*self.offset_scale
        elif filt == 'R':
            return 0*self.offset_scale
        elif filt == 'I':
            return -1*self.offset_scale
        else:
            return 0*self.offset_scale

    def _set_t(self):
        '''set time relative to reference'''
        if self.tref == 'min':
            self.tref = self.lc['MJD'].min()
        if self.lc is not None:
            self.lc['t_rel'] = self.lc['MJD'] - self.tref
            self.tset = True
        else:
            print('no lc to set t_rel for, exiting')
            return

    def _transform_raw(self):
        '''transforms dataframe of light curve in raw format to internal format'''
        df = self.raw
        df['err'] = (df['+emag'] - df['-emag']) / 2
        self.lc = pd.concat([df[df['filter'].str.upper() == filt][['mjd', 'mag','err']].set_axis(['MJD', filt, 'E' + filt], axis = 'columns', inplace = False)
                             for filt in self.filters], sort = False)

    def _load_raw(self, lc_file):
        '''loads "raw" light curves generated by LOSSPhotPypeline.pipeline.LPP'''
        if 'raw' not in lc_file:
            print('{} must have "raw" in its name, exiting.'.format(lc_file))
            return
        df = pd.read_csv(lc_file, delim_whitespace = True, comment = ';',
                         names = ('mjd', 'etburst', 'mag', '-emag', '+emag', 'limmag', 'filter', 'imagename'))
        self.raw = df # is a copy needed here?
        self._transform_raw()

    def _load_standard(self, lc_file):
        '''loads "standard" light curves generated by LOSSPhotPypeline.pipeline.LPP'''
        if 'standard' not in lc_file:
            print('{} must have "standard" in its name, exiting.'.format(lc_file))
            return
        self.lc = pd.read_csv(lc_file, delim_whitespace = True, usecols = (1,3,4,5,6,7,8,9,10,11,12))

    def load_lc(self, lc_file):
        '''
        Interprets the supplied light curve file and loads appropriately.

        Parameters
        ----------
        lc_file : str
            name of file containing light curve
            should either be a "raw" or "standard" file for LOSSPhotPypeline
        '''

        if 'raw' in lc_file:
            self._load_raw(lc_file)
        elif 'standard' in lc_file:
            self._load_standard(lc_file)
        else:
            print('{} is an unrecognized light curve format, exiting')
            return

    def _drop_lc_points(self, drop_dict):
        '''copy lc and then set all elements specified by dropdict to NaN'''
        self.lc_cut = copy.deepcopy(self.lc)
        for filt in drop_dict.keys():
            self.lc_cut.loc[drop_dict[filt], filt] = np.nan

    def _setup_plot(self):
        '''does some of the bookkeeping needed to set up light curve plots'''
        fig, ax = plt.subplots(1,1)
        ax.invert_yaxis()
        ax.set_xlabel('Time (MJD - {:.1f})'.format(self.tref))
        ax.set_ylabel('Mag')
        if self.name is not None:
            title_msg = self.name
            if self.photmethod is not None:
                title_msg += ' ({})'.format(self.photmethod)
            ax.set_title(title_msg)
        return fig, ax

    def plot_lc(self, lc = None, style = None, context = None, return_fig = False, icut = False):
        '''
        Plots light curve.

        Parameters
        ----------
        lc : light curve in internal format, optional, default : None
            light curve to plot
        style : str, optional, default: 'white'
            seaborn plot style to use
        context : str, optional, default: 'notebook'
            seaborn context to use
        return_fig : bool, optional, default : False
            return figure and axes if True
        icut : bool, optional, default: False
            run interactive point cutting
        '''

        # set plot attributes
        if style is None:
            style = self.style
        if context is None:
            context = self.context
        sns.set_style(style)
        sns.set_context(context)

        if lc is None:
            lc = self.lc

        if self.tset is False:
            self._set_t()

        if icut is False:
            fig, ax = self._setup_plot()
        else:
            drop_dict = {filt: [] for filt in self.filters}

        # iterate through filters to generate light curves
        for filt in self.filters:

            if icut is True:
                fig, ax = self._setup_plot()

            # get non-null points in current passband
            tmp = lc[self.lc[filt].notnull()]

            # bookkeeping for current passband
            offset = self._offset(filt)
            sgn = '+'
            if offset < 0:
                sgn = '-'

            # plot light curve
            errobj = ax.errorbar(tmp['t_rel'], tmp[filt] + self._offset(filt), yerr = tmp['E' + filt], fmt = '.', elinewidth = 1, capsize = 2,
                                 capthick = 1, c = self._color(filt), label = '{} {} {}'.format(filt, sgn, abs(offset)), picker = 3)

            # handle selection of bad points
            if icut is True:
                cut, = ax.plot([], [], 'rX', markersize = 10, label = 'points to cut')
                ax.legend()
                plt.ion()
                cid = fig.canvas.mpl_connect('pick_event', lambda event: onpick(event, tmp, drop_dict, filt, cut, fig, offset))
                fig.show()
                input('hit [return] when done selection bad points in {} band > '.format(filt))
                fig.canvas.mpl_disconnect(cid)
                plt.ioff()
                plt.close()
                continue

        if icut is True:
            self._drop_lc_points(drop_dict)
            self.plot_lc(lc = self.lc_cut)
        else:
            ax.legend()
            if return_fig:
                return fig, ax
            else:
                plt.savefig('{}.ps'.format(self.lc_file.split('.dat')[0]), bbox_inches = 'tight')
