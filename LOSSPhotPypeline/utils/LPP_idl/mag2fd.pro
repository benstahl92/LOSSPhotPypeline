pro mag2fd,mag,filter,err=err,minus=minus,plus=plus,outflux=outflux,silent=silent

 if N_params() eq 0 then begin
	print,'Syntax: mag2fluxdensity,mag,filter,err=err,[minus=minus,plus=plus],outflux=outflux'
 	return
 endif

mag_err_minus=mag*0D0+0D0
mag_err_plus=mag*0D0+0D0

if keyword_set(err) then begin
  mag_err_minus=err*(-1D0)
  mag_err_plus=err
endif

if keyword_set(minus) then mag_err_minus=minus
if keyword_set(plus) then mag_err_plus=plus

number=n_elements(mag)
if (number ne n_elements(filter) or number ne n_elements(mag_err_minus) or number ne n_elements(mag_err_plus) ) then begin
    print,"Element number in parament not matching or is zero! Doing nothing"
    return
endif

tempst={flux:0d0, fluxerr:0d0, fluxerrminus:0d0, fluxerrplus:0d0, mag:0d0, magerr:0d0, magerrminus:0d0, magerrplus:0d0, filter:''}
outflux=replicate(tempst,number)
outflux.mag=mag
outflux.magerr=(mag_err_plus-mag_err_minus)/2d0
outflux.magerrminus=mag_err_minus
outflux.magerrplus=mag_err_plus
outflux.filter=filter

for i=0,number-1 do begin
  case filter[i] of
    'U': begin
           temp=mag[i]-0.002+0.77
           tempminus=mag[i]+mag_err_plus[i]-0.002+0.77
           tempplus=mag[i]+mag_err_minus[i]-0.002+0.77
           constantvale=6d0
           factor=3631d0
         end
    'B': begin
           temp=mag[i]-0.002-0.12
           tempminus=mag[i]+mag_err_plus[i]-0.002-0.12
           tempplus=mag[i]+mag_err_minus[i]-0.002-0.12
           constantvale=6d0
           factor=3631d0
         end
    'V': begin
           temp=mag[i]-0.002
           tempminus=mag[i]+mag_err_plus[i]-0.002
           tempplus=mag[i]+mag_err_minus[i]-0.002
           constantvale=6d0
           factor=3631d0
         end
    'R': begin
           temp=mag[i]-0.002+0.186
           tempminus=mag[i]+mag_err_plus[i]-0.002+0.186
           tempplus=mag[i]+mag_err_minus[i]-0.002+0.186
           constantvale=6d0
           factor=3631d0
         end
    'X': begin
           temp=mag[i]-0.002+0.186
           tempminus=mag[i]+mag_err_plus[i]-0.002+0.186
           tempplus=mag[i]+mag_err_minus[i]-0.002+0.186
           constantvale=6d0
           factor=3631d0
         end
    'clear': begin
           temp=mag[i]-0.002+0.186
           tempminus=mag[i]+mag_err_plus[i]-0.002+0.186
           tempplus=mag[i]+mag_err_minus[i]-0.002+0.186
           constantvale=6d0
           factor=3631d0
         end
    'CLEAR': begin
           temp=mag[i]-0.002+0.186
           tempminus=mag[i]+mag_err_plus[i]-0.002+0.186
           tempplus=mag[i]+mag_err_minus[i]-0.002+0.186
           constantvale=6d0
           factor=3631d0
         end
    'I': begin
           temp=mag[i]-0.002+0.444
           tempminus=mag[i]+mag_err_plus[i]-0.002+0.444
           tempplus=mag[i]+mag_err_minus[i]-0.002+0.444
           constantvale=6d0
           factor=3631d0
         end
    'J': begin
           temp=mag[i]-0.002+0.899
           tempminus=mag[i]+mag_err_plus[i]-0.002+0.899
           tempplus=mag[i]+mag_err_minus[i]-0.002+0.899
           constantvale=6d0
           factor=3631d0
         end
    'H': begin
           temp=mag[i]-0.002+1.379
           tempminus=mag[i]+mag_err_plus[i]-0.002+1.379
           tempplus=mag[i]+mag_err_minus[i]-0.002+1.379
           constantvale=6d0
           factor=3631d0
         end
    'K': begin
           temp=mag[i]-0.002+1.886
           tempminus=mag[i]+mag_err_plus[i]-0.002+1.886
           tempplus=mag[i]+mag_err_minus[i]-0.002+1.886
           constantvale=6d0
           factor=3631d0
         end
    'Kp': begin
           temp=mag[i]-0.002+1.826
           tempminus=mag[i]+mag_err_plus[i]-0.002+1.826
           tempplus=mag[i]+mag_err_minus[i]-0.002+1.826
           constantvale=6d0
           factor=3631d0
         end
    'L': begin
           temp=mag[i]-0.002+2.765
           tempminus=mag[i]+mag_err_plus[i]-0.002+2.765
           tempplus=mag[i]+mag_err_minus[i]-0.002+2.765
           constantvale=6d0
           factor=3631d0
         end
    'SDSS-u': begin
           temp=mag[i]-0.04
           tempminus=mag[i]+mag_err_plus[i]-0.04
           tempplus=mag[i]+mag_err_minus[i]-0.04
           constantvale=6d0
           factor=3631d0
         end
    'u': begin
           temp=mag[i]-0.04
           tempminus=mag[i]+mag_err_plus[i]-0.04
           tempplus=mag[i]+mag_err_minus[i]-0.04
           constantvale=6d0
           factor=3631d0
         end
    'SDSS-g': begin
           temp=mag[i]
           tempminus=mag[i]+mag_err_plus[i]
           tempplus=mag[i]+mag_err_minus[i]
           constantvale=6d0
           factor=3631d0
         end
    'g': begin
           temp=mag[i]
           tempminus=mag[i]+mag_err_plus[i]
           tempplus=mag[i]+mag_err_minus[i]
           constantvale=6d0
           factor=3631d0
         end
    'SDSS-r': begin
           temp=mag[i]
           tempminus=mag[i]+mag_err_plus[i]
           tempplus=mag[i]+mag_err_minus[i]
           constantvale=6d0
           factor=3631d0
         end
    'r': begin
           temp=mag[i]
           tempminus=mag[i]+mag_err_plus[i]
           tempplus=mag[i]+mag_err_minus[i]
           constantvale=6d0
           factor=3631d0
         end
    'SDSS-i': begin
           temp=mag[i]-0.015
           tempminus=mag[i]+mag_err_plus[i]-0.015
           tempplus=mag[i]+mag_err_minus[i]-0.015
           constantvale=6d0
           factor=3631d0
         end
    'i': begin
           temp=mag[i]-0.015
           tempminus=mag[i]+mag_err_plus[i]-0.015
           tempplus=mag[i]+mag_err_minus[i]-0.015
           constantvale=6d0
           factor=3631d0
         end
    'SDSS-z': begin
           temp=mag[i]-0.03
           tempminus=mag[i]+mag_err_plus[i]-0.03
           tempplus=mag[i]+mag_err_minus[i]-0.03
           constantvale=6d0
           factor=3631d0
         end
    'z': begin
           temp=mag[i]-0.03
           tempminus=mag[i]+mag_err_plus[i]-0.03
           tempplus=mag[i]+mag_err_minus[i]-0.03
           constantvale=6d0
           factor=3631d0
         end
    'Swift-v': begin
           temp=mag[i]-17.89
           tempminus=mag[i]+mag_err_plus[i]-17.89
           tempplus=mag[i]+mag_err_minus[i]-17.89
           constantvale=0d0
           factor=254.4d0
         end
    'Swift-b': begin
           temp=mag[i]-19.11
           tempminus=mag[i]+mag_err_plus[i]-19.11
           tempplus=mag[i]+mag_err_minus[i]-19.11
           constantvale=0d0
           factor=92.0d0
         end
    'Swift-u': begin
           temp=mag[i]-18.34
           tempminus=mag[i]+mag_err_plus[i]-18.34
           tempplus=mag[i]+mag_err_minus[i]-18.34
           constantvale=0d0
           factor=66.6d0
         end
    'Swift-uvw1': begin
           temp=mag[i]-17.49
           tempminus=mag[i]+mag_err_plus[i]-17.49
           tempplus=mag[i]+mag_err_minus[i]-17.49
           constantvale=0d0
           factor=92.6d0
         end
    'Swift-uvm2': begin
           temp=mag[i]-16.82
           tempminus=mag[i]+mag_err_plus[i]-16.82
           tempplus=mag[i]+mag_err_minus[i]-16.82
           constantvale=0d0
           factor=141.1d0
         end
    'Swift-uvw2': begin
           temp=mag[i]-17.35
           tempminus=mag[i]+mag_err_plus[i]-17.35
           tempplus=mag[i]+mag_err_minus[i]-17.35
           constantvale=0d0
           factor=85.2d0
         end
    'Swift-white': begin
           temp=mag[i]-20.29
           tempminus=mag[i]+mag_err_plus[i]-20.29
           tempplus=mag[i]+mag_err_minus[i]-20.29
           constantvale=0d0
           factor=14.9d0
         end
    else: begin
            print,'Unknown filter!'
            ;return
            break
          end
  endcase
   

  outflux[i].flux=factor*10d0^(constantvale-0.4*temp)
  outflux[i].fluxerrminus=factor*10d0^(constantvale-0.4*tempminus)-outflux[i].flux
  outflux[i].fluxerrplus=factor*10d0^(constantvale-0.4*tempplus)-outflux[i].flux
  outflux[i].fluxerr=(outflux[i].fluxerrplus-outflux[i].fluxerrminus)/2d0
  if not keyword_set(silent) then print,outflux[i].flux,' uJy for mag ',mag[i],' in ',filter[i]
endfor
end
