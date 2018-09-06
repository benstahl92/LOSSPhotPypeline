pro lpp_readcolst,filename,outst,format=format,output=output

if n_params() eq 0 then begin
  print,'Syntax- readcolst,filename,outst'
  print,'Note: The first line must contain the tag names for each column'
  return
endif

line=''
openr,lunr,/get_lun,filename
readf,lunr,line
close,lunr
free_lun,lunr


tages=strsplit(line,/extract)
tages=strtrim(tages,2)
if keyword_set(output) then begin
  print,tages
endif

tnb=n_elements(tages)

if keyword_set(format) then begin
  ;   Remove blanks from format string
  frmt = strupcase(strcompress(format,/REMOVE))   
  remchar, frmt, '('         ;Remove parenthesis from format
  remchar, frmt, ')'   
  formats=strsplit(frmt,',',/extract)
  fnb=n_elements(formats)
  if fnb lt tnb then begin
    formats=[formats,replicate('D',tnb-fnb)]
  endif
endif else begin
  formats=replicate('D',tnb)
endelse

i=0
case formats[i] of
  'F' : inival=0.0
  'A' : inival=''
  'D' : inival=0d0
  else: inival=0.0
endcase
sttmp=create_struct(tages[0], inival)
for i=1,tnb-1 do begin
  case formats[i] of
    'F' : inival=0.0
    'A' : inival=''
    'D' : inival=0d0
    else: inival=0.0
  endcase
  sttmp=create_struct(sttmp, tages[i], inival)
endfor

formatstmp=""
nbtmp=n_elements(formats)
if nbtmp eq 1 then begin
  formatstmp=formatstmp+formats[0]
endif else begin
  for i=0,n_elements(formats)-2 do begin
    formatstmp=formatstmp+formats[i]+','
  endfor
  formatstmp=formatstmp+formats[i]
endelse
formats=formatstmp
if keyword_set(output) then begin
  print,'reading format is : ',formats
endif

case tnb of 
1 : begin
    readcol,filename,v1,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    end
2 : begin
    readcol,filename,v1,v2,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    end
3 : begin
    readcol,filename,v1,v2,v3,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    end
4 : begin
    readcol,filename,v1,v2,v3,v4,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    end
5 : begin
    readcol,filename,v1,v2,v3,v4,v5,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    end
6 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    end
7 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    end
8 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    end
9 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    end
10 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    st.(9)=v10
    end
11 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    st.(9)=v10
    st.(10)=v11
    end
12 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    st.(9)=v10
    st.(10)=v11
    st.(11)=v12
    end
13 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    st.(9)=v10
    st.(10)=v11
    st.(11)=v12
    st.(12)=v13
    end
14 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    st.(9)=v10
    st.(10)=v11
    st.(11)=v12
    st.(12)=v13
    st.(13)=v14
    end
15 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    st.(9)=v10
    st.(10)=v11
    st.(11)=v12
    st.(12)=v13
    st.(13)=v14
    st.(14)=v15
    end
16 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    st.(9)=v10
    st.(10)=v11
    st.(11)=v12
    st.(12)=v13
    st.(13)=v14
    st.(14)=v15
    st.(15)=v16
    end
17 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    st.(9)=v10
    st.(10)=v11
    st.(11)=v12
    st.(12)=v13
    st.(13)=v14
    st.(14)=v15
    st.(15)=v16
    st.(16)=v17
    end
18 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    st.(9)=v10
    st.(10)=v11
    st.(11)=v12
    st.(12)=v13
    st.(13)=v14
    st.(14)=v15
    st.(15)=v16
    st.(16)=v17
    st.(17)=v18
    end
19 : begin
    readcol,filename,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,skipline=1,count=count,format=formats
    st=replicate(sttmp,count)
    st.(0)=v1
    st.(1)=v2
    st.(2)=v3
    st.(3)=v4
    st.(4)=v5
    st.(5)=v6
    st.(6)=v7
    st.(7)=v8
    st.(8)=v9
    st.(9)=v10
    st.(10)=v11
    st.(11)=v12
    st.(12)=v13
    st.(13)=v14
    st.(14)=v15
    st.(15)=v16
    st.(16)=v17
    st.(17)=v18
    st.(18)=v19
    end
else: st=[]
endcase

outst=st

end
