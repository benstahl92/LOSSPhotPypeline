pro lpp_cal_instrumag,image,filter,cal_source,cal_file,photsub=photsub,output=output

if n_params() eq 0 then begin
  print,'syntax - LPP_cal_instrumag,image,filter,cal_source,cal_file,photsub=photsub,output=output'
  return
endif

lpp_image_name_trans,image,imagest

fi=findfile(image)

if fi[0] eq '' then begin
  print,'file : ',image,' not found, quit!'
  return
endif

inputfiles=[]
outputfiles=[]

;;findinput files, now we always use the psf result
fp=findfile(imagest.psf)
if fp[0] eq '' then begin
  print,'file : ',imagest.psf,' not found!'
endif
inputfiles=[fp[0]]
outputfiles=[imagest.psfdat]
if keyword_set(photsub) then begin
  fp=findfile(imagest.psfsub)
  if fp[0] eq '' then begin
    print,'file : ',imagest.psfsub,' not found!'
  endif else begin
    inputfiles=[inputfiles,fp[0]]
    outputfiles=[outputfiles,imagest.psfsubdat]
  endelse
endif
if n_elements(inputfiles) eq 0 then begin
  print,'No input mag file found, doing nuthing'
  return
endif

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

;;need to do every photmag calibration
;;zeropointoffset=dblarr(8)+!values.d_nan
photmethodnum=8
zeropointoffset=fltarr(photmethodnum)+100.0
calMagMean=fltarr(photmethodnum)
instruMagMean=fltarr(photmethodnum)

for j=0,n_elements(inputfiles)-1 do begin
  ;;readin instrument mag file, and trans x,y to ra,dec
  print,'working on file : ',inputfiles[j]
  readcol,inputfiles[j],id,x,y,mag35,mag35err,mag50,mag50err,mag70,mag70err,mag90,mag90err,mag10fh,mag10fherr,mag15fh,mag15fherr,mag20fh,mag20fherr,magpsf,magpsferr

  imhdr=headfits(image)
  extast,imhdr,astr
  xy2rd,x,y,astr,raimage,decimage
    
  ;;need to do every mag calibration

  for k=0,photmethodnum-1 do begin

    case k of
      0 : begin
            maguse=mag35
          end
      1 : begin
            maguse=mag50
          end
      2 : begin
            maguse=mag70
          end
      3 : begin
            maguse=mag90
          end
      4 : begin
            maguse=mag10fh
          end
      5 : begin
            maguse=mag15fh
          end
      6 : begin
            maguse=mag20fh
          end
      7 : begin
            maguse=magpsf
          end
    else: begin
            print,'Unknown photmehtod'
            break
          end
    endcase
    ;cleanup, getrid of NaN
    indtmp=where(maguse gt 0 and maguse lt 30, nf)
    if nf le 0 then begin
      print,'No good stars, doing nothing, exiting ...'
      break
    endif
    maguse=maguse[indtmp]
    rause=raimage[indtmp]
    decuse=decimage[indtmp]
    
    ;;match the two radec; match to 5 arcsec
    close_match_radec,rause,decuse,stars.ra,stars.dec,indtmp1,indtmp2,5.0/3600.0,1.0,missed,/silent
    nmatch=n_elements(indtmp1)
    if nmatch le 0 then begin
      print,'no stars matches with catalog, doing nothing for photmethod',k
      break
    endif
    
    ;;printout the matched stars
    ;; printout has only clear filter, but actual calculation below is correct
    if keyword_set(output) then begin
      for i=0,nmatch-1 do begin
        print,id[indtmp1[i]],rause[indtmp1[i]],decuse[indtmp1[i]],stars[indtmp2[i]].ra,stars[indtmp2[i]].dec,stars[indtmp2[i]].CLEAR
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
    instruMagMean[k]=mean(maguse[indtmp1])
    calMagMean[k]=mean(calmags)
    zeropointoffset[k]=calMagMean[k]-instruMagMean[k]
    print,'zeromag for photmethod',k,' is : ',zeropointoffset[k]
    ;;zero point offset is the offset to 25.0. So the real zeropoint should be
    ;;25.0 + zeropointoffset
    ;;should do more clean up, getrid of big offset ones, but for now, let it be
  endfor

  ;;write the zeropoint, use the 3.5p one
  if (j eq 0) then begin
    openw,lun,imagest.zero,/get_lun
    ;;note here the skynoise was divided by exposures too, in order to make it
    ;;consistent with stars count for calculating the right magnitudes.
    printf,lun,25.0+zeropointoffset[0]
    close,lun
    free_lun,lun
  endif
  
  ;;now, output the calibrated mag, name mag+zeropointoffset
  openw,lun,outputfiles[j],/get_lun
  printf,lun,';;id   ximage   yimage    3.5p   err    5.0p   err    7.0p   err    9.0p   err   1.0fh   err   1.5fh   err   2.0fh   err     psf   err'
  ;;note x,y need plus 1.0
  for i=0,n_elements(id)-1 do begin
    printf,lun,id[i],x[i],y[i],mag35[i]+zeropointoffset[0],mag35err[i],mag50[i]+zeropointoffset[1],mag50err[i],mag70[i]+zeropointoffset[2],mag70err[i],mag90[i]+zeropointoffset[3],mag90err[i],mag10fh[i]+zeropointoffset[4],mag10fherr[i],mag15fh[i]+zeropointoffset[5],mag15fherr[i],mag20fh[i]+zeropointoffset[6],mag20fherr[i],magpsf[i]+zeropointoffset[7],magpsferr[i],format='(i04,f9.2,f9.2,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3,f8.3,f6.3)'
  endfor
  close,lun
  free_lun,lun
endfor


end
