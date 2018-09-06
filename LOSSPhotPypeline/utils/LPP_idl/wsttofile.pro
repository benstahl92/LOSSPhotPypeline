pro wsttofile,filename,st,append=append

if N_params() eq 0 then begin
       print,'Syntax: wsttofile,filename,st,append=append'
       return
endif

if not keyword_set(append) then begin
  writefits,filename,''
endif

mwrfits,st,filename

end
