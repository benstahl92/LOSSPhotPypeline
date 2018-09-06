from astropy.io import fits
from astropy.time import Time
from astropy import wcs
import os
import re
import math

class FitsImage(object):
    def __init__(self,name):
        #print(name)
        self.oriname=name
        self.name=os.path.basename(name)
        ## in initializing, check if image exist or not, if not, returen error
        ## TBD, need to complete
        self.hdulist=fits.open(self.oriname)
        self.hdulist[0].verify('fix')
        ## the following fields are the basic fits information
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
        ## the following fields are the WCS information
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
        ## in default, call the following function
        self.extract_info()

    ##this method extract the basic fits information
    def extract_info(self):
        #print(self.name)
        ##header=fits.getheader(self.name,0)
        ##strange, this usage will have error when get "FILTERS", change to use hdulist
        header=self.hdulist[0].header
        if 'TELESCOP' in header:
            telescope=header["TELESCOP"]
        elif 'VERSION' in header:
            telescope=header["VERSION"]
        elif 'INSTRUME' in header:
            telescope=header["INSTRUME"]
        else :
            telescope='Unknown'
        #print(telescope)
        ##delete all the blank space
        telescope=telescope.replace(' ','')
        telescope=telescope.replace("'",'')
        #print("telescopete is : ",telescope)
        ##I need swith case structure to determine which telescope it is, for now just use if elif else
        if telescope == "K.A.I.T." :
            self.telescope="kait"
            self.pixscale=0.7965
            date=header["DATE-OBS"]
            uttime=header["UT"]
            #print(date,uttime)
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
            #print(self.exptime,self.filter)
        elif telescope == "nickel_direct" or telescope == "nickel_spectrograph" or telescope == "NickelSpectrograph" or telescope == "NICKEL" or telescope == "1M-CASS" :
            self.telescope="Nickel"
            self.pixscale=0.37000
            ##CCD header seems changed, noted on Aug. 12, 2015
            if 'DATE-STA' in header:
                date=header["DATE-STA"]
                uttime=header["DATE-STA"]
                #print(date,uttime)
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
                #print(date,uttime)
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
                #print(date,uttime)
                ##is it really day at first then month? or month at first then day?
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
                #print(date,uttime)
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
            #idname need to get from filename, should be dxxx
            #self.idname=header["DATID"]
            idnametmp=re.split('[._]',self.name)
            if idnametmp[2][0] == 'd' :
                self.idname=idnametmp[2]
            elif idnametmp[3][0] == 'd' :
                self.idname=idnametmp[3]
            else :
                self.idname=idnametmp[1]
        ##Will add the other telescope when needed
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
            print("not find telescope in header")
            print("Unknown telescope, need update the code!!!")
            self.telescope="unknown"
        ###For all object, replace space with "-", and also replace "_" with "-"
        self.object=self.object.strip()
        self.object=self.object.replace(' ','-')
        self.object=self.object.replace('_','-')
        self.object=self.object.replace(',','-')
        self.object=self.object.replace(' ','')
        if self.object == '' :
            self.object='Unk'

        ###For all filter, delete spaces
        self.filter=self.filter.strip()
        self.filter=self.filter.replace(' ','')
        if self.filter == '' :
            self.filter='Unk'

        self.Xsize=header["NAXIS1"]
        self.Ysize=header["NAXIS2"]
        ##need to calculate mjd, jd etc.
        utctime=self.year+'-'+self.month+'-'+self.day+'T'+self.hour+':'+self.minute+':'+self.second
        #print("UT time is: ",utctime)
        timetmp=Time(utctime)
        self.mjd=timetmp.mjd
        self.jd=timetmp.jd

        ##change the ugriz filter to SU, SG, SR, SI, SZ
        ##TBD, maybe no need of this
        ##here, don't do this, beacuse the filter will go to the filename
        #if self.filter == 'u' :
        #    self.filter = 'SU'
        #if self.filter == 'g' :
        #    self.filter = 'SG'
        #if self.filter == 'r' :
        #    self.filter = 'SR'
        #if self.filter == 'i' :
        #    self.filter = 'SI'
        #if self.filter == 'z' :
        #    self.filter = 'SZ'

        ##And in default, also extrac wcs info
        self.extract_wcsinfo()

        ##get the uniform file name
        self.basename=self.object+'_'+self.year+self.month+self.day+'_'+self.hour+self.minute+self.second+'_'+self.idname+'_'+self.telescope+'_'+self.filter
        if self.WCSED == 'T' :
            self.savepath=self.telescope+'/'+self.telescope+'_'+'image_calib_sucess/'+self.year+self.month+self.day+'/'
            self.uniformname=self.basename+'_c.fit'
        else :
            self.savepath=self.telescope+'/'+self.telescope+'_'+'image_calib_failed/'+self.year+self.month+self.day+'/'
            self.uniformname=self.basename+'.fit'


    ##this method extract the wcs information. Assuming images have already been wcsed, with keyword "WCSED"
    def extract_wcsinfo(self):
        header=self.hdulist[0].header
        if not 'WCSED' in header :
          #print('Warning: this image is not WCSed, no WCSED keywrod')
          return
        ##Yes it's wcsed, extrac wcs
        self.WCSED='T'
        ##This part need to verify they are right
        try:
            wcstmp=wcs.WCS(header)
        ##need to find out what's error of this
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

    ##this method extract the wcs information. Assuming images have already been wcsed, with keyword "WCSED"
    def find_wcs_solution(self):
        header=self.hdulist[0].header
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

class FitsInfo(FitsImage):
    def __init__(self,name):
        FitsImage.__init__(self,name)
        self.fwhm=0.0
        self.sky=0.0
        self.zeromag=0.0
        self.limitmag=0.0

    ##this method do the job to get the zeromag photometry
    def find_zeromag(self):
        if self.WCSED != 'T' :
            print('This image is not WCSed, can not do findzero mag, quiting...')
            return 0
        ##for now execute the shell commmand to complete the procedure
        print("zaphot_find_zero_mag.sh ",self.oriname)
        os.system("zaphot_find_zero_mag.sh %s" % self.oriname)

    ##this method extract the phot information.
    def extract_zeromagphotinfo(self):
        header=self.hdulist[0].header
        if not 'ZEROMAG' in header :
          print('Image need to do photometry first')
          print('Doing it now')
          self.find_zeromag()
          self.__init__(self.oriname)
        ##Yes it's zeromaged, extrac photinfo
        ##hdulist has been reloaded now
        header=self.hdulist[0].header
        try:
            self.fwhm=header["FWHM"]
        except KeyError:
            self.fwhm=0.0
        if not isinstance(self.fwhm,(int,float)) :
            self.fwhm = 0.0
        try:
            self.sky=header["SKY"]
        except KeyError:
            self.sky=0.0
        if not isinstance(self.sky,(int,float)) :
            self.sky = 0.0
        try:
            self.zeromag=header["ZEROMAG"]
        except KeyError:
            self.zeromag=0.0
        if not isinstance(self.zeromag,(int,float)) :
            self.zeromag = 0.0
        ##need to calculate the limiting mag
        #self.limitmag=-2.5*alog10(self.sky)+self.zeromag
        try:
            self.limitmag=header["LIMITMAG"]
        except KeyError:
            self.limitmag=0.0
        if not isinstance(self.limitmag,(int,float)) :
            self.limitmag = 0.0

    ##this method get all the necessary information to add into the database
    def get_databaseinfo(self):
        dbinfo={
        ## the following fields are the basic fits information
        ##'oriname'     : self.oriname,
        'basename'    : self.basename,
        'name'        : self.name,
        'telescope'   : self.telescope,
        'pixscale'    : self.pixscale,
        'day'         : self.day,
        'month'       : self.month,
        'year'        : self.year,
        'hour'        : self.hour,
        'minute'      : self.minute,
        'second'      : self.second,
        'mjd'         : self.mjd,
        'jd'          : self.jd,
        'Xsize'       : self.Xsize,
        'Ysize'       : self.Ysize,
        'exptime'     : self.exptime,
        'filter'      : self.filter,
        'uniformname' : self.uniformname,
        'savepath'    : self.savepath,
        ## the following fields are the WCS information
        'WCSED'       : self.WCSED,
        'centerRa'    : self.centerRa,
        'centerDec'   : self.centerDec,
        'corner1Ra'   : self.corner1Ra,
        'corner1Dec'  : self.corner1Dec,
        'corner2Ra'   : self.corner2Ra,
        'corner2Dec'  : self.corner2Dec,
        'corner3Ra'   : self.corner3Ra,
        'corner3Dec'  : self.corner3Dec,
        'corner4Ra'   : self.corner4Ra,
        'corner4Dec'  : self.corner4Dec,
        ## the following fields are the phot information
        'fwhm'        : self.fwhm,
        'sky'         : self.sky,
        'zeromag'     : self.zeromag,
        'limitmag'    : self.limitmag,
        'objname'     : self.object,
        }
        return dbinfo