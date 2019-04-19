pro lpp_cal_landolt2natural,calfile

if n_params() eq 0 then begin
  print,'Syntax- LPP_cal_Landolt_Natural_diff,calfile'
  print,'Note: only applies to BVRI band, not other bands'
  return
endif

extend=strmid(calfile,strlen(calfile)-4,4)
;print,extend
if extend eq '.fit' or extend eq 'fits' then begin
  st=mrdfits(calfile,1)
endif else begin
  lpp_readcolst,calfile,st
endelse

;help,stLandolt
outstfitfilehead=calfile
strreplace,outstfitfilehead,'_Landolt_standard.fit',''
strreplace,outstfitfilehead,'.fits',''
strreplace,outstfitfilehead,'.fit',''
strreplace,outstfitfilehead,'.dat',''

;;for kait1
stnew=st
Cb=-0.095
Cv=0.027
Cr=-0.181
Ci=-0.071
stnew.B=st.B+Cb*(st.B-st.V)
stnew.V=st.V+Cv*(st.B-st.V)
stnew.R=st.R+Cr*(st.V-st.R)
stnew.I=st.I+Ci*(st.R-st.I)
;;add updated error by zwk on 190419
stnew.EB=sqrt((1.0+Cb)^2*st.EB^2 + Cb^2*st.EV^2)
stnew.EV=sqrt((1.0-Cv)^2*st.EV^2 + Cv^2*st.EB^2)
stnew.ER=sqrt((1.0-Cr)^2*st.ER^2 + Cr^2*st.EV^2)
stnew.EI=sqrt((1.0-Ci)^2*st.EI^2 + Ci^2*st.ER^2)
outstfitfile=outstfitfilehead+'_kait1_natural.fit'
wsttofile,outstfitfile,stnew

;;for kait2
stnew=st
Cb=-0.085
Cv=0.032
Cr=0.062
Ci=-0.007
stnew.B=st.B+Cb*(st.B-st.V)
stnew.V=st.V+Cv*(st.B-st.V)
stnew.R=st.R+Cr*(st.V-st.R)
stnew.I=st.I+Ci*(st.R-st.I)
stnew.EB=sqrt((1.0+Cb)^2*st.EB^2 + Cb^2*st.EV^2)
stnew.EV=sqrt((1.0-Cv)^2*st.EV^2 + Cv^2*st.EB^2)
stnew.ER=sqrt((1.0-Cr)^2*st.ER^2 + Cr^2*st.EV^2)
stnew.EI=sqrt((1.0-Ci)^2*st.EI^2 + Ci^2*st.ER^2)
outstfitfile=outstfitfilehead+'_kait2_natural.fit'
wsttofile,outstfitfile,stnew

;;for kait3
stnew=st
Cb=-0.057
Cv=0.032
Cr=0.064
Ci=-0.001
stnew.B=st.B+Cb*(st.B-st.V)
stnew.V=st.V+Cv*(st.B-st.V)
stnew.R=st.R+Cr*(st.V-st.R)
stnew.I=st.I+Ci*(st.R-st.I)
stnew.EB=sqrt((1.0+Cb)^2*st.EB^2 + Cb^2*st.EV^2)
stnew.EV=sqrt((1.0-Cv)^2*st.EV^2 + Cv^2*st.EB^2)
stnew.ER=sqrt((1.0-Cr)^2*st.ER^2 + Cr^2*st.EV^2)
stnew.EI=sqrt((1.0-Ci)^2*st.EI^2 + Ci^2*st.ER^2)
outstfitfile=outstfitfilehead+'_kait3_natural.fit'
wsttofile,outstfitfile,stnew

;;for kait4
stnew=st
Cb=-0.134
Cv=0.051
Cr=0.107
Ci=0.014
stnew.B=st.B+Cb*(st.B-st.V)
stnew.V=st.V+Cv*(st.B-st.V)
stnew.R=st.R+Cr*(st.V-st.R)
stnew.I=st.I+Ci*(st.R-st.I)
stnew.EB=sqrt((1.0+Cb)^2*st.EB^2 + Cb^2*st.EV^2)
stnew.EV=sqrt((1.0-Cv)^2*st.EV^2 + Cv^2*st.EB^2)
stnew.ER=sqrt((1.0-Cr)^2*st.ER^2 + Cr^2*st.EV^2)
stnew.EI=sqrt((1.0-Ci)^2*st.EI^2 + Ci^2*st.ER^2)
outstfitfile=outstfitfilehead+'_kait4_natural.fit'
wsttofile,outstfitfile,stnew

;;;Updated by zwk on 170108
;;;Found that nicke B, and B color termed change sometime between
;;;090113 and 090821, so should divide nickel to nickel1 and nickel2
;;;for Nickel

;;;for Nickel1
stnew=st
Cb=-0.092
Cv=0.053
Cr=0.089
Ci=-0.044
stnew.B=st.B+Cb*(st.B-st.V)
stnew.V=st.V+Cv*(st.B-st.V)
stnew.R=st.R+Cr*(st.V-st.R)
stnew.I=st.I+Ci*(st.R-st.I)
stnew.EB=sqrt((1.0+Cb)^2*st.EB^2 + Cb^2*st.EV^2)
stnew.EV=sqrt((1.0-Cv)^2*st.EV^2 + Cv^2*st.EB^2)
stnew.ER=sqrt((1.0-Cr)^2*st.ER^2 + Cr^2*st.EV^2)
stnew.EI=sqrt((1.0-Ci)^2*st.EI^2 + Ci^2*st.ER^2)
outstfitfile=outstfitfilehead+'_nickel1_natural.fit'
wsttofile,outstfitfile,stnew

;;;for Nickel2
stnew=st
Cb=0.041
Cv=0.082
Cr=0.092
Ci=-0.043
stnew.B=st.B+Cb*(st.B-st.V)
stnew.V=st.V+Cv*(st.B-st.V)
stnew.R=st.R+Cr*(st.V-st.R)
stnew.I=st.I+Ci*(st.R-st.I)
stnew.EB=sqrt((1.0+Cb)^2*st.EB^2 + Cb^2*st.EV^2)
stnew.EV=sqrt((1.0-Cv)^2*st.EV^2 + Cv^2*st.EB^2)
stnew.ER=sqrt((1.0-Cr)^2*st.ER^2 + Cr^2*st.EV^2)
stnew.EI=sqrt((1.0-Ci)^2*st.EI^2 + Ci^2*st.ER^2)
outstfitfile=outstfitfilehead+'_nickel2_natural.fit'
wsttofile,outstfitfile,stnew


end
