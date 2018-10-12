pro lpp_dat_res_bin,datafile,outst,outfile=outfile,output=output

!quiet = 1
!except = 0

if n_params() eq 0 then begin
  print,'Syntax- LPP_dat_res_bin,datafile,outst,outfile=outfile'
  return
endif

lpp_dat_res_format,datafile,photst
ind=where(photst.emag le 10.0,fb)
if fb lt 0 then begin
  print,'No good data, doing nothing'
  return
endif

photst=photst[ind]
nimages=n_elements(photst)
;;get all the filters
allfilters=photst.filter
allfilters=strtrim(allfilters,2)
;;uniq filters
allfilters=allfilters[UNIQ(allfilters, SORT(allfilters))]
filternumber=n_elements(allfilters)
;print,'Filters found in all the data :'
;print,allfilters

groups=fltarr(nimages)
groupsfilter=strarr(nimages)
currentgroup=1
;;criterion to judge the same group or not
judgetime=0.4 ;;days
for i=0,nimages-1 do begin
  ;;only check left items that haven't been assigned the groups
  left=where(groups eq 0,nf)
  if nf gt 0 then begin
    ind=where(abs(photst[i].time-photst[left].time) le judgetime, nfg)
    if nfg ne 0 then begin
      onegroup=left[ind]
      ;;now need to check in one group, is there many filters?
      ;;if yes, split it into more groups
      for j=0,filternumber-1 do begin
        ind=where(photst[onegroup].filter eq allfilters[j], nff)
        if nff ge 1 then begin
          groups[onegroup[ind]]=currentgroup
          currentgroup=currentgroup+1
        endif
      endfor
    endif
  endif
endfor

;;old structure this was updated below by zwk on 140511
;sttmp={time:0d0, etime:0d0, mag:0.0, emag:0.0, emag_plus:0.0, emag_minus:0.0, mag_limit:0.0, filter:'', imname:''}
;;this must be the same structure as in LPP_dat_res_format.pro
sttmp={time:0d0, etime:0d0, mag:0.0, emag:0.0, emag_plus:0.0, emag_minus:0.0, mag_limit:0.0, filter:'', imname:'',fd:0d0, fderr:0d0}
outst=replicate(sttmp,max(groups))

if keyword_set(outfile) then begin
  openw, outlun, outfile, /get
endif

;for i=0,nimages-1 do begin
for i=1,max(groups) do begin
  ind=where(groups eq i,fb)
  if fb gt 1 then begin
    ;print,'multi detection'
    outst[i-1].TIME=mean(photst[ind].TIME)
    outst[i-1].ETIME=(max(photst[ind].TIME)-min(photst[ind].TIME))/2.0+max(photst[ind].ETIME)
    outst[i-1].MAG=mean(photst[ind].MAG)
    outst[i-1].EMAG=mean(photst[ind].EMAG)
    outst[i-1].EMAG_PLUS=outst[i-1].MAG+outst[i-1].EMAG
    outst[i-1].EMAG_MINUS=outst[i-1].MAG-outst[i-1].EMAG
    outst[i-1].MAG_LIMIT=mean(photst[ind].MAG_LIMIT)
    outst[i-1].FILTER=photst[ind[0]].FILTER
    outst[i-1].IMNAME=string(photst[ind[0]].IMNAME)
    ;;ideally, should use the following, make that work
    ;outst[i-1].IMNAME=string(photst[ind].IMNAME)
  endif else begin
    ;print,'single detection'
    outst[i-1]=photst[ind[0]]
  endelse

  ;;print out
  if keyword_set(output) then begin
    print,outst[i-1].TIME,outst[i-1].ETIME,outst[i-1].mag,outst[i-1].EMAG_MINUS,outst[i-1].EMAG_PLUS,outst[i-1].MAG_LIMIT,' '+outst[i-1].filter+' ',outst[i-1].IMNAME,format='(f16.6,f12.5,f12.5,f12.5,f12.5,f12.5,a0,a0)'
  endif

  if keyword_set(outfile) then begin
    printf,outlun,outst[i-1].TIME,outst[i-1].ETIME,outst[i-1].mag,outst[i-1].EMAG_MINUS,outst[i-1].EMAG_PLUS,outst[i-1].MAG_LIMIT,' '+outst[i-1].filter+' ',outst[i-1].IMNAME,format='(f16.6,f12.5,f12.5,f12.5,f12.5,f12.5,a0,a0)'
  endif

endfor

if keyword_set(outfile) then begin
  free_lun,outlun
endif

end
