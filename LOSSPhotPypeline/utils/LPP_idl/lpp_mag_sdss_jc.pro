pro lpp_mag_sdss_jc,direction,starst,gri=gri,nou=nou,output=output

if n_params() eq 0 then begin
  print,'Syntax- LPP_mag_sdss_jc,direction,starst'
  print,'direction: 1 SDSS -> JohnsonCousins, 2 JohnsonCousins -> SDSS'
  return
endif

if direction eq 1 then begin
  if keyword_set(output) then begin
    print,'working on : SDSS -> JohnsonCousins'
  endif
  ;;See papger Smith et al. 2002, ApJ, 123, 2121
  ;starst.B = starst.SG + 0.47*(starst.SG-starst.SR) + 0.17
  ;starst.V = starst.SG - 0.55*(starst.SG-starst.SR) - 0.03
  ;starst.U = 0.75*(starst.SU-starst.SG) - 0.83 + starst.B
  ;starst.R = starst.V - (0.59*(starst.SG-starst.SR) + 0.11)
  ;ind1=where(starst.SR-starst.SI lt 0.95,nf1)
  ;if nf1 ge 1 then begin
  ;  starst[ind1].I = starst[ind1].R - (1.00*(starst[ind1].SR-starst[ind1].SI) + 0.21)
  ;endif
  ;ind2=where(starst.SR-starst.SI ge 0.95,nf2)
  ;if nf2 ge 1 then begin
  ;  starst[ind2].I = starst[ind2].R - (0.70*(starst[ind2].SR-starst[ind2].SI) + 0.49)
  ;endif

if not keyword_set(gri) then begin
  if not keyword_set(nou) then begin
    Btmp = starst.SG + 0.47*(starst.SG-starst.SR) + 0.17
    starst.U = 0.75*(starst.SU-starst.SG) - 0.83 + Btmp
  endif

  ;;See papger Lupton (2005)
  ;B = u - 0.8116*(u - g) + 0.1313;  sigma = 0.0095
  ;B = g + 0.3130*(g - r) + 0.2271;  sigma = 0.0107
  ;V = g - 0.2906*(u - g) + 0.0885;  sigma = 0.0129
  ;V = g - 0.5784*(g - r) - 0.0038;  sigma = 0.0054
  ;R = r - 0.1837*(g - r) - 0.0971;  sigma = 0.0106
  ;R = r - 0.2936*(r - i) - 0.1439;  sigma = 0.0072
  ;I = r - 1.2444*(r - i) - 0.3820;  sigma = 0.0078
  ;I = i - 0.3780*(i - z)  -0.3974;  sigma = 0.0063
  starst.B = starst.SG + 0.3130*(starst.SG-starst.SR) + 0.2271
  starst.V = starst.SG - 0.5784*(starst.SG-starst.SR) - 0.0038
  starst.R = starst.SR - 0.2936*(starst.SR-starst.SI) - 0.1439
  starst.I = starst.SR - 1.2444*(starst.SR-starst.SI) - 0.3820
endif else begin
  starst.R = starst.SR - 0.2936*(starst.SR-starst.SI) - 0.1439
  starst.I = starst.SR - 1.2444*(starst.SR-starst.SI) - 0.3820
endelse
endif
if direction eq 2 then begin
  print,'JohnsonCousins -> SDSS is not working, fix it'
  ;print,'JohnsonCousins -> SDSS'
endif

end
