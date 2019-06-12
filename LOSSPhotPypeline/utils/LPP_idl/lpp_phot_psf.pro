pro lpp_phot_psf,image,fwhm=fwhm,exposures=exposures,savesky=savesky,ccdronoise=ccdronoise,ccdgain=ccdgain,photsub=photsub,output=output,forcesky=forcesky

!quiet = 1
!except = 0

if n_params() eq 0 then begin
  print,'syntax - LPP_phot_psf,image,fwhm=fwhm,exposures=exposures,savesky=savesky'
  return
endif

if not keyword_set(exposures) then exposures=1.0
if not keyword_set(ccdronoise) then ccdronoise=5.0
if not keyword_set(ccdgain) then ccdgain=1.0
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
  print,'exposure time is: ',exposures
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
;print,'Object stars:'
;print,objx,objy

;;OK, all prepared, can proceed

;; first, find the image size
;imhdr=headfits(image)
;imagedata=mrdfits(image,0,imhdr,/silent)
imagedata=readfits(image,imhdr)
maxX=float(sxpar(imhdr,'NAXIS1'))
maxY=float(sxpar(imhdr,'NAXIS2'))
;print,maxX,maxY

;; recentroid objects
w=where(objx gt fwhm and objy gt fwhm $
        and objx lt maxX-fwhm-1 and objy lt maxY-fwhm-1)
gcntrd,imagedata,objx[w],objy[w],xcen,ycen,fwhm ;;;,maxgood=ims.satcounts
;print,objx,objy
w2=where(xcen ne -1.0 and ycen ne -1.0,nw)
if nw eq 0 then begin
    print,'*****************************'
    print,'No good objects found near target!?!?!?'
    print,'*****************************'
    return
endif
objx[w[w2]]=xcen[w2]
objy[w[w2]]=ycen[w2]

;;good, to here, we have object can do aperture photometry
apt_radius=[3.5,5.0,7.0,9.0,1.0*fwhm,1.5*fwhm,2.0*fwhm]
;;here +1 is for PSF photometry, the last one
nphot=n_elements(apt_radius)+1
nobj=n_elements(objx)
fluxall=fltarr(nobj,nphot)
fluxerrall=fltarr(nobj,nphot)
skynoise=fltarr(nphot)
skys=fltarr(nobj,nphot)
magall=fltarr(nobj,nphot)
magerrall=fltarr(nobj,nphot)
magall[*]=!values.d_nan
magerrall[*]=!values.d_nan

if keyword_set(forcesky) then begin
  forcesky=[median(imagedata),stddev(imagedata),n_elements(imagedata)]
endif

;;for i=0,nphot-1 do begin
;;should use nphot-2, because the last one is PSF phot, not apr phot
for i=0,nphot-2 do begin
  lpp_get_aper_counts,imagedata,fwhm,objx,objy,flux,eflux,radius=apt_radius[i],skynoise=skynoisetmp,skys=skytmp,forcesky=forcesky
  ;print,flux,eflux
  fluxall[*,i]=flux
  print,'measured apt flux in ori image is (i, flux[i])',i,fluxall[0,i]
  fluxerrall[*,i]=eflux
  skys[*,i]=skytmp
  skynoise[i]=skynoisetmp
  print,'skynoise is: ',skynoise[i]
  print,'sky is: ',skys[0,i]
end
;print,fluxall

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
      magerrall[i]=9.99
    endelse
  endif
endfor

;; ***
;; *** get local psf, will select good stars from objx,objy
;; ***

;;use S/N to judege good star or nor, use the 3.5p apr flux

snr=fluxall[*,0]/fluxerrall[*,0]

w=reverse(sort(snr))
nw=n_elements(w)
fail=0
if nw le 1 then begin
    print,'*****************************'
    print,'No good objects found near target!?!?!?'
    print,'*****************************'
    fail=1
endif

;;if succeed then continue
if fail eq 0 then begin
  indtmp=where(snr gt 10,nf)
  if nf le 1 then begin
    indtmp=where(snr gt 5,nf)
    if nf lt 1 then begin
      print,'No good star can be used for make PSF, quiting PSF photometry'
      fail=1
    endif
  endif
endif

if fail eq 0 then begin
  if keyword_set(output) then begin
    print,'found ',nf,' bright stars with high S/N'
  endif
  w=w[0:nf-1]
  nw=n_elements(w)
  
  if nw eq 1 then begin
    wo=w
  endif
  if nw ge 2 then begin
    wo=w[0:nw-1]
  endif
  if nw ge 5 then begin
    wo=w[0:3]
  endif
  if nw ge 10 then begin
    wo=w[1:6]
  endif
  if nw ge 15 then begin
    wo=w[2:9]
  endif
  if nw ge 20 then begin
    wo=w[3:15]
  endif
  if nw ge 30 then begin
    wo=w[4:22]
  endif
  wbak=w  ;;wbak is used if the first time trying psf failed
  
  w=wo
  nw=n_elements(w)
  psfstarx=objx[w]
  psfstary=objy[w]
  psfstarcounts=fluxall[w,0]
  psfstarmags=-2.5*alog10(psfstarcounts)+25
  psfstarskys=skys[w,0]
  inds=lindgen(nw)
  
  if keyword_set(output) then begin
    print,'selected ',n_elements(w),' stars used for calculate PSF!!!'
  endif
  ;; Calculate the local PSF (actually, the residuals from a gaussian)
  psfrad=1.5*fwhm
  fitrad=1.0*fwhm
  radtol=0.95*fitrad
  ;;need to readin image data array
  ;imagedata=mrdfits(image,0,/silent)
  ;imagedata=readfits(image,imhdr)
  lpp_getpsf,imagedata,psfstarx,psfstary,psfstarmags,psfstarskys $
    ,ccdronoise,ccdgain,gauss,psf,inds,psfrad,fitrad,imagest.psffitarr,psfmag=psfmag,/quiet,fail=fail
  if fail ne 0 then begin
    ;;print,'psf failed'
    if keyword_set(output) then print,'first try making PSF failed, now using all the stars'
    w=wbak
    nw=n_elements(w)
    psfstarx=objx[w]
    psfstary=objy[w]
    psfstarcounts=fluxall[w,0]
    psfstarmags=-2.5*alog10(psfstarcounts)+25
    psfstarskys=skys[w,0]
    inds=lindgen(nw)
    fail=0
    lpp_getpsf,imagedata,psfstarx,psfstary,psfstarmags,psfstarskys $
      ,ccdronoise,ccdgain,gauss,psf,inds,psfrad,fitrad,imagest.psffitarr,psfmag=psfmag,/quiet,fail=fail
    if fail ne 0 then begin
      if keyword_set(output) then print,'second trying making PSF failed too, can not do PSF phot, quiting'
      fail=1
    endif
    print,'second trying making PSF succeed'
  endif
  if keyword_set(output) then print,'end making psf'
endif

;;if psf is not faied, then do the following
if fail eq 0 then begin 
  ;; nstar does the actual psf fitting
  ;;here mags and magerr input are from above apr result, and will be modified after
  ;;psf fitting. Also note the number may changed because stars may get grouped or dropped
  ;;the input mag should be positive, otherwise will report error from nstar
  w=where(magall[*,0] gt 0,nw)
  if nw eq 0 then begin
      print,'*****************************'
      print,'Not one object on '+image+' has an aper flux above zero and a good centroid. Sorry.'
      print,'*****************************'
      return
  endif
  
  magpsf=magall[w,0]
  magpsferr=magerrall[w,0]
  skyspsf=skys[w,0]
  xs=objx[w]
  ys=objy[w]
  inds=lindgen(n_elements(xs))
  
  ;print,n_elements(magpsf),n_elements(magpsferr),n_elements(skyspsf),inds,n_elements(objx),n_elements(objy)
  ;; group the stars together
  group,xs,ys,psfrad+fitrad,ngroup
  psfphotfail=0
  lpp_nstar,imagedata,inds,xs,ys,magpsf,skyspsf,ngroup,ccdgain,ccdronoise,'',magpsferr $
    ,usepsf=psf,gauss=gauss,psfmag=psfmag,psfrad=psfrad,fitrad=fitrad,fail=psfphotfail,/silent
  ;;psf fit failed
  if psfphotfail ne 0 then begin
    if keyword_set(output) then print,'psf fitting failed'
  endif else begin
    ;;findout the targets corresponding to xs,ys
    close_match,objx,objy,xs,ys,m1,m2,radtol,1,missed1,/silent
    ;print,'start matching 5'
    if m1[0] eq -1 then begin
        print,'*********************************'
        print,'Could not fit PSF to target on '+image+'...sorry'
        print,'*********************************'
    endif else begin
        ;; psf
        fluxall[m1,nphot-1]=10.0^(-0.4*(magpsf[m2]-25))
        print,'measured psf flux in ori image is: ',objx[m1[0]],objy[m1[0]],fluxall[m1[0],nphot-1]
        blah=10.0^(-0.4*(magpsf[m2]-psfmag))
        eblah=alog(10.0)/2.5*blah*magpsferr[m2]
        fluxerrall[m1,nphot-1]=10.0^(-0.4*(psfmag-25))*eblah
        ;;print out to check the value
        for i=0,n_elements(m1)-1 do begin
          ;;need to re-calculate the mag using flux value, considering the exposure time
          magall[m1[i],nphot-1]=-2.5*alog10(fluxall[m1[i],nphot-1]/exposures)+25.0
          if finite(fluxerrall[m1[i],nphot-1]) eq 1 then begin
            emagptmp=-2.5*alog10((fluxall[m1[i],nphot-1]-fluxerrall[m1[i],nphot-1])/exposures)+25.0
            emagmtmp=-2.5*alog10((fluxall[m1[i],nphot-1]+fluxerrall[m1[i],nphot-1])/exposures)+25.0
            magerrall[m1[i],nphot-1]=(emagptmp-emagmtmp)/2.0
          endif else begin
            magerrall[m1[i],nphot-1]=9.99
          endelse
          ;help,i,fluxall[m1[i],nphot-1],fluxerrall[m1[i],nphot-1],magall[m1[i],nphot-1],magerrall[m1[i],nphot-1]
          ;print,i,fluxall[m1[i],nphot-1],fluxerrall[m1[i],nphot-1],magall[m1[i],nphot-1],magerrall[m1[i],nphot-1],magall[m1[i],0]
        endfor
    endelse
    ;print,magall,magerrall
  endelse
endif

subphotdid=0
;;great, all done, unless with keyword photsub, even fail, still need to do apt sub
if keyword_set(photsub) then begin
  ;;check the sub image exist or not
  fs=findfile(imagest.cfsb)
  if fs[0] eq '' then begin
    print,'subimage file : ',imagest.cfsb,' not found, skip sub phot!'
    subphotdid=0
  endif else begin
    if keyword_set(output) then begin
      print,'Doing sub image photometry now'
    endif
      print,'Doing sub image photometry now'
    subfluxall=fltarr(nphot)
    subfluxerrall=fltarr(nphot)
    subskynoise=fltarr(nphot)
    subskys=fltarr(nphot)
    submagall=fltarr(nphot)
    submagerrall=fltarr(nphot)
    submagall[*]=!values.d_nan
    submagerrall[*]=!values.d_nan
    ;;readin subimage data
    ;subimagedata=mrdfits(imagest.cfsb,0,imhdr,/silent)
    subimagedata=readfits(imagest.cfsb,imhdr)
    help,(subimagedata)
    ;; do the aprature photometry to the sub image,only to the object, no need to do reference stars
    xs=objx[0]
    ys=objy[0]
    ;; recentroid objects
    gcntrd,subimagedata,xs,ys,xcen,ycen,fwhm ;;;,maxgood=ims.satcounts
    if xcen ne -1.0 and ycen ne -1.0 then begin
        ;;gcntrd succeed
        xs=xcen
        ys=ycen
    endif
    for i=0,nphot-2 do begin
      lpp_get_aper_counts,subimagedata,fwhm,xs,ys,flux,eflux,radius=apt_radius[i],skynoise=skynoisetmp,skys=skytmp
      ;print,flux,eflux
      subfluxall[i]=flux
      print,'measured apt flux in sub image is (i, flux[i])',xs,ys,i,subfluxall[i]
      subfluxerrall[i]=eflux
      subskynoise[i]=skynoisetmp
      subskys[i]=skytmp
      print,'skynoise is: ',subskynoise[i]
      print,'sky is: ',subskys[i]
    end
    subphotdid=1
    ;;transform count to mag, use zero point of 25.0
    ;;this is improtatn, because later we also need this information to calculat the sky noise
    ;;and then limiting magnitude.
    for i=0,n_elements(subfluxall)-1 do begin
      if fluxall[i] gt 0 then begin
        submagall[i]=-2.5*alog10(subfluxall[i]/exposures)+25.0
        if finite(subfluxerrall[i]) eq 1 then begin
          subemagptmp=-2.5*alog10((subfluxall[i]-subfluxerrall[i])/exposures)+25.0
          subemagmtmp=-2.5*alog10((subfluxall[i]+subfluxerrall[i])/exposures)+25.0
          submagerrall[i]=(subemagptmp-subemagmtmp)/2.0
        endif else begin
          submagerrall[i]=9.99
        endelse
      endif
    endfor

    ;;nstar doing the actual psf photometry to the subimage
    ;;but only do it if psf is not fail

    if fail eq 0 then begin
      ;;here mags and magerr input are from above apr result, and will be modified after
      ;;psf fitting. Also note the number may changed because stars may get grouped or dropped
      ;;the input mag should be positive, otherwise will report error from nstar
      submagpsf=submagall[0]
      submagpsferr=submagerrall[0]
      subskyspsf=subskys[0]

      subpsfphotfail=0
      lpp_nstar,subimagedata,[0],xs,ys,submagpsf,subskyspsf,[0],ccdgain,ccdronoise,'',submagpsferr $
        ,usepsf=psf,gauss=gauss,psfmag=psfmag,psfrad=psfrad,fitrad=fitrad,fail=subpsfphotfail,/silent

      ;;psf fit failed
      if subpsfphotfail ne 0 then begin
        if keyword_set(output) then print,'sub psf fitting failed'
      endif else begin
        ;;findout the targets corresponding to xs,ys
        close_match,objx[0],objy[0],xs,ys,m1,m2,radtol,1,missed1,/silent
        ;print,'start matching 5'
        if m1[0] eq -1 then begin
            print,'*********************************'
            print,'Could not fit PSF to target on subimage of '+image+'...sorry'
            print,'target at X,Y of: ',objx[0],objy[0]
            print,'fitting object at X,Y of: ',xs,ys
            print,'*********************************'
        endif else begin
            ;; psf
            ;help,subfluxall,submagpsf,psfmag,submagpsferr
            subfluxall[nphot-1]=10.0^(-0.4*(submagpsf-25))
            print,'measured psf flux in sub image is: ',subfluxall[nphot-1]
            blah=10.0^(-0.4*(submagpsf-psfmag))
            eblah=alog(10.0)/2.5*blah*submagpsferr
            subfluxerrall[nphot-1]=10.0^(-0.4*(psfmag-25))*eblah
            ;;print out to check the value
            ;;only one object
            ;;need to re-calculate the mag using flux value, considering the exposure time
            submagall[nphot-1]=-2.5*alog10(subfluxall[nphot-1]/exposures)+25.0
            if finite(subfluxerrall[nphot-1]) eq 1 then begin
              subemagptmp=-2.5*alog10((subfluxall[nphot-1]-subfluxerrall[nphot-1])/exposures)+25.0
              subemagmtmp=-2.5*alog10((subfluxall[nphot-1]+subfluxerrall[nphot-1])/exposures)+25.0
              submagerrall[nphot-1]=(subemagptmp-subemagmtmp)/2.0
            endif else begin
              submagerrall[nphot-1]=9.99
            endelse
            ;print,subfluxall[nphot-1],subfluxerrall[nphot-1],submagall[nphot-1],submagerrall[nphot-1],submagall[0]
        endelse
      endelse
    endif
  endelse
endif

;;write the out put to the text file, if photsub, write out both
outfile=imagest.psf
openw,lun,outfile,/get_lun
printf,lun,';;id   ximage   yimage    3.5p   err    5.0p   err    7.0p   err    9.0p   err   1.0fh   err   1.5fh   err   2.0fh   err     psf   err'
;;note x,y need plus 1.0
for i=0,nobj-1 do begin
  printf,lun,i+1,objx[i]+1.0,objy[i]+1.0,magall[i,0],magerrall[i,0],magall[i,1],magerrall[i,1],magall[i,2],magerrall[i,2],magall[i,3],magerrall[i,3],magall[i,4],magerrall[i,4],magall[i,5],magerrall[i,5],magall[i,6],magerrall[i,6],magall[i,7],magerrall[i,7],format='(i4,f9.2,f9.2,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3)'
endfor
close,lun
free_lun,lun
if keyword_set(photsub) and subphotdid ne 0 then begin
  outfile=imagest.psfsub
  magall[0,*]=submagall[*]
  magerrall[0,*]=submagerrall[*]
  openw,lun,outfile,/get_lun
  printf,lun,';;id   ximage   yimage    3.5p   err    5.0p   err    7.0p   err    9.0p   err   1.0fh   err   1.5fh   err   2.0fh   err     psf   err'
  ;;note x,y need plus 1.0
  for i=0,nobj-1 do begin
    printf,lun,i+1,objx[i]+1.0,objy[i]+1.0,magall[i,0],magerrall[i,0],magall[i,1],magerrall[i,1],magall[i,2],magerrall[i,2],magall[i,3],magerrall[i,3],magall[i,4],magerrall[i,4],magall[i,5],magerrall[i,5],magall[i,6],magerrall[i,6],magall[i,7],magerrall[i,7],format='(i4,f9.2,f9.2,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3)'
  endfor
  close,lun
  free_lun,lun
endif

;;write the sky (always from the original image, not the sub image) if savesky keyword is set
if keyword_set(savesky) then begin
  openw,lun,imagest.sky,/get_lun
  ;;note here the skynoise was divided by exposures too, in order to make it
  ;;consistent with stars count for calculating the right magnitudes.
  noise=median(skynoise)/exposures
  if median(skynoise) eq 0 then begin
    noise=0.000001
  endif
  printf,lun,noise
  close,lun
  free_lun,lun
endif

if keyword_set(output) then begin
  print,systime(1)-starttime,format='("photometry took ",f5.2," seconds")'
endif
end
