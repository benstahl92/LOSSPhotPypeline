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
    if df.index[ind] in drop_dict[filt]:
        drop_dict[filt].remove(df.index[ind])
    else:
        drop_dict[filt].add(df.index[ind])

    # plot the location
    x = df['t_rel'].loc[drop_dict[filt]]
    y = df[filt].loc[drop_dict[filt]] + offset
    cut.set_data(x, y)
    fig.canvas.draw()

class plotLC:
    '''Light curve plotting for LOSSPhotPypeline outputs'''

    def __init__(self, lc = None, lc_raw = None, lc_file = None, lm_file = None, tref = 'min', filters = 'auto', 
                 offset_scale = 1, style = 'white', context = 'notebook', name = None, photmethod = None):
        '''
        instantiation instructions

        Parameters
        ----------
        lc : pandas.DataFrame, optional, default: None
            internal representation of light curve
            must have columns: MJD, <some combination of filter mags and errors
        lc_raw : pandas.DataFrame, optional, default: None
            dataframe in "raw" light curve format
        lc_file : str, optional, default: None
            name of file containing light curve to plot
        lm_file : str, optional, default: None
            name of raw formatted file containing limiting mags to plot
        tref : int or float, optional, default: 'min'
            time to reference all others to
        filters : iterable, optional, default: 'auto'
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
        self.lm_file = lm_file
        self.tref = tref
        self.offset_scale = offset_scale
        self.style = style
        self.context = context
        self.name = name
        self.photmethod = photmethod

        self.tset = False
        self.lc_cut = None

        self.lm = None

        self.all_black = False

        self.filter_ref = ('B','V','R','I','CLEAR')

        if (self.lc is None) and (self.raw is None) and (self.lc_file is not None):
            self.load_lc(self.lc_file)
            self._set_t()

        if self.lm_file is not None:
            self.load_lm(self.lm_file)


        if filters == 'auto':
            self._get_filters()
        else:
            filters = [filt.upper() for filt in filters]
            if set(filters).issubset(self.filter_ref) is False:
                print('provided filter set is not supported, exiting')
                return
            self.filters = filters

    def _color(self, filt):
        '''returns color to plot for given filter'''
        if self.all_black:
            return 'black'
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

    def _marker(self, filt):
        '''returns marker to use for given filter'''
        if 'raw' in self.lc_file:
            return 'o'
        if filt == 'B':
            return '^'
        elif filt == 'V':
            return 'D'
        elif filt == 'R':
            return 's'
        elif filt == 'I':
            return 'v'
        else:
            return 'o'

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
                             for filt in self.filter_ref], sort = False)

    def _load_raw(self, lc_file):
        '''loads "raw" light curves generated by LOSSPhotPypeline.pipeline.LPP'''
        if 'raw' not in lc_file:
            print('{} must have "raw" in its name, exiting.'.format(lc_file))
            return
        df = pd.read_csv(lc_file, delim_whitespace = True, comment = ';',
                         names = ('mjd', 'etburst', 'mag', '-emag', '+emag', 'limmag', 'filter', 'imagename'))
        self.raw = df
        self._transform_raw()

    def _load_lm(self, lm_file):
        '''loads "raw" light curves generated by LOSSPhotPypeline.pipeline.LPP'''
        df = pd.read_csv(lc_file, delim_whitespace = True, comment = ';',
                         names = ('mjd', 'etburst', 'mag', '-emag', '+emag', 'limmag', 'filter', 'imagename'))
        self.lm = pd.concat([df[df['filter'].str.upper() == filt][['mjd', 'limmag']].set_axis(['MJD', filt, 'E' + filt], axis = 'columns', inplace = False)
                             for filt in self.filter_ref], sort = False)
        self.lm['t_rel'] = self.lm['MJD'] - self.tref

    def _load_standard(self, lc_file):
        '''loads "standard" light curves generated by LOSSPhotPypeline.pipeline.LPP'''
        if ('standard' not in lc_file) and ('group' not in lc_file):
            print('{} must have "standard" in its name, exiting.'.format(lc_file))
            return
        self.lc = pd.read_csv(lc_file, delim_whitespace = True)

    def _load_cut(self, lc_file):
        '''loads "cut" light curves generated with icut mode'''
        if 'cut' not in lc_file:
            print('{} must have "cut" in its name, exiting.'.format(lc_file))
            return
        self.lc = pd.read_csv(lc_file, delim_whitespace = True)

    def load_lc(self, lc_file):
        '''
        Interprets the supplied light curve file and loads appropriately.

        Parameters
        ----------
        lc_file : str
            name of file containing light curve
            should either be a "raw" or "standard" file for LOSSPhotPypeline
        '''
        if ('standard' in lc_file) or ('group' in lc_file):
            self._load_standard(lc_file)
        elif 'raw' in lc_file:
            self._load_raw(lc_file)
        else:
            print('{} is an unrecognized light curve format, exiting')
            return

    def _get_filters(self):
        '''determine filters from light curve (only filters with at least one NaN)'''

        # get lc data
        if self.lc is not None:
            tmp = self.lc.dropna(axis = 1, how = 'all')
        else:
            return

        # extract filters and then sort
        self.filters = list(pd.Series(self.filter_ref).loc[pd.Series(self.filter_ref).isin(tmp.columns)])
        self.filters.sort(key = lambda x: self.filter_ref.index(x))

    def _drop_lc_points(self, drop_dict):
        '''copy lc and then set all elements specified by dropdict to NaN'''
        self.lc_cut = copy.deepcopy(self.lc)
        for filt in drop_dict.keys():
            self.lc_cut.loc[list(drop_dict[filt]), filt] = np.nan
        self.drop_dict = drop_dict

    def write_cut_lc(self, fname = None):
        '''write cut lc to file of same format that it was read from'''

        if fname is None:
            fname = self.lc_file#.replace('.dat', '_cut.dat')
        if self.raw is None: # it was a "standard" file
            cols = self.lc_cut.columns[self.lc_cut.columns != 't_rel']
            self.lc_cut.to_csv(fname, sep = '\t', na_rep = 'NaN', index = False, columns = cols)
        else:
            df = copy.deepcopy(self.raw.drop('err', axis = 1))
            df.columns = (';; MJD','etburst', 'mag', '-emag', '+emag', 'limmag', 'filter', 'imagename')
            for filt in self.drop_dict.keys():
                df.loc[(df['filter'].str.upper() == filt) & (df[';; MJD'].isin(self.lc.loc[self.drop_dict[filt],'MJD'])), ['mag','-emag','+emag']] = np.nan
            self.raw_cut = df
            self.raw_cut.to_csv(fname, sep = '\t', na_rep = 'NaN', index = False, float_format='%9.5f')

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
        elif self.lc_file is not None:
            ax.set_title(self.lc_file)
        return fig, ax

    def plot_lc(self, lc = None, style = None, context = None, return_fig = False, icut = False, magerr_cut = 2,
                fname = None, extensions = ['.png']):
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
        magerr_cut : int or float, optional, default: 2
            cutoff on magnitude error above which points are cut (forced if icut is False, proposed otherwise)
        fname : str, optional, default: None
            name of file to write plot to
        extensions : list, optional: default: ['.png']
            extensions to write image files
        '''

        # check if there is data to plot and return if not
        #if len(self.lc.loc[self.lc['B'].notnull(), :]) == 0:
        #if len(self.lc.iloc[np.any(self.lc.loc[:, ['B','V','R','I','CLEAR']].notnull(), axis = 1)]) == 0:
        if len(self.filters) == 0:
            print('no data to plot')
            return None

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
            drop_dict = {filt: set() for filt in self.filters}

        # iterate through filters to generate light curves
        for filt in self.filters:

            # get non-null points in current passband
            tmp = lc[lc[filt].notnull()]
            if self.lm is not None:
                tmplm = self.lm[self.lm[filt].notnull()]

            if (magerr_cut is None) or (magerr_cut is False):
                ob = tmp['E' + filt] > np.inf
            else:
                ob = tmp['E' + filt] > magerr_cut
            outliers = tmp.index[ob]

            # bookkeeping for current passband
            offset = self._offset(filt)
            sgn = '+'
            if offset < 0:
                sgn = '-'

            # plot light curve
            if icut is True:
                fig, ax = self._setup_plot()
                errobj = ax.errorbar(tmp['t_rel'], tmp[filt] + self._offset(filt), yerr = tmp['E' + filt], fmt = '.', elinewidth = 1, marker = self._marker(filt),
                                     c = self._color(filt), label = '{} {} {}'.format(filt, sgn, abs(offset)), picker = 3)
            else:
                errobj = ax.errorbar(tmp.loc[~ob,'t_rel'], tmp.loc[~ob,filt] + self._offset(filt), yerr = tmp.loc[~ob,'E' + filt], marker = self._marker(filt),
                                     fmt = '.', elinewidth = 1, c = self._color(filt), label = '{} {} {}'.format(filt, sgn, abs(offset)))

            ax.plot(tmplm['t_rel'], tmplm[filt] + self._offset(filt), '\u2193', c = self._color(filt))

            # handle selection of bad points
            if icut is True:
                drop_dict[filt].update(outliers)
                cut, = ax.plot(tmp['t_rel'].loc[drop_dict[filt]], tmp[filt].loc[drop_dict[filt]] + offset, 'rX', markersize = 10, label = 'points to cut')
                ax.legend(bbox_to_anchor = (1.01, 0.5), loc = 'center left')
                box = ax.get_position()
                ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
                plt.ion()
                cid = fig.canvas.mpl_connect('pick_event', lambda event: onpick(event, tmp, drop_dict, filt, cut, fig, offset))
                fig.show()
                input('click to (un)select points for removal from {} band [hit "enter" when done] '.format(filt))
                fig.canvas.mpl_disconnect(cid)
                plt.ioff()
                plt.clf()
                plt.close()
                continue

        # make plot square
        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()
        ax.set_aspect(np.abs((x1-x0)/(y1-y0)))

        if icut is True:
            self._drop_lc_points(drop_dict)
            self.write_cut_lc()
            # get name of images to cut
            if self.raw is not None:
                images = []
                for filt in drop_dict.keys():
                    images.extend(list(self.raw.loc[drop_dict[filt], 'imagename']))
            else:
                images = None
            return images
            #self.plot_lc(lc = self.lc_cut, magerr_cut = False, extensions = ['_cut{}'.format(ext) for ext in extensions])
        else:
            # workaround for bugs with the legend
            handles, labels = ax.get_legend_handles_labels()
            handles = [h[0] for h in handles]
            ax.legend(handles, labels, bbox_to_anchor = (1.01, 0.5), loc = 'center left')
            if return_fig:
                return fig, ax
            else:
                if fname is None:
                    for ext in extensions:
                        fname = self.lc_file.replace('.dat', ext)
                        plt.savefig(fname, bbox_inches = 'tight')
                else:
                    plt.savefig(fname, bbox_inches = 'tight')
                plt.clf()
                plt.close()
