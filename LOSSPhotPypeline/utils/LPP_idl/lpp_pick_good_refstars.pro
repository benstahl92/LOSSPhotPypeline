pro lpp_pick_good_refstars,starid,radecfile,calfile,output=output

!quiet = 1
!except = 0

if n_params() eq 0 then begin
  print,'Syntax- LPP_pick_good_refstar,starid,radecfile,calfile'
  return
endif

if n_elements(starid) eq 0 then begin
  print,'No starid is given, quit'
  return
endif

;;readin radecfile
readcol,radecfile,ra,dec
goodrefra=ra[starid+1]
goodrefdec=dec[starid+1]

;;print,'good ref stars:'
;;for i=0,n_elements(goodrefra)-1 do begin
;;  print,'star id', starid[i], ': ',goodrefra[i],goodrefdec[i],format='(a,i3,a,f11.5,f11.5)'
;;endfor

;;readin calfile
lpp_readcolst,calfile,calst

;;do the match
;;match the two radec; match to 5 arcsec
close_match_radec,goodrefra,goodrefdec,calst.ra,calst.dec,indtmp1,indtmp2,5.0/3600.0,1.0,missed
nmatch=n_elements(indtmp1)
if nmatch le 0 then begin
  print,'no stars matches with catalog, doing nothing, exiting ...'
  return
endif
;;printout the matched stars, lines
if keyword_set(output) then begin
  print,'good ref stars:'
  for i=0,nmatch-1 do begin
    print,'star id', starid[indtmp1[i]], ': ',goodrefra[indtmp1[i]],goodrefdec[indtmp1[i]],calst[indtmp2[i]].ra,calst[indtmp2[i]].dec,' at line : ',indtmp2[i]+2,format='(a,i4,a,f11.5,f11.5,f11.5,f11.5,a,i4)'
  endfor
  print,''
  print,''
endif

;;;;use awk to print out the needed lines
;;;;Unfortunatley, this is not in the exact order as input arrary, use new method below
;;cmd="awk 'NR==1"
;;  for i=0,nmatch-1 do begin
;;    cmd=cmd+"||NR=="+string(indtmp2[i]+2,format='(i0)')
;;  endfor
;;cmd=cmd+"' "+calfile
;;spawn,cmd
;;
;;outcalfile=calfile
;;strreplace,outcalfile,'.dat','_use.dat'
;;cmd=cmd+" > "+outcalfile
;;print,''
;;print,''
;;print,cmd
;;spawn,cmd

;;new method, makesure the output stars are in right order
cmd="awk 'NR==1"+"' "+calfile
spawn,cmd,line0
;;also add starID to the output file
line0='starID '+line0
lines=[line0]
for i=0,nmatch-1 do begin
  cmd="awk 'NR=="+string(indtmp2[i]+2,format='(i0)')+"' "+calfile
  ;print,cmd
  spawn,cmd,linetmp
  ;;also add starID to the output file
  linetmp=string(starid[indtmp1[i]],format='(i0)')+"  "+linetmp
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
