# standard imports
from astropy.io import fits
from astropy.time import Time
from astropy import wcs
import numpy as np
import os
import re
import math
import sewpy
import inspect

# internal imports
import LOSSPhotPypeline
from LOSSPhotPypeline.image.FileNames import FileNames

class FitsImage(object):
    '''basic fits image handling'''

    def __init__(self, name):
        '''instantiation instructions'''

        self.oriname=name
        self.name=os.path.basename(name)

        # open fits file        
        hdulist=fits.open(self.oriname)
        hdulist[0].verify('fix+ignore')
        self.header = hdulist[0].header
        hdulist.close()

        # basic information
        self.telescope=''
        self.object='Unk'
        self.idname='unk'
        self.pixscale=0.0
        self.day=''
        self.month=''
        self.year=''
        self.hour=''
        self.minute=''
        self.second=''
        self.mjd=0.0
        self.jd=0.0
        self.Xsize=0
        self.Ysize=0
        self.exptime=0.0
        self.filter=''
        self.basename=''
        self.uniformname=''
        self.savepath=''

        # WCS information
        self.WCSED='F'
        self.centerRa=0.0
        self.centerDec=0.0
        self.corner1Ra=0.0
        self.corner1Dec=0.0
        self.corner2Ra=0.0
        self.corner2Dec=0.0
        self.corner3Ra=0.0
        self.corner3Dec=0.0
        self.corner4Ra=0.0
        self.corner4Dec=0.0

        # color term
        self.color_term = None

        self.extract_info()
        self.get_color_term()

    def extract_info(self):
        '''extract basic fits information'''

        header = self.header

        if 'TELESCOP' in header:
            telescope=header["TELESCOP"]
        elif 'VERSION' in header:
            telescope=header["VERSION"]
        elif 'INSTRUME' in header:
            telescope=header["INSTRUME"]
        else :
            telescope='Unknown'
        telescope=telescope.replace(' ','')
        telescope=telescope.replace("'",'')

        if telescope == "K.A.I.T.":
            self.telescope="kait"
            self.pixscale=0.7965
            date=header["DATE-OBS"]
            uttime=header["UT"]
            self.day=date[0:2]
            self.month=date[3:5]
            self.year=date[6:10]
            self.hour=uttime[0:2]
            self.minute=uttime[3:5]
            self.second=uttime[6:8]
            self.exptime=header["EXPTIME"]
            self.filter=header["FILTERS"]
            try:
                self.object=header["OBJECT"]
            except KeyError:
                self.object='Unk'
            if 'DATID' in header:
                self.idname=header["DATID"]
            else :
                self.idname='Unk'

        elif ((telescope == "nickel_direct") or (telescope == "nickel_spectrograph") or (telescope == "NickelSpectrograph") or 
              (telescope == "NICKEL") or( telescope == "1M-CASS")):
            self.telescope="Nickel"
            self.pixscale=0.37000
            # CCD header seems changed, noted on Aug. 12, 2015
            if 'DATE-STA' in header:
                date=header["DATE-STA"]
                uttime=header["DATE-STA"]
                self.day=date[8:10]
                self.month=date[5:7]
                self.year=date[0:4]
                self.hour=uttime[11:13]
                self.minute=uttime[14:16]
                self.second=uttime[17:19]
                self.exptime=header["EXPTIME"]
            elif 'DATE-BEG' in header:
                date=header["DATE-BEG"]
                uttime=header["DATE-BEG"]
                self.day=date[8:10]
                self.month=date[5:7]
                self.year=date[0:4]
                self.hour=uttime[11:13]
                self.minute=uttime[14:16]
                self.second=uttime[17:19]
                self.exptime=header["EXPTIME"]
            elif 'DATE-OBS' in header:
                date=header["DATE-OBS"]
                uttime=header["TIME"]
                # is it really day at first then month? or month at first then day?
                day=int(date.split("/")[0])
                self.day='{:02d}'.format(day)
                month=int(date.split("/")[1])
                self.month='{:02d}'.format(month)
                year=int(date.split("/")[2])
                if year > 80 and year <= 99 :
                    year = year+1900
                if year >= 0 and year <= 50 :
                    year = year+2000
                self.year='{:4d}'.format(year)
                hour=int(uttime.split(":")[0])
                self.hour='{:02d}'.format(hour)
                minute=int(uttime.split(":")[1])
                self.minute='{:02d}'.format(minute)
                second=math.floor(float(uttime.split(":")[2]))
                self.second='{:02d}'.format(second)
                self.exptime=header["EXPTIME"]
            elif 'DATE' in header:
                date=header["DATE"]
                uttime=header["DATE"]
                self.day=date[8:10]
                self.month=date[5:7]
                self.year=date[0:4]
                self.hour=uttime[11:13]
                self.minute=uttime[14:16]
                self.second=uttime[17:19]
                self.exptime=header["EXPTIME"]
            else :
                print('data and uttime not found, check it')
                return

            if 'FILTNAM' in header:
                self.filter=str(header["FILTNAM"])
            elif 'FILTER' in header:
                self.filter=str(header["FILTER"])
            else :
                self.filter='Unk'
            self.object=header["OBJECT"]

            # idname need to get from filename, should be dxxx
            idnametmp=re.split('[._]', self.name)
            if idnametmp[2][0] == 'd' :
                self.idname=idnametmp[2]
            elif idnametmp[3][0] == 'd' :
                self.idname=idnametmp[3]
            else :
                self.idname=idnametmp[1]

        # will add the other telescope when needed
        elif telescope == "P48" :
            self.telescope="P48"
            self.pixscale=1.01214
        elif telescope == "BITRAN-CCDImagingSystem" :
            self.telescope="Koichi"
            self.pixscale=1.44588
        elif telescope == "C14F/6" :
            self.telescope="RonC14"
            self.pixscale=1.26643
        elif telescope == "2m0-01" :
            self.telescope="LCOGT-ogg"
            self.pixscale=0.300741
        elif telescope == "1m0-08" :
            self.telescope="LCOGT-elp"
            self.pixscale=0.46961
        else :
            print("telescope not found in header")
            print("Unknown telescope, need to update the code!!!")
            self.telescope="unknown"

        # For all object, replace space with "-", and also replace "_" with "-"
        self.object=self.object.strip()
        self.object=self.object.replace(' ','-')
        self.object=self.object.replace('_','-')
        self.object=self.object.replace(',','-')
        self.object=self.object.replace(' ','')
        if self.object == '' :
            self.object='Unk'

        # For all filter, delete spaces
        self.filter=self.filter.strip()
        self.filter=self.filter.replace(' ','')
        if self.filter == '' :
            self.filter='Unk'

        self.Xsize=header["NAXIS1"]
        self.Ysize=header["NAXIS2"]

        # get time
        utctime=self.year+'-'+self.month+'-'+self.day+'T'+self.hour+':'+self.minute+':'+self.second
        timetmp=Time(utctime)
        self.mjd=timetmp.mjd
        self.jd=timetmp.jd

        # extract WCS info
        self.extract_wcsinfo()

        # standardize naming
        self.basename=self.object+'_'+self.year+self.month+self.day+'_'+self.hour+self.minute+self.second+'_'+self.idname+'_'+self.telescope+'_'+self.filter
        if self.WCSED == 'T' :
            self.savepath=self.telescope+'/'+self.telescope+'_'+'image_calib_sucess/'+self.year+self.month+self.day+'/'
            self.uniformname=self.basename+'_c.fit'
        else :
            self.savepath=self.telescope+'/'+self.telescope+'_'+'image_calib_failed/'+self.year+self.month+self.day+'/'
            self.uniformname=self.basename+'.fit'

    def extract_wcsinfo(self):
        '''extract WCS information, if no keyword "WCSED"'''

        header = self.header

        if not 'WCSED' in header:
          #print('Warning: this image is not WCSed, no WCSED keyword')
          return
        self.WCSED='T'

        try:
            wcstmp=wcs.WCS(header)
        except wcs._wcs.InvalidTransformError:
            return

        xtmp=[(self.Xsize-1.0)/2.0,0.0,0.0,self.Xsize-1.0,self.Xsize-1.0]
        ytmp=[(self.Ysize-1.0)/2.0,0.0,self.Ysize-1.0,self.Ysize-1.0,0.0]
        ratmp, dectmp=wcstmp.wcs_pix2world(xtmp, ytmp, 1)
        self.centerRa=ratmp[0]
        self.centerDec=dectmp[0]
        self.corner1Ra=ratmp[1]
        self.corner1Dec=dectmp[1]
        self.corner2Ra=ratmp[2]
        self.corner2Dec=dectmp[2]
        self.corner3Ra=ratmp[3]
        self.corner3Dec=dectmp[3]
        self.corner4Ra=ratmp[4]
        self.corner4Dec=dectmp[4]

    def find_wcs_solution(self):
        '''determine WCS solution, it it has not been found already'''

        # rewrite to not need shell scripts...
        header=self.header
        if 'WCSED' in header :
          #print('This image is alread WCSed, no need to do again')
          return
        ##not wcsed, do it
        if self.telescope == 'kait' :
            command="Ssolve-field-kait {0}".format(self.oriname)
            #print(command)
            os.system(command)
            return
        elif self.telescope == 'Nickel' :
            command="Ssolve-field-Nickel {0}".format(self.oriname)
            #print(command)
            os.system(command)
            return
        else :
            print('This method has not been developed yet, please do it!!!')
            return

    def get_color_term(self):
        '''determine the the color term appropriate for the image'''

        # select color term based on telescope and date
        if self.telescope == 'kait':
            tel = 'kait'
            if self.mjd < 51229.0: # mjd of 1999-02-20
                tel += '1'
            elif self.mjd < 52163.0: # mjd of 2001-09-11
                tel += '2'
            elif self.mjd < 54232.0: # mjd of 2007-05-12
                tel += '3'
            else:
                tel += '4'
        elif self.telescope == 'Nickel':
            tel = 'nickel'
            if self.mjd < 54845.0: # mjd of 2009-01-14
                tel += '1'
            else:
                tel += '2'
        else:
            tel = None

        self.color_term = tel

class FitsInfo(FitsImage, FileNames):
    '''measure quantities from fits images'''

    def __init__(self, name):
        '''instantiation instructions'''

        FitsImage.__init__(self,name)
        FileNames.__init__(self, name)

        self.fwhm=0.0
        self.sky=0.0
        self.zeromag=0.0
        self.limitmag=0.0

    def get_fwhm(self, force = False, nominal = 5):
        '''gets fwhm from header or runs SExtractor to determine it if not in header'''

        if 'FWHM' in self.header:
            self.fwhm = self.header['FWHM']

        # skip if already done unless forced to re-calculate
        if (self.fwhm != 0) and (force is False):
            return

        # get paths to needed files
        sxcp = os.path.join(os.path.dirname(inspect.getfile(LOSSPhotPypeline)), 'conf', 'sextractor_config')
        filt = os.path.join(sxcp, 'gauss_2.0_5x5.conv')
        par = os.path.join(sxcp, 'fwhm.par')
        star = os.path.join(sxcp, 'default.nnw')

        # set up configuration dictionary to override SExtractor defaults
        cf = {'PARAMETERS_NAME': par,
              'DETECT_MINAREA': 10,
              'DETECT_THRESH': 3,
              'ANALYSIS_THRESH': 3.5,
              'FILTER_NAME': filt,
              'DEBLEND_MINCOUNT': 0.0001,
              'MASK_TYPE': 'NONE',
              'SATUR_LEVEL': 36000.0,
              'MAG_ZEROPOINT': 25.0,
              'GAIN': 3,
              'PIXEL_SCALE': 0.7965,
              'SEEING_FWHM': 4.17,
              'STARNNW_NAME': star,
              'BACK_SIZE': 8,
              'BACKPHOTO_THICK': 24,
              'WEIGHT_TYPE': 'BACKGROUND',
              'WEIGHT_GAIN': 'Y'}

        # run SExtractor and get results, write nominal val if failed
        sew = sewpy.SEW(config = cf, configfilepath = sxcp)
        res = sew(self.cimg)["table"]
        if len(res) == 0:
            self.fwhm = nominal
        else:
            self.fwhm = np.median(res["FWHM_IMAGE"])

        # if somehow still zero, write nominal value
        if self.fwhm == 0:
            self.fwhm = nominal

        # set in the fits image
        self.write_header('FWHM', self.fwhm)

    def get_zeromag(self):
        '''get zeromag photometry from *zero.txt file generated by lpp_cal_instrumag'''

        if 'ZEROMAG' in self.header:
            self.zero = self.header['ZEROMAG']
        elif os.path.exists(self.zerotxt):
            with open(self.zerotxt, 'r') as f:
                self.zero = float(f.read())
        else:
            print('zero not yet determined, run lpp_cal_instrumag first')

    def get_sky(self):
        '''get sky value from *sky.txt file generated by lpp_phot_psf'''

        if 'SKY' in self.header:
            self.sky = self.header['SKY']
        elif os.path.exists(self.skytxt):
            with open(self.skytxt, 'r') as f:
                self.sky = float(f.read())
        else:
            print('zero not yet determined, run lpp_phot_psf first')

    def calc_limmag(self):
        '''calculate limiting magnitude'''

        if (self.zero != 0) and (self.sky != 0):
           self.limmag = -2.5*np.log10(3*self.sky) + self.zero
        else:
            print('zero and sky are not yet determined, cannot calculate limiting mag')

    def write_header(self, keyword, value):
        '''write header (fits.setval fails, but would do the same thing)'''

        hdul = fits.open(self.oriname, mode = 'update', memmap = False)
        hdul[0].verify('fix+ignore')
        hdul[0].header[keyword] = value
        hdul.flush(output_verify = 'ignore')
        hdul.close()
