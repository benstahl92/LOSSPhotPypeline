pro lpp_cal_instrumag,image,filter,cal_source,cal_file,usepsf=usepsf,output=output

if n_params() eq 0 then begin
  print,'syntax - LPP_cal_instrumag,image,filter,cal_source,cal_file,usepsf=usepsf'
  return
endif

lpp_image_name_trans,image,imagest

fi=findfile(image)

if fi[0] eq '' then begin
  print,'file : ',image,' not found, quit!'
  return
endif

if keyword_set(usepsf) then begin
  fp=findfile(imagest.psf)
  if fp[0] eq '' then begin
    print,'file : ',imagest.psf,' not found, quit!'
    return
  endif
  fp=fp[0]
endif else begin
  fp=findfile(imagest.apt)
  if fp[0] eq '' then begin
    print,'file : ',imagest.apt,' not found, quit!'
    return
  endif
  fp=fp[0]
endelse

;fa=findfile(imagest.apass)
;if fa[0] eq '' then begin
;  print,'file : ',imagest.apass,' not found, quit!'
;  return
;endif

;; read calibration file
stars=MRDFITS(cal_file, 1, /SILENT)

;; do cut (stricter if source is apass) to select good stars
indtmp=where(stars.B le 18.0 and stars.V le 18.0 and stars.SG le 18.0 and stars.SR le 18.0 and stars.SI le 18.0, nf)
if cal_source eq 'APASS' then begin
  indtmp=where(stars.B le 16.0 and stars.V le 16.0 and stars.SG le 16.0 and stars.SR le 16.0 and stars.SI le 16.0, nf)
endif
if nf le 0 then begin
  print,'No good calibration star, doing nothing, exiting ...'
  return
endif
stars=stars[indtmp]

if keyword_set(usepsf) then begin
  ;;readin instrument mag file, and trans x,y to ra,dec
  readcol,imagest.psf,id,x,y,mag35,mag35err,mag50,mag50err,mag70,mag70err,mag90,mag90err,mag10fh,mag10fherr,mag15fh,mag15fherr,mag20fh,mag20fherr,magpsf,magpsferr
  ;cleanup, getrid of NaN
  indtmp=where(magpsf gt 0 and magpsf lt 30, nf)
  if nf le 0 then begin
    print,'No good stars, doing nothing, exiting ...'
    return
  endif
  
  ;;the following line will deleted NaN stars, not good, need upate
  ;;but for now just let it be.
  id=id[indtmp] & x=x[indtmp] & y=y[indtmp] & mag35=mag35[indtmp] & mag35err=mag35err[indtmp] & mag50=mag50[indtmp] & mag50err=mag50err[indtmp] & mag70=mag70[indtmp] & mag70err=mag70err[indtmp] & mag90=mag90[indtmp] & mag90err=mag90err[indtmp] & mag10fh=mag10fh[indtmp] & mag10fherr=mag10fherr[indtmp] & mag15fh=mag15fh[indtmp] & mag15fherr=mag15fherr[indtmp] & mag20fh=mag20fh[indtmp] & mag20fherr=mag20fherr[indtmp] & magpsf=magpsf[indtmp] & magpsferr=magpsferr[indtmp]
endif else begin
  ;;readin instrument mag file, and trans x,y to ra,dec
  readcol,imagest.apt,id,x,y,mag35,mag35err,mag50,mag50err,mag70,mag70err,mag90,mag90err,mag10fh,mag10fherr,mag15fh,mag15fherr,mag20fh,mag20fherr
  ;cleanup, getrid of NaN
  indtmp=where(mag35 gt 0 and mag35 lt 30, nf)
  if nf le 0 then begin
    print,'No good stars, doing nothing, exiting ...'
    return
  endif

  ;;the following line will deleted NaN stars, not good, need upate
  ;;but for now just let it be.
  id=id[indtmp] & x=x[indtmp] & y=y[indtmp] & mag35=mag35[indtmp] & mag35err=mag35err[indtmp] & mag50=mag50[indtmp] & mag50err=mag50err[indtmp] & mag70=mag70[indtmp] & mag70err=mag70err[indtmp] & mag90=mag90[indtmp] & mag90err=mag90err[indtmp] & mag10fh=mag10fh[indtmp] & mag10fherr=mag10fherr[indtmp] & mag15fh=mag15fh[indtmp] & mag15fherr=mag15fherr[indtmp] & mag20fh=mag20fh[indtmp] & mag20fherr=mag20fherr[indtmp]
endelse
imhdr=headfits(image)
extast,imhdr,astr
xy2rd,x,y,astr,raimage,decimage

;;match the two radec; match to 5 arcsec
close_match_radec,raimage,decimage,stars.ra,stars.dec,indtmp1,indtmp2,5.0/3600.0,1.0,missed,/SILENT
nmatch=n_elements(indtmp1)
if nmatch le 0 then begin
  print,'no stars matches with catalog, doing nothing, exiting ...'
  return
endif

;;printout the matched stars
;; printout has only clear filter, but actual calculation below is correct
if keyword_set(output) then begin
  for i=0,nmatch-1 do begin
    print,id[indtmp1[i]],raimage[indtmp1[i]],decimage[indtmp1[i]],stars[indtmp2[i]].ra,stars[indtmp2[i]].dec,stars[indtmp2[i]].CLEAR
  endfor
endif

if filter eq "B" then begin
  calmags = stars[indtmp2].B
endif
if filter eq "V" then begin
  calmags = stars[indtmp2].V
endif
if filter eq "R" then begin
  calmags = stars[indtmp2].R
endif
if filter eq "I" then begin
  calmags = stars[indtmp2].I
endif
if filter eq "CLEAR" then begin
  calmags = stars[indtmp2].CLEAR
endif

;;do calibration, find zeropoint
if keyword_set (usepsf) then begin
  instruMagMean=mean(magpsf[indtmp1])
endif else begin
  instruMagMean=mean(mag35[indtmp1])
endelse
calMagMean=mean(calmags)
zeropointoffset=calMagMean-instruMagMean
;;zero point offset is the offset to 25.0. So the real zeropoint should be
;;25.0 + zeropointoffset
;;should do more clean up, getrid of big offset ones, but for now, let it be

;;now, output the calibrated mag, name mag+zeropointoffset
if keyword_set(usepsf) then begin
  openw,lun,imagest.psfdat,/get_lun
  printf,lun,';;id   ximage   yimage    3.5p   err    5.0p   err    7.0p   err    9.0p   err   1.0fh   err   1.5fh   err   2.0fh   err     psf   err'
  ;;note x,y need plus 1.0
  for i=0,n_elements(id)-1 do begin
    printf,lun,id[i],x[i],y[i],mag35[i]+zeropointoffset,mag35err[i],mag50[i]+zeropointoffset,mag50err[i],mag70[i]+zeropointoffset,mag70err[i],mag90[i]+zeropointoffset,mag90err[i],mag10fh[i]+zeropointoffset,mag10fherr[i],mag15fh[i]+zeropointoffset,mag15fherr[i],mag20fh[i]+zeropointoffset,mag20fherr[i],magpsf[i]+zeropointoffset,magpsferr[i],format='(i04,f9.2,f9.2,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3)'
  endfor
  close,lun
  free_lun,lun
endif else begin
  openw,lun,imagest.aptdat,/get_lun
  printf,lun,';;id   ximage   yimage    3.5p   err    5.0p   err    7.0p   err    9.0p   err   1.0fh   err   1.5fh   err   2.0fh   err'
  ;;note x,y need plus 1.0
  for i=0,n_elements(id)-1 do begin
    printf,lun,id[i],x[i],y[i],mag35[i]+zeropointoffset,mag35err[i],mag50[i]+zeropointoffset,mag50err[i],mag70[i]+zeropointoffset,mag70err[i],mag90[i]+zeropointoffset,mag90err[i],mag10fh[i]+zeropointoffset,mag10fherr[i],mag15fh[i]+zeropointoffset,mag15fherr[i],mag20fh[i]+zeropointoffset,mag20fherr[i],format='(i04,f9.2,f9.2,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3)'
  endfor
  close,lun
  free_lun,lun
endelse

;;write the zeropoint
openw,lun,imagest.zero,/get_lun
;;note here the skynoise was divided by exposures too, in order to make it
;;consistent with stars count for calculating the right magnitudes.
printf,lun,25.0+zeropointoffset
close,lun
free_lun,lun


end
