pro lpp_phot_apt,image,fwhm=fwhm,exposures=exposures,savesky=savesky,output=output

if n_params() eq 0 then begin
  print,'syntax - LPP_phot_apt,image,fwhm=fwhm,exposures=exposures,savesky=savesky'
  return
endif

if not keyword_set(exposures) then exposures=1.0
starttime=systime(1)

lpp_image_name_trans,image,imagest

fi=findfile(image)

if fi[0] eq '' then begin
  print,'file : ',image,' not found, quit!'
  return
endif

if not keyword_set(fwhm) then begin
  ;;no fwhm is given, need to look into the .fwhm file
  ff=findfile(imagest.fwhm)
  if ff[0] eq '' then begin
    print,'file : ',imagest.fwhm,' not found, quit!'
    return
  endif
  readcol,imagest.fwhm,fwhm
  fwhm=fwhm[0]
endif
if fwhm le 0 then begin
  print,'fwhm is 0 or below 0, wrong value, please check'
  return
endif
if keyword_set(output) then begin
  print,'fwhm is: ',fwhm,' pixel'
endif

fo=findfile(imagest.obj)
if fo[0] eq '' then begin
  print,'file : ',imagest.obj,' not found, quit!'
  return
endif

readcol,imagest.obj,objx,objy
;;;Note, in IDL, this value need -1
objx=objx-1.0
objy=objy-1.0
print,objx,objy

;;OK, all prepared, can proceed

;; first, find the image size
;imhdr=headfits(image)
imagedata=mrdfits(image,0,imhdr)
maxX=float(sxpar(imhdr,'NAXIS1'))
maxY=float(sxpar(imhdr,'NAXIS2'))
;print,maxX,maxY

;; recentroid objects
w=where(objx gt fwhm and objy gt fwhm $
        and objx lt maxX-fwhm-1 and objy lt maxY-fwhm-1)
gcntrd,imagedata,objx[w],objy[w],xcen,ycen,fwhm ;;;,maxgood=ims.satcounts
objx[w]=xcen
objy[w]=ycen
print,objx,objy
w=where(xcen ne -1.0 and ycen ne -1.0,nw)
if nw eq 0 then begin
    print,'*****************************'
    print,'No good objects found near target!?!?!?'
    print,'*****************************'
    return
endif

;;good, to here, we have object can do aperture photometry
apt_radius=[3.5,5.0,7.0,9.0,1.0*fwhm,1.5*fwhm,2.0*fwhm]
nphot=n_elements(apt_radius)
nobj=n_elements(objx)
fluxall=fltarr(nobj,nphot)
fluxerrall=fltarr(nobj,nphot)
magall=fltarr(nobj,nphot)
magerrall=fltarr(nobj,nphot)
magall[*]=!values.d_nan
magerrall[*]=!values.d_nan
for i=0,nphot-1 do begin
  lpp_get_aper_counts,imagedata,fwhm,objx,objy,flux,eflux,radius=apt_radius[i],skynoise=skynoise
  ;print,flux,eflux
  fluxall[*,i]=flux
  fluxerrall[*,i]=eflux
end
if keyword_set(output) then begin
  print,fluxall
endif

;;transform count to mag, use zero point of 25.0
;;this is improtatn, because later we also need this information to calculat the sky noise
;;and then limiting magnitude.
for i=0,n_elements(fluxall)-1 do begin
if fluxall[i] gt 0 then begin
  magall[i]=-2.5*alog10(fluxall[i]/exposures)+25.0
  if finite(fluxerrall[i]) eq 1 then begin
    emagptmp=-2.5*alog10((fluxall[i]-fluxerrall[i])/exposures)+25.0
    emagmtmp=-2.5*alog10((fluxall[i]+fluxerrall[i])/exposures)+25.0
    magerrall[i]=(emagptmp-emagmtmp)/2.0
  endif else begin
    taremag=0.50
  endelse
endif
endfor

;print,magall,magerrall

;;write the out put to the text file
openw,lun,imagest.apt,/get_lun
printf,lun,';;id   ximage   yimage    3.5p   err    5.0p   err    7.0p   err    9.0p   err   1.0fh   err   1.5fh   err   2.0fh   err'
;;note x,y need plus 1.0
for i=0,nobj-1 do begin
  printf,lun,i+1,objx[i]+1.0,objy[i]+1.0,magall[i,0],magerrall[i,0],magall[i,1],magerrall[i,1],magall[i,2],magerrall[i,2],magall[i,3],magerrall[i,3],magall[i,4],magerrall[i,4],magall[i,5],magerrall[i,5],magall[i,6],magerrall[i,6],format='(i4,f9.2,f9.2,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3)'
endfor
close,lun
free_lun,lun

;;write the sky if savesky keyword is set
if keyword_set(savesky) then begin
  openw,lun,imagest.sky,/get_lun
  ;;note here the skynoise was divided by exposures too, in order to make it
  ;;consistent with stars count for calculating the right magnitudes.
  printf,lun,skynoise/exposures
  close,lun
  free_lun,lun
endif

if keyword_set(output) then begin
  print,systime(1)-starttime,format='("photometry took ",f5.2," seconds")'
endif
end
