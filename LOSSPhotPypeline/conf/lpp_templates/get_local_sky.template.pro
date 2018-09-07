function get_local_sky,image,x,y,radius1,radius2,annulus=annulus,rejected=rejected $
                       ,std=std,inmask=inmask,noreject=noreject

;+
; NAME:
;      get_local_sky
; PURPOSE:
;      determines the mean sky and STD near an object
; TYPE:
;      
; CALLING SEQUENCE:
;      sky_value=get_local_sky(image,x,y,radius1,radius2
;      [,annulus=annulus,rejected=rejected,std=std,inmask=inmask
;      ,noreject=noreject])
; INPUTS:
;      image--> 2d fltarr of the image
;      x--> x location of the object on the image
;      y--> y location of the object on the image
;      radius1--> inner radius of the sky annulus
;      radius2--> outter radius of the sky annulus
; OPTIONAL INPUTS:
;      inmask--> indicies of pixels to mask
; KEYWORDS:
;      noreject--> do not preform a clipped mean
; OUTPUTS:
;      returns the mean sky in the annulus
;      annulus--> indicies of pixels used to calculate the sky
;      rejected--> indicies of pixels in the annulus not used to
;      calculate the sky
;      std--> standard deviation of the sky in the annulus
; COMMON BLOCKS:
;      
; SIDE EFFECTS:
;      
; EXAMPLES:
;      sky_value=get_local_sky(image,hostx,hosty,23.9,50.6,std=std,inmask=mask,reject=reject,annu=annu)
; PROCEDURE:
;      calls a C routine which calculates a clipped mean of pixels in
;      the specified annulus.
; MODIFICATION HISTORY:
;      Robert Quimby 2001
;-

;; ##### Set true path to .so file here! #####
sopath=

if keyword_set(noreject) then doreject=0 else doreject=1

ans=size(image)
n_rows=long(ans[2])
n_cols=long(ans[1])

n_inmask=n_elements(inmask)
if n_inmask eq 0 then inmask=lonarr(1)-1

sky_value=fltarr(1)
std=fltarr(1)
annulus=lonarr(4*radius2^2.0)-1
rejected=lonarr(4*radius2^2.0)-1

;;print,'calling local_sky_sub.c'
ans=call_external(sopath+'local_sky_sub.so','local_sky_sub' $
                  ,float(image) $
                  ,long(n_rows) $
                  ,long(n_cols) $
                  ,float(x) $
                  ,float(y) $
                  ,float(radius1) $
                  ,float(radius2) $
                  ,long(inmask) $
                  ,long(n_inmask) $
                  ,float(sky_value) $
                  ,float(std) $
                  ,long(annulus) $
                  ,long(doreject) $
                  ,long(rejected))
;;print,'sky_value is ',sky_value


w=where(annulus ne -1)
if w[0] ne -1 then annulus=annulus[w] else annulus=-1
w=where(rejected ne -1)
if w[0] ne -1 then rejected=rejected[w] else rejected=-1

return,sky_value[0]
end
