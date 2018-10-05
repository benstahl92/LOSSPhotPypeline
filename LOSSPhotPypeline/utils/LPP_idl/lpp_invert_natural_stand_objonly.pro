pro lpp_invert_natural_stand_objonly,natural_data_file,system,outfile=outfile,output=output

if n_params() ne 2 then begin
  print,'syntax- LPP_invert_natural_stand_objonly,natural_data_file,system'
  print,'system options: kait1, kait2, kait3, kait4, nickel1,nickel2'
  return
endif

nochanges=0
;;see Mo's paper Table 4, observed color terms
case system of
  'kait1' : begin
      color_term={C_B:-0.095, C_V:0.027, C_R:-0.181, C_I:-0.071}
  end
  'kait2' : begin
      color_term={C_B:-0.085, C_V:0.032, C_R:0.062, C_I:-0.007}
  end
  'kait3' : begin
      color_term={C_B:-0.057, C_V:0.032, C_R:0.064, C_I:-0.001}
  end
  'kait4' : begin
      color_term={C_B:-0.134, C_V:0.051, C_R:0.107, C_I:0.014}
  end
  'nickel1': begin
      color_term={C_B:-0.092, C_V:0.053, C_R:0.089, C_I:-0.044}
  end
  'nickel2': begin
      color_term={C_B:0.041, C_V:0.082, C_R:0.092, C_I:-0.043}
  end
  'Landolt': begin
      color_term={C_B:0.000, C_V:0.000, C_R:0.000, C_I:0.000}
      nochanges=1
  end
  else     : begin
      print,'Could not recognize the system, Using color term 0'
      color_term={C_B:0.000, C_V:0.000, C_R:0.000, C_I:0.000}
      nochanges=1
  end
endcase

;;readin natural mag file
;;examples
;; GROUP      MJD  STAR     B   EB     V   EV     R   ER     I   EI
;;    1 55798.1728    0 15.18 0.02 14.75 0.02 14.65 0.02 14.76 0.03
;;    2 55798.1740    0 15.20 0.02 14.76 0.02 14.65 0.02 14.77 0.03
lpp_readcolst,natural_data_file,natural_st

stand_st=natural_st

tagnames=strtrim(tag_names(stand_st),2)
tagnumber=n_elements(tagnames)
;print,tagnumber

;;dealing with different groups, minimum need B, and V

indtmp=where(tagnames eq 'B', nf)
if nf eq 0 then begin
  print,'B band mag is not in the input file, can not do the transformation, quiting ...'
  return
endif

indtmp=where(tagnames eq 'V', nf)
if nf eq 0 then begin
  print,'V band mag is not in the input file, can not do the transformation, quiting ...'
  return
endif

b_v=(natural_st.B-natural_st.V)/(1.0+color_term.C_B-color_term.C_V)
stand_st.B=natural_st.B-color_term.C_B*b_v
stand_st.V=natural_st.V-color_term.C_V*b_v

indtmp=where(tagnames eq 'R', nf)
if nf ne 0 then begin
  stand_st.R=(natural_st.R-color_term.C_R*stand_st.V)/(1.0-color_term.C_R)
endif

indtmp=where(tagnames eq 'I', nf)
if nf ne 0 then begin
  stand_st.I=(natural_st.I-color_term.C_I*stand_st.R)/(1.0-color_term.C_I)
endif

indtmp=where(tagnames eq 'U', nf)
if nf ne 0 then begin
  print,'U band has no color term in build, just output the same value'
endif

indtmp=where(tagnames eq 'CLEAR', nf)
if nf ne 0 then begin
  print,'CLEAR band has no color term in build, just output the same value'
endif

;;print out tags, this need update, casue different filter numbers have diffferent number of tag names
;;assuming the first 3 tags are GROUP, MJD, STAR

if keyword_set(output) then begin
  print,''
  print,'!!!Note, only BVIR filter mags will be transformed to standard system!!!!'
  print,''
endif

if nochanges eq 1 then begin
  print,'According to the system, no changes to input!'
  print,''
  stand_st=natural_st
endif

;;this is for 2 filters, which is the minimum
if tagnumber eq 7 then begin
  if keyword_set(output) then begin
    print,tagnames[0],tagnames[1],tagnames[2],tagnames[3],tagnames[4],tagnames[5],tagnames[6],format='(a7,a10,a5,a7,a9,a7,a9,a7,a9)'
  endif
  if keyword_set(outfile) then begin
    openw, outlun, outfile, /get
    printf,outlun,tagnames[0],tagnames[1],tagnames[2],tagnames[3],tagnames[4],tagnames[5],tagnames[6],format='(a7,a10,a5,a7,a9,a7,a9,a7,a9)'
  endif
  for i=0,n_elements(stand_st)-1 do begin
    if keyword_set(output) then begin
      print,stand_st[i].(0),stand_st[i].(1),stand_st[i].(2),stand_st[i].(3),stand_st[i].(4),stand_st[i].(5),stand_st[i].(6),format='(i6,f11.4,i5,f7.2,f9.2,f7.2,f9.2)'
    endif
    if keyword_set(outfile) then begin
      printf,outlun,stand_st[i].(0),stand_st[i].(1),stand_st[i].(2),stand_st[i].(3),stand_st[i].(4),stand_st[i].(5),stand_st[i].(6),format='(i6,f11.4,i5,f7.2,f9.2,f7.2,f9.2)'
    endif
  endfor
  if keyword_set(outfile) then begin
    free_lun,outlun
  endif
endif

;;this is for 3 filters
if tagnumber eq 9 then begin
  if keyword_set(output) then begin
    print,tagnames[0],tagnames[1],tagnames[2],tagnames[3],tagnames[4],tagnames[5],tagnames[6],tagnames[7],tagnames[8],format='(a7,a10,a5,a7,a9,a7,a9,a7,a9,a7,a9)'
  endif
  if keyword_set(outfile) then begin
    openw, outlun, outfile, /get
    printf,outlun,tagnames[0],tagnames[1],tagnames[2],tagnames[3],tagnames[4],tagnames[5],tagnames[6],tagnames[7],tagnames[8],format='(a7,a10,a5,a7,a9,a7,a9,a7,a9,a7,a9)'
  endif
  for i=0,n_elements(stand_st)-1 do begin
    if keyword_set(output) then begin
      print,stand_st[i].(0),stand_st[i].(1),stand_st[i].(2),stand_st[i].(3),stand_st[i].(4),stand_st[i].(5),stand_st[i].(6),stand_st[i].(7),stand_st[i].(8),format='(i6,f11.4,i5,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2)'
    endif
    if keyword_set(outfile) then begin
      printf,outlun,stand_st[i].(0),stand_st[i].(1),stand_st[i].(2),stand_st[i].(3),stand_st[i].(4),stand_st[i].(5),stand_st[i].(6),stand_st[i].(7),stand_st[i].(8),format='(i6,f11.4,i5,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2)'
    endif
  endfor
  if keyword_set(outfile) then begin
    free_lun,outlun
  endif
endif

;;this is for 4 filters
if tagnumber eq 11 then begin
  if keyword_set(output) then begin
    print,tagnames[0],tagnames[1],tagnames[2],tagnames[3],tagnames[4],tagnames[5],tagnames[6],tagnames[7],tagnames[8],tagnames[9],tagnames[10],format='(a7,a10,a5,a7,a9,a7,a9,a7,a9,a7,a9,a7,a9)'
  endif
  if keyword_set(outfile) then begin
    openw, outlun, outfile, /get
    printf,outlun,tagnames[0],tagnames[1],tagnames[2],tagnames[3],tagnames[4],tagnames[5],tagnames[6],tagnames[7],tagnames[8],tagnames[9],tagnames[10],format='(a7,a10,a5,a7,a9,a7,a9,a7,a9,a7,a9,a7,a9)'
  endif
  for i=0,n_elements(stand_st)-1 do begin
    if keyword_set(output) then begin
      print,stand_st[i].(0),stand_st[i].(1),stand_st[i].(2),stand_st[i].(3),stand_st[i].(4),stand_st[i].(5),stand_st[i].(6),stand_st[i].(7),stand_st[i].(8),stand_st[i].(9),stand_st[i].(10),format='(i6,f11.4,i5,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2)'
    endif
    if keyword_set(outfile) then begin
      printf,outlun,stand_st[i].(0),stand_st[i].(1),stand_st[i].(2),stand_st[i].(3),stand_st[i].(4),stand_st[i].(5),stand_st[i].(6),stand_st[i].(7),stand_st[i].(8),stand_st[i].(9),stand_st[i].(10),format='(i6,f11.4,i5,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2)'
    endif
  endfor
  if keyword_set(outfile) then begin
    free_lun,outlun
  endif
endif

;;this is for 5 filters
if tagnumber eq 13 then begin
  if keyword_set(output) then begin
    print,tagnames[0],tagnames[1],tagnames[2],tagnames[3],tagnames[4],tagnames[5],tagnames[6],tagnames[7],tagnames[8],tagnames[9],tagnames[10],tagnames[11],tagnames[12],format='(a7,a10,a5,a7,a9,a7,a9,a7,a9,a7,a9,a7,a9,a7,a9)'
  endif
  if keyword_set(outfile) then begin 
    openw, outlun, outfile, /get
    printf,outlun,tagnames[0],tagnames[1],tagnames[2],tagnames[3],tagnames[4],tagnames[5],tagnames[6],tagnames[7],tagnames[8],tagnames[9],tagnames[10],tagnames[11],tagnames[12],format='(a7,a10,a5,a7,a9,a7,a9,a7,a9,a7,a9,a7,a9,a7,a9)'
  endif
  for i=0,n_elements(stand_st)-1 do begin
    if keyword_set(output) then begin
      print,stand_st[i].(0),stand_st[i].(1),stand_st[i].(2),stand_st[i].(3),stand_st[i].(4),stand_st[i].(5),stand_st[i].(6),stand_st[i].(7),stand_st[i].(8),stand_st[i].(9),stand_st[i].(10),stand_st[i].(11),stand_st[i].(12),format='(i6,f11.4,i5,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2)'
    endif 
    if keyword_set(outfile) then begin
      printf,outlun,stand_st[i].(0),stand_st[i].(1),stand_st[i].(2),stand_st[i].(3),stand_st[i].(4),stand_st[i].(5),stand_st[i].(6),stand_st[i].(7),stand_st[i].(8),stand_st[i].(9),stand_st[i].(10),stand_st[i].(11),stand_st[i].(12),format='(i6,f11.4,i5,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2,f7.2,f9.2)'
    endif
  endfor
  if keyword_set(outfile) then begin
    free_lun,outlun
  endif
endif

end
