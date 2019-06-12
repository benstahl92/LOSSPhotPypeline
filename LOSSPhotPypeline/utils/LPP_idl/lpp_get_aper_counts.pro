;; got it from rphot_get_aper_counts in rphot, did not use any mask
;; ********************************************************************************
pro lpp_get_aper_counts,image,fwhm,x,y,flux,eflux,lsky=lsky,std=std,skynoise=skynoise,skys=skys,radius=radius,skyrad1=skyrad1,skyrad2=skyrad2,ccdgain=ccdgain,forcesky=forcesky

;; preforms aperature photometry on the current image. X and Y can be
;; arrays. If no mask exists for the current image and we are getting
;; target counts, calculate mask on the fly.

if not keyword_set(radius) then radius=3.5
if not keyword_set(skyrad1) then skyrad1ratio=2.0
if not keyword_set(skyrad2) then skyrad2ratio=4.0
if not keyword_set(ccdgain) then ccdgain=1.0

n=n_elements(x)
flux=dblarr(n)
eflux=dblarr(n)
skys=dblarr(n)
skynoises=dblarr(n)
for i=0,n-1 do begin

    ;; reset sky radii
    skyrad1=skyrad1ratio*radius > fwhm + 1.0
    skyrad2=skyrad2ratio*radius > fwhm
    ;print,'radius,skyrad1,skyrad2:',radius,skyrad1,skyrad2
    if keyword_set(forcesky) then begin
        setsky=forcesky
        std=forcesky[1]
        nsky=forcesky[2]
    endif else begin 
      ;; do local sky subtraction
      niter=0
      naper=!pi*(radius > fwhm)^2.0
      repeat begin
          lsky=(get_local_sky(image,x[i],y[i],skyrad1,skyrad2 $
                              ,annulus=annulus,std=std,rej=rej,noreject=noreject))[0]
          nsky=n_elements(annulus)
          w=where(rej ne -1,nrej)
          nsky=nsky-nrej
          ;;w=where(noreject ne -1,nrej)
          ;;if noreject eq 0 then nsky=nsky-nrej
          niter=niter+1
          skyrad2=skyrad2+0.5*skyrad1
      endrep until nsky gt 2*naper or niter gt 8
      setsky=[lsky,std,nsky]
      skys[i]=lsky

    endelse
    ;; get the counts
    lpp_aper,image,x[i],y[i],f,ef,sky,esky,ccdgain,radius,[skyrad1,skyrad2],[0,0] $
        ,/flux,/exact,setskyval=setsky,/silent
    flux[i]=f
    eflux[i]=ef

    ;; calcualte the local sky noise
    area=!pi*radius^2.0
    ;skynoise=sqrt(area*std^2.0 + std^2.0/nsky*area^2.0)
    skynoises[i]=sqrt(area*std^2.0 + std^2.0/nsky*area^2.0)
endfor
;;
;help,skynoises
;print,'skynoises:',skynoises
skynoise=median(skynoises)

w=where(finite(flux) eq 0,nw)
if nw gt 0 then begin
    print,"APER returned flux=NAN. It shouldn't. Use updated APER...stopping"
    stop
endif

end

