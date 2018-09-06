pro lpp_mag_ps1_jc,direction,starst,output=output

if n_params() eq 0 then begin
  print,'Syntax- LPP_mag_ps1_jc,direction,starst'
  print,'direction: 1 PS1 -> JohnsonCousins, 2 JohnsonCousins -> PS1'
  return
endif

if direction eq 1 then begin
  if keyword_set(output) then begin
    print,'working on : PS1 -> JohnsonCousins'
  endif
  ;;See papger Tonry et al., 2012, ApJ, 750, 99
  ;;see equation 6 and Table 6
  ;;B1 = g + 0.212 + 0.55*(starst.SG-starst.SR) + 0.034*(starst.SG-starst.SR)^2

  B1 = starst.SG + 0.212 + 0.556*(starst.SG-starst.SR) + 0.034*(starst.SG-starst.SR)^2
  V1 = starst.SR + 0.005 + 0.462*(starst.SG-starst.SR) + 0.013*(starst.SG-starst.SR)^2
  R1 = starst.SR - 0.137 - 0.108*(starst.SG-starst.SR) - 0.029*(starst.SG-starst.SR)^2
  I1 = starst.SI - 0.366 - 0.136*(starst.SG-starst.SR) - 0.018*(starst.SG-starst.SR)^2
  B2 = starst.SG + 0.213 + 0.587*(starst.SG-starst.SR)
  V2 = starst.SR + 0.006 + 0.474*(starst.SG-starst.SR)
  R2 = starst.SR - 0.138 - 0.131*(starst.SG-starst.SR)
  I2 = starst.SI - 0.367 - 0.149*(starst.SG-starst.SR)
  starst.B = (B1 + B2)/2.0
  starst.V = (V1 + V2)/2.0
  starst.R = (R1 + R2)/2.0
  starst.I = (I1 + I2)/2.0
endif
if direction eq 2 then begin
  print,'JohnsonCousins -> PS1 is not working, fix it'
endif

end
