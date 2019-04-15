pro lpp_image_name_trans,inputname,outnamest,noimproddir=noimproddir

if n_params() eq 0 then begin
  print,'Syntax- LPP_image_name_trans,inputname,outnamest,noimproddir=noimproddir'
  return
endif

imagenamest={ori:'', dir: '', root:'', cimg:'',sobj:'',cobj:'', cwcs:'', cnew:'', ctwp:'', cfwp:'', ctcv:'', cfcv:'', ctsb:'', cfsb:'', cph:'', ctph:'', sbph:'', cand:'', sobjdir:'./' , fwhm:'', obj:'', apt:'', aptdat:'', aptsub:'', aptsubdat:'', psf:'', psfdat:'', psfsub:'', psfsubdat:'', psffitarr:'',standrd:'', standxy:'', objectrd:'', sky:'', apass:'', zero:''}

dir=strmid(inputname[0],0,strpos(inputname[0],'/',/REVERSE_SEARCH))
imagedir=''
proddir=''
if strmid(dir,strlen(dir)-5,5) eq 'image' then begin
  dir=strmid(dir,0,strlen(dir)-5)
  imagedir='image/'
  proddir='prod/'
endif
if strmid(dir,strlen(dir)-4,4) eq 'prod' then begin
  dir=strmid(dir,0,strlen(dir)-4)
  imagedir='prod/'
  proddir='dir/'
endif
if dir eq '' or dir eq '.' then dir='./'
if strmid(dir,strlen(dir)-1,1) ne '/' then dir=dir+'/'
if keyword_set(noimproddir) then begin
  imagedir=''
  proddir=''
endif

imagenamest.dir=dir
imagenamest.ori=inputname[0]
;dirparts1=strsplit(inputname[0],'/',/extract)
;imagename=dirparts1[n_elements(dirparts1)-1]
;another option to get imagename
imagename=strmid(inputname[0],strpos(inputname[0],'/',/REVERSE_SEARCH)+1)
;print,imagename

strreplace,imagename,'_c.fit',''
strreplace,imagename,'_sobj.fit',''
strreplace,imagename,'_cobj.fit',''
strreplace,imagename,'_cnew.fit',''
strreplace,imagename,'_cwcs.fit',''
strreplace,imagename,'_ctwp.fit',''
strreplace,imagename,'_cfwp.fit',''
strreplace,imagename,'_ctcv.fit',''
strreplace,imagename,'_cfcv.fit',''
strreplace,imagename,'_ctsb.fit',''
strreplace,imagename,'_cfsb.fit',''
strreplace,imagename,'_cph.fit',''
strreplace,imagename,'_ctph.fit',''
strreplace,imagename,'_sbph.fit',''
strreplace,imagename,'_cand.fit',''
strreplace,imagename,'_fwhm.txt',''
strreplace,imagename,'_obj.txt',''
strreplace,imagename,'_apt.txt',''
strreplace,imagename,'_apt.dat',''
strreplace,imagename,'_aptsub.txt',''
strreplace,imagename,'_aptsub.dat',''
strreplace,imagename,'_psf.txt',''
strreplace,imagename,'_psf.dat',''
strreplace,imagename,'_psfsub.txt',''
strreplace,imagename,'_psfsub.dat',''
strreplace,imagename,'_psffitarr.fit',''
strreplace,imagename,'_standrd.txt',''
strreplace,imagename,'_standxy.txt',''
strreplace,imagename,'_sky.txt',''
strreplace,imagename,'_apass.dat',''
strreplace,imagename,'_zero.txt',''
strreplace,imagename,'.fit',''
imagenamest.root=imagename

imagenamest.cimg=dir + imagedir + imagenamest.root + '_c.fit'
imagenamest.sobj=dir + proddir  + imagenamest.root + '_sobj.fit'
imagenamest.cobj=dir + proddir  + imagenamest.root + '_cobj.fit'
imagenamest.cnew=dir + imagedir + imagenamest.root + '_cnew.fit'
imagenamest.cwcs=dir + proddir  + imagenamest.root + '_cwcs.fit'
imagenamest.ctwp=dir + imagedir + imagenamest.root + '_ctwp.fit'
imagenamest.cfwp=dir + imagedir + imagenamest.root + '_cfwp.fit'
imagenamest.ctcv=dir + imagedir + imagenamest.root + '_ctcv.fit'
imagenamest.cfcv=dir + imagedir + imagenamest.root + '_cfcv.fit'
imagenamest.ctsb=dir + imagedir + imagenamest.root + '_ctsb.fit'
imagenamest.cfsb=dir + imagedir + imagenamest.root + '_cfsb.fit'
imagenamest.cph =dir + imagedir + imagenamest.root + '_cph.fit'
imagenamest.ctph=dir + imagedir + imagenamest.root + '_ctph.fit'
imagenamest.sbph=dir + imagedir + imagenamest.root + '_sbph.fit'
imagenamest.cand=dir + imagedir + imagenamest.root + '_cand.fit'
imagenamest.fwhm=dir + imagedir + imagenamest.root + '_fwhm.txt'
imagenamest.obj=dir + imagedir + imagenamest.root + '_obj.txt'
imagenamest.apt=dir + imagedir + imagenamest.root + '_apt.txt'
imagenamest.aptdat=dir + imagedir + imagenamest.root + '_apt.dat'
imagenamest.aptsub=dir + imagedir + imagenamest.root + '_aptsub.txt'
imagenamest.aptsubdat=dir + imagedir + imagenamest.root + '_aptsub.dat'
imagenamest.psf=dir + imagedir + imagenamest.root + '_psf.txt'
imagenamest.psfdat=dir + imagedir + imagenamest.root + '_psf.dat'
imagenamest.psfsub=dir + imagedir + imagenamest.root + '_psfsub.txt'
imagenamest.psfsubdat=dir + imagedir + imagenamest.root + '_psfsub.dat'
imagenamest.psffitarr=dir + imagedir + imagenamest.root + '_psffitarr.fit'
imagenamest.standrd=dir + imagedir + imagenamest.root + '_standrd.txt'
;imagenamest.standxy=dir + imagedir + imagenamest.root + '_standxy.txt'
imagenamest.objectrd=dir + imagedir + imagenamest.root + '_objectrd.txt'
;imagenamest.objectxy=dir + imagedir + imagenamest.root + '_objectxy.txt'
imagenamest.sky=dir + imagedir + imagenamest.root + '_sky.txt'
imagenamest.zero=dir + imagedir + imagenamest.root + '_zero.txt'
imagenamest.apass=dir + imagedir + imagenamest.root + '_apass.dat'

outnamest=imagenamest

end
