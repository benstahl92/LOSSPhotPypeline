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
  EB1square = (1.0+0.556+0.034*2.0*(starst.SG-starst.SR))^2*starst.ESG^2 + (-0.556 - 0.034*2.0*(starst.SG-starst.SR))^2*starst.ESR^2+0.032^2
  V1 = starst.SR + 0.005 + 0.462*(starst.SG-starst.SR) + 0.013*(starst.SG-starst.SR)^2
  EV1square = (1.0-0.462+0.013*2.0*(starst.SG-starst.SR))^2*starst.ESR^2 + (0.462 + 0.013*2.0*(starst.SG-starst.SR))^2*starst.ESG^2+0.012^2
  R1 = starst.SR - 0.137 - 0.108*(starst.SG-starst.SR) - 0.029*(starst.SG-starst.SR)^2
  ER1square = (1.0+0.108-0.029*2.0*(starst.SG-starst.SR))^2*starst.ESR^2 + (-0.108 - 0.029*2.0*(starst.SG-starst.SR))^2*starst.ESG^2+0.015^2
  I1 = starst.SI - 0.366 - 0.136*(starst.SG-starst.SR) - 0.018*(starst.SG-starst.SR)^2
  EI1square = starst.ESI^2+(0.136+0.018*2.0*(starst.SG-starst.SR))^2*starst.ESR^2 + (-0.136 - 0.018*2.0*(starst.SG-starst.SR))^2*starst.ESG^2+0.017^2
  B2 = starst.SG + 0.213 + 0.587*(starst.SG-starst.SR)
  EB2square = (1.0+0.587)^2*starst.ESG^2 + 0.587^2*starst.ESR^2
  V2 = starst.SR + 0.006 + 0.474*(starst.SG-starst.SR)
  EV2square = (1.0-0.474)^2*starst.ESR^2 + 0.474^2*starst.ESG^2
  R2 = starst.SR - 0.138 - 0.131*(starst.SG-starst.SR)
  ER2square = (1.0+0.131)^2*starst.ESR^2 + 0.131^2*starst.ESG^2
  I2 = starst.SI - 0.367 - 0.149*(starst.SG-starst.SR)
  EI2square = starst.ESI^2 + 0.149^2*starst.ESR^2 + 0.149^2*starst.ESG^2
  starst.B = (B1 + B2)/2.0
  starst.V = (V1 + V2)/2.0
  starst.R = (R1 + R2)/2.0
  starst.I = (I1 + I2)/2.0
  ;;;zwk added on 190318.
  ;print,EB1square,EB2square,EV1square,EV2square,ER1square,ER2square,EI1square,EI2square
  starst.EB = sqrt(EB1square + EB2square)/2.0
  starst.EV = sqrt(EV1square + EV2square)/2.0
  starst.ER = sqrt(ER1square + ER2square)/2.0
  starst.EI = sqrt(EI1square + EI2square)/2.0
endif
if direction eq 2 then begin
  print,'JohnsonCousins -> PS1 is not working, fix it'
endif

end
