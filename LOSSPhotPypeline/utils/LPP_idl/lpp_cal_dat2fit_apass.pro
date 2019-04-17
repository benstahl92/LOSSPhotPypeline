pro lpp_cal_dat2fit_apass,apass_datfilename,output=output

!quiet = 1
!except = 0

if n_params() eq 0 then begin
  print,'Syntax- ,LPP_cal_dat2fit_apass,apass_datfilename'
  return
endif

datfilename=apass_datfilename
outstfitfile=datfilename

if keyword_set(output) then begin
  print,'working on',datfilename
endif
lpp_readcolst,datfilename,apassst
tnb=n_elements(apassst)

stars=lpp_gen_star_mags(tnb,mag=0.0,merr=0.01)

stars.ra=apassst.ra
stars.dec=apassst.dec
stars.B=apassst.B
stars.V=apassst.V
stars.SG=apassst.g
stars.SR=apassst.r
stars.SI=apassst.i
stars.C=apassst.r
stars.CLEAR=apassst.r
;;zwk added on 190318. added error
stars.EB=apassst.BErr
stars.EV=apassst.VErr
stars.ESG=apassst.gErr
stars.ESR=apassst.rErr
stars.ESI=apassst.iErr
stars.EC=apassst.rErr
stars.ECLEAR=apassst.rErr
lpp_mag_sdss_jc,1,stars,/gri
stars.C=stars.R
stars.CLEAR=stars.R
stars.EC=stars.ER
stars.ECLEAR=stars.ECLEAR


strreplace,outstfitfile,'.dat','_Landolt_standard.fit'
wsttofile,outstfitfile,stars

lpp_cal_landolt2natural,outstfitfile

end
