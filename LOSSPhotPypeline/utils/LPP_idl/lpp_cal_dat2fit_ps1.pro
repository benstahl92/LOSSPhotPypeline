pro lpp_cal_dat2fit_ps1,ps1_datfilename,output=output

!quiet = 1
!except = 0

if n_params() eq 0 then begin
  print,'Syntax- LPP_cal_dat2fit_ps1,ps1_datfilename'
  return
endif

datfilename=ps1_datfilename
outstfitfile=datfilename

if keyword_set(output) then begin
  print,'working on',datfilename
endif
lpp_readcolst,datfilename,ps1st
tnb=n_elements(ps1st)

stars=lpp_gen_star_mags(tnb,mag=0.0,merr=0.01)

stars.ra=ps1st.ra
stars.dec=ps1st.dec
stars.SG=ps1st.g
stars.SR=ps1st.r
stars.SI=ps1st.i
stars.SZ=ps1st.z
stars.C=ps1st.r
stars.CLEAR=ps1st.r
;;zwk added on 190318. added error
stars.ESG=ps1st.gErr
stars.ESR=ps1st.rErr
stars.ESI=ps1st.iErr
stars.ESZ=ps1st.zErr
stars.EC=ps1st.rErr
stars.ECLEAR=ps1st.rErr
lpp_mag_ps1_jc,1,stars
stars.C=stars.R
stars.CLEAR=stars.R
stars.EC=stars.ER
stars.ECLEAR=stars.ER


strreplace,outstfitfile,'.dat','_Landolt_standard.fit'
wsttofile,outstfitfile,stars

lpp_cal_landolt2natural,outstfitfile

end
