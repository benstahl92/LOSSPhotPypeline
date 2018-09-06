pro lpp_rebin_from_nickel,nickelimname,newim,savefile=savefile

if n_params() eq 0 then begin
    print,'LPP_rebin_from_nickel,nickelimname,newim,savefile=savefile'
    return
endif

;; pixscale=0.7965 for kait
;; pixscale=0.3702 for nickel

scale=0.3700/0.7965

nim=mrdfits(nickelimname,0,head,/dscale,/silent)

naxis1=sxpar(head,'NAXIS1')
naxis2=sxpar(head,'NAXIS2')

naxis1k=500
naxis2k=500

newnaxis1=round(naxis1*scale)
newnaxis2=round(naxis2*scale)

maxnaxis1=newnaxis1
maxnaxis2=newnaxis2
;print,naxis1,naxis2
;print,scale
;print,newnaxis1,newnaxis2

if maxnaxis1 gt naxis1k then maxnaxis1=naxis1k
if maxnaxis2 gt naxis2k then maxnaxis2=naxis2k
;print,maxnaxis1,maxnaxis2

hrebin, nim, head, newim, newhead, newnaxis1,newnaxis2
;help,newim,newhead

bak=median(newim)
newimk=dblarr(naxis1k,naxis2k) + bak
newimk[0:maxnaxis1-1,0:maxnaxis2-1]=newim[0:maxnaxis1-1,0:maxnaxis2-1]
;help,newimk,newhead

time=sxpar(head,'DATE-STA')
if time eq 0 then begin
  time=sxpar(head,'DATE-BEG')
endif
year=strmid(time,0,4)
month=strmid(time,5,2)
day=strmid(time,8,2)
date=day+'/'+month+'/'+year
ut=strmid(time,11,strlen(time)-11)
sxdelpar,newhead,['DATE-OBS','UT']
sxaddpar,newhead,'UT',      ut,  ' add as style for kait image',after='FILTNAM'
sxaddpar,newhead,'DATE-OBS',date,' add as style for kait image',after='FILTNAM'

newim=newimk

if n_elements(savefile) eq 1 then begin
  writefits,savefile,newimk,newhead
endif

end
