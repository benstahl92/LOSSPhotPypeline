pro lpp_kait_subtract_isis,image,cfcvref,subreg=subreg,output=output

if n_params() eq 0 then begin
  print,'syntax - lpp_kait_subtract,image,cfcvref'
  print,'Note : images must have been aligned'
  print,'subreg = 1: percent, say 0.9'
  print,'subreg = 2: given reg, say [100,400,100,400] (equal to [100:400,100:400])'
  return
endif

if not keyword_set(subreg) then subreg=0.9

lpp_image_name_trans,image,imagest

fi=findfile(image)

if fi[0] eq '' then begin
  print,'file : ',image,' not found, quit!'
  return
endif
fr=findfile(cfcvref)
if fr[0] eq '' then begin
  print,'file : ',cfcvref,' not found, quit!'
  return
endif

cmd='Simsubtract '+cfcvref+' '+image+' '+imagest.CFSB+' '+imagest.CFCV
spawn,cmd

im_sfsb=mrdfits(imagest.CFSB,0,head1,/fscale)
im_sfcv=mrdfits(imagest.CFCV,0,head2,/fscale)

if n_elements(subreg) eq 1 then begin
  naxis1=sxpar(head1,'NAXIS1')
  naxis2=sxpar(head1,'NAXIS1')
  minx=round(naxis1*(1.0-subreg))
  maxx=round(naxis1*(subreg))
  miny=round(naxis2*(1.0-subreg))
  maxy=round(naxis2*(subreg))
endif
if n_elements(subreg) eq 4 then begin
  minx=subreg[0]
  maxx=subreg[1]
  miny=subreg[2]
  maxy=subreg[3]
endif
if keyword_set(output) then begin
  print,minx,maxx,miny,maxy
endif 

tmp_img=mrdfits(image,0,headtmp1,/fscale)
tmp_img_ref=mrdfits(cfcvref,0,headtmp2,/fscale)
bzero=sxpar(headtmp1,'BZERO')
if bzero ne 0.0 then sxaddpar,headtmp1,'BZERO',0.0
writefits,'tmp_img_isis_sub_c.fit',tmp_img[minx:maxx,miny:maxy],headtmp1
bzero=sxpar(headtmp2,'BZERO')
if bzero ne 0.0 then sxaddpar,headtmp2,'BZERO',0.0
writefits,'tmp_img_isis_sub_ref_c.fit',tmp_img_ref[minx:maxx,miny:maxy],headtmp2
cmd='Simsubtract '+'tmp_img_isis_sub_ref_c.fit'+' '+'tmp_img_isis_sub_c.fit'+' '+imagest.CFSB+' '+imagest.CFCV
spawn,cmd
im_sfsb[minx:maxx,miny:maxy]=mrdfits(imagest.CFSB,/fscale)
im_sfcv[minx:maxx,miny:maxy]=mrdfits(imagest.CFCV,/fscale)
bzero=sxpar(head1,'BZERO')
if bzero ne 0.0 then sxaddpar,head1,'BZERO',0.0
writefits,imagest.CFSB,im_sfsb,head1
bzero=sxpar(head2,'BZERO')
if bzero ne 0.0 then sxaddpar,head2,'BZERO',0.0
writefits,imagest.CFCV,im_sfcv,head2

cmd='rm -f '+'tmp_img_isis_sub_c.fit'+' '+'tmp_img_isis_sub_ref_c.fit'
spawn,cmd

end
