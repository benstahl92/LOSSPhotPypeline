pro lpp_dat_res_group,datafile,outst,outfile=outfile

!quiet = 1
!except = 0

if n_params() eq 0 then begin
  print,'Syntax- LPP_dat_res_group,datafile,outst,outfile=outfile'
  return
endif

lpp_dat_res_format,datafile,photst
ind=where(photst.emag le 10.0,fb)
if fb lt 0 then begin
  print,'No good data, doing nothing'
  return
endif

if fb eq 1 then begin
  print,'Only one data porint is good, not doing group'
  return
endif

photst=photst[ind]

lpp_phot_dat_res_group,photst.time,photst.mag,photst.filter,magerr=photst.emag,outst=outst,outfile=outfile

end
