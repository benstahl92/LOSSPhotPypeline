pro lpp_sim_fake_star,image,ximage,yimage,mag,fwhm=fwhm,exposures=exposures,outfile=outfile,psffitarrfile=psffitarrfile,usenaturalmag=usenaturalmag

if n_params() eq 0 then begin
  print,'syntax - lpp_sim_fake_star,image,ximage,yimage,mag,fwhm=fwhm,exposures=exposures'
  return
endif

if not keyword_set(exposures) then exposures=1.0

if (n_elements(ximage) ne n_elements(yimage)) or (n_elements(ximage) ne n_elements(mag)) then begin
  print,'number of elements in ximage, yimage or mag are not the same, please check'
  return
endif
if n_elements(ximage) eq 0 then begin
  print,'number of elements in ximage is 0, please check'
  return
endif

;image_name_trans,image,imagest
lpp_image_name_trans,image,imagest

fi=findfile(image)

if fi[0] eq '' then begin
  print,'file : ',image,' not found, quit!'
  return
endif

;;;Note, in IDL, this value need -1
ximage=ximage-1.0
yimage=yimage-1.0

;;OK, all prepared, can proceed

;; first, find the image size
;imhdr=headfits(image)
imagedata=mrdfits(image,0,imhdr,/silent)
maxX=float(sxpar(imhdr,'NAXIS1'))
maxY=float(sxpar(imhdr,'NAXIS2'))
;print,maxX,maxY

if keyword_set(usenaturalmag) then begin
  magzero=25.0
endif else begin
  ;;also need to find zero mag from .zero file
  ff=findfile(imagest.zero)
  if ff[0] eq '' then begin
    print,'file : ',imagest.zero,' not found, quit!'
    return
  endif
  readcol,imagest.zero,magzero
  magzero=magzero[0]
endelse
print,'zero mag is : ',magzero

psffitfilereaded=0
for i=0,n_elements(ximage)-1 do begin
  ;totalcount=5000
  ;;now need to findout the totalcount according to the mag
  ;;note in our pipeline, exposure time was set to be 1 (because of a bug we found before), so
  totalcount=(10^((mag[i]-magzero)/(-2.5)))*exposures
  print,'mag ',mag[i],' corresponding to flux count of :',totalcount
  ;;method 1, simulating with real psf
  if keyword_set(psffitarrfile) then begin
    if psffitfilereaded eq 0 then begin
      ff=findfile(psffitarrfile)
      if ff[0] eq '' then begin
        print,'file : ',psffitarrfile,' not found'
        ;;try to find _psffitarr.fit
        ff=findfile(imagest.psffitarr)
        if ff[0] eq '' then begin
          print,'file : ',imagest.psffitarr,'also not found, quit'
          ;;try to find _psffitarr.fit
          return
        endif else begin
          print,'OK, find ',imagest.psffitarr,', use it.'
          rdpsf,realpsf,hrealpsf,imagest.psffitarr
          psffitfilereaded=1
          psfmag = sxpar(hrealpsf,'PSFMAG')
        endelse
      endif else begin
        rdpsf,realpsf,hrealpsf,psffitarrfile
        psfmag = sxpar(hrealpsf,'PSFMAG')
        psffitfilereaded=1
      endelse
    endif
    psfdim=size(realpsf)
    width=psfdim[1]
    halfwidth=width/2
    ;print,width,halfwidth
    ;;width need to be even
    
    if ((ximage[i] - halfwidth) lt 0) or ((ximage[i] + halfwidth) gt maxX-1) then begin
      print,'ximage[i] of ',ximage[i],' is too close to the X edge, not simulating this star'
      continue
    endif
    if ((yimage[i] - halfwidth) lt 0) or ((yimage[i] + halfwidth) gt maxY-1) then begin
      print,'ximage[i] of ',ximage[i],' is too close to the Y edge, not simulating this star'
      continue
    endif

    ;;calculate the scale between psfcount mag and real psfmag
    psfcountmag=-2.5*alog10(total(realpsf))+25.0
    psfcountmagscale=(10^((psfmag-psfcountmag)/2.5))
    print,'psfcountmagscale is: ',psfcountmagscale
    countscale=totalcount/total(realpsf)
    print,'countscale is : ',countscale
    totalscale=countscale*psfcountmagscale
    print,'totalscale is : ',totalscale
    simstar_arr=(realpsf)*totalscale
    ;help,simstar_arr
    ;print,simstar_arr
  endif else begin
    ;;method 2, simulating with a perfect gaussian function
    ;;method 2 need fwhm informaiton
    if not keyword_set(fwhm) then begin
      ;;no fwhm is given, try to read from header first
      fwhm=float(sxpar(imhdr,'FWHM'))
      print,'fwhm in header is',fwhm
      if fwhm eq 0 then begin
        ;;no fwhm is in the header, need to look into the .fwhm file
        ff=findfile(imagest.fwhm)
        if ff[0] eq '' then begin
          print,'file : ',imagest.fwhm,' not found, quit!'
          return
        endif
        readcol,imagest.fwhm,fwhm
        fwhm=fwhm[0]
      endif
    endif
    if fwhm le 0 then begin
      print,'fwhm is 0 or below 0, wrong value, please check'
      return
    endif
    print,'fwhm is: ',fwhm,' pixel'

    width=15
    ;;width need to be even
    halfwidth=width/2

    if ((ximage[i] - halfwidth) lt 0) or ((ximage[i] + halfwidth) gt maxX-1) then begin
      print,'ximage[i] of ',ximage[i],' is too close to the X edge, not simulating this star'
      continue
    endif
    if ((yimage[i] - halfwidth) lt 0) or ((yimage[i] + halfwidth) gt maxY-1) then begin
      print,'ximage[i] of ',ximage[i],' is too close to the Y edge, not simulating this star'
      continue
    endif

    sigma=fwhm/2.35482
    print,'sigma = ',sigma
    ;simstar_arr=GAUSSIAN_FUNCTION([sigma,sigma],width=width,MAXIMUM=5000)
    simstar_arr=GAUSSIAN_FUNCTION([sigma,sigma],width=width,/NORMALIZE)*totalcount
    ;help,simstar_arr
  endelse
  ;print,total(simstar_arr)

  ;print,simstar_arr[5:7,5:7]
  ;help,imagedata[ximage[i]-halfwidth:ximage[i]+halfwidth,yimage[i]-halfwidth:yimage[i]+halfwidth]
  if (width mod 2) eq 0 then begin
    imagedata[ximage[i]-halfwidth+1:ximage[i]+halfwidth,yimage[i]-halfwidth+1:yimage[i]+halfwidth] = imagedata[ximage[i]-halfwidth+1:ximage[i]+halfwidth,yimage[i]-halfwidth+1:yimage[i]+halfwidth] + simstar_arr
  endif else begin
    imagedata[ximage[i]-halfwidth:ximage[i]+halfwidth,yimage[i]-halfwidth:yimage[i]+halfwidth] = imagedata[ximage[i]-halfwidth:ximage[i]+halfwidth,yimage[i]-halfwidth:yimage[i]+halfwidth] + simstar_arr
  endelse
endfor

if not keyword_set(outfile) then begin
  outfile=imagest.root+'_sim_c.fit'
endif
writefits,outfile,imagedata,imhdr

end
