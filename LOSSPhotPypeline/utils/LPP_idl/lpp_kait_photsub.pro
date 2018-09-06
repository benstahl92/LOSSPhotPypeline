pro lpp_kait_photsub,cobjlist,ref,subreg=subreg,output=output

if n_params() eq 0 then begin
  print,'syntax - lpp_kait_photsub,cobjlist,ref,subreg=subreg'
  print,'subreg = 1: percent, say 0.9'
  print,'subreg = 2: given reg, say [100,400,100,400] (equal to [100:400,100:400])'
  return
endif

tnb=n_elements(cobjlist)

for i=0,tnb-1 do begin

  lpp_image_name_trans,cobjlist[i],imagest
  
  fi=findfile(imagest.cimg)
  
  if fi[0] eq '' then begin
    print,'file : ',imagest.cimg,' not found, quit!'
    return
  endif

  ;; Now warp the image
  if keyword_set(output) then begin
    print,cobjlist[i],ref
  endif
  lpp_kait_warp_tf_ref,cobjlist[i],ref,/save,/from
  ;;use wcs trans
  ;image_warpwcs_tf_ref,cobjlist[i],ref,/from
  if keyword_set(output) then begin
    print,cobjlist[i],ref
  endif

  fr=findfile(imagest.cfwp)
  if fr[0] eq '' then begin
    print,'file : ',imagest.cfwp,' not found, quit!'
    return
  endif
  
  lpp_kait_subtract_isis,imagest.cimg,imagest.cfwp,subreg=subreg
endfor

end
