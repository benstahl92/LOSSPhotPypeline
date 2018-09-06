function lpp_gen_star_mags,number,mag=mag,merr=merr
if n_params() eq 0 then begin
  print,'Syntax- LPP_gen_star_mags,number,mag=mag,merr=merr'
  return,-1
endif

if not keyword_set(mag) then mag=0.0
if not keyword_set(merr) then merr=0.01

sttmp={ra:0.0, dec:0.0, epoch: 2000.0, SU: mag, ESU: merr, SG: mag, ESG: merr, SR: mag, ESR: merr, SI: mag, ESI: merr, SZ: mag, ESZ: merr, U: mag, EU: merr, B: mag, EB: merr, V: mag, EV: merr, R: mag, ER: merr, I: mag, EI: merr, J: mag, EJ: merr, H: mag, EH: merr, K: mag, EK: merr, C: mag, EC: merr, CLEAR: mag, ECLEAR: merr}
starmagst=replicate(sttmp,number)
return,starmagst

end
