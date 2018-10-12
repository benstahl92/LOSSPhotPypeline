pro lpp_cal_dat2fit_sdss,sdss_datfilename,output=output

!quiet = 1
!except = 0

if n_params() eq 0 then begin
  print,'Syntax- LPP_cal_dat2fit_sdss,sdss_datfilename'
  return
endif

datfilename=sdss_datfilename
outstfitfile=datfilename

if keyword_set(output) then begin
  print,'working on',datfilename
endif
lpp_readcolst,datfilename,sdssst
tnb=n_elements(sdssst)

stars=lpp_gen_star_mags(tnb,mag=0.0,merr=0.01)

stars.ra=sdssst.ra
stars.dec=sdssst.dec
stars.SU=sdssst.u
stars.SG=sdssst.g
stars.SR=sdssst.r
stars.SI=sdssst.i
stars.SZ=sdssst.z
stars.C=sdssst.r
stars.CLEAR=sdssst.r
lpp_mag_sdss_jc,1,stars
stars.C=stars.R
stars.CLEAR=stars.R

strreplace,outstfitfile,'.dat','_Landolt_standard.fit'
wsttofile,outstfitfile,stars

lpp_cal_landolt2natural,outstfitfile

end
