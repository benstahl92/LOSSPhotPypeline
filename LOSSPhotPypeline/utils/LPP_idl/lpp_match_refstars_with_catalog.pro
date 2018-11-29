pro lpp_match_refstars_with_catalog,radecfile,calfile,output=output

!quiet = 1
!except = 0

if n_params() eq 0 then begin
  print,'Syntax- LPP_match_refstars_with_catalog,radecfile,calfile,output=output'
  return
endif

;;readin radecfile
readcol,radecfile,ra,dec

lpp_readcolst,calfile,calst

;;do the match
;;match the two radec; match to 5 arcsec
close_match_radec,ra,dec,calst.ra,calst.dec,indtmp1,indtmp2,5.0/3600.0,1.0,missed
nmatch=n_elements(indtmp1)
if nmatch le 0 then begin
  print,'no stars matches with catalog, doing nothing, exiting ...'
  return
endif
indtmp2=uniq(indtmp2)
;;do the sorting to select 40 bright stars.
totalstar=n_elements(indtmp2)
if totalstar gt 40 then begin
  indtmp=sort(calst[indtmp2].R)
  indtmp2=indtmp2[indtmp[0:39]]
  print,'Selected the 40 most bright stars for calibration out from the total of ',totalstar
endif else begin
  indtmp=sort(calst[indtmp2].R)
  indtmp2=indtmp2[indtmp]
endelse

;;new method, makesure the output stars are in right order
cmd="awk 'NR==1"+"' "+calfile
spawn,cmd,line0
lines=[line0]
nmatch=n_elements(indtmp2)
for i=0,nmatch-1 do begin
  cmd="awk 'NR=="+string(indtmp2[i]+2,format='(i0)')+"' "+calfile
  ;print,cmd
  spawn,cmd,linetmp
  ;;also add starID to the output file
  lines=[lines,linetmp]
endfor
if keyword_set(output) then begin
  print,lines
endif
;;write the output file
outcalfile=calfile
strreplace,outcalfile,'.dat','_use.dat'
openw, outlun, outcalfile, /get
printf,outlun,lines
free_lun,outlun

end
