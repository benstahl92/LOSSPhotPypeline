class FileNames(object):
    '''standardize and handle all file names/types encountered by pipeline'''

    def __init__(self, name):
        '''do everything upon instantiation'''

        # determine root file name
        self.root = name
        self.root = self.root.replace('_c.fit','')
        self.root = self.root.replace('_sobj.fit','')
        self.root = self.root.replace('_cobj.fit','')
        self.root = self.root.replace('_cnew.fit','')
        self.root = self.root.replace('_cwcs.fit','' )
        self.root = self.root.replace('_ctwp.fit','' )
        self.root = self.root.replace('_cfwp.fit','' )
        self.root = self.root.replace('_ctcv.fit','' )
        self.root = self.root.replace('_cfcv.fit','' )
        self.root = self.root.replace('_ctsb.fit','' )
        self.root = self.root.replace('_cfsb.fit','' )
        self.root = self.root.replace('_cph.fit',''  )
        self.root = self.root.replace('_ctph.fit','' )
        self.root = self.root.replace('_sbph.fit','' )
        self.root = self.root.replace('_cand.fit','' )
        self.root = self.root.replace('_fwhm.txt','' )
        self.root = self.root.replace('_obj.txt',''  )
        self.root = self.root.replace('_psfstar.txt',''  )
        self.root = self.root.replace('_apt.txt',''  )
        self.root = self.root.replace('_apt.dat',''  )
        self.root = self.root.replace('_psf.txt',''  )
        self.root = self.root.replace('_standrd.txt','')
        self.root = self.root.replace('_standxy.txt','')
        self.root = self.root.replace('_objectrd.txt','')
        self.root = self.root.replace('_objectxy.txt','')
        self.root = self.root.replace('_sky.txt','')
        self.root = self.root.replace('_apass.dat','')
        self.root = self.root.replace('_zero.txt','')
        self.root = self.root.replace('.fit','')
        self.root = self.root.replace('.fts','')

        # generate all filenames from root
        self.cimg      = self.root + '_c.fit'
        self.sobj      = self.root + '_sobj.fit'
        self.cobj      = self.root + '_cobj.fit'
        self.cnew      = self.root + '_cnew.fit'
        self.cwcs      = self.root + '_cwcs.fit'
        self.ctwp      = self.root + '_ctwp.fit'
        self.cfwp      = self.root + '_cfwp.fit'
        self.ctcv      = self.root + '_ctcv.fit'
        self.cfcv      = self.root + '_cfcv.fit'
        self.ctsb      = self.root + '_ctsb.fit'
        self.cfsb      = self.root + '_cfsb.fit'
        self.cph       = self.root + '_cph.fit'
        self.ctph      = self.root + '_ctph.fit'
        self.sbph      = self.root + '_sbph.fit'
        self.cand      = self.root + '_cand.fit'
        self.fwhm_fl   = self.root + '_fwhm.txt'
        self.obj       = self.root + '_obj.txt'
        self.psfstar   = self.root + '_psfstar.txt'
        self.apt       = self.root + '_apt.txt'
        self.aptdat    = self.root + '_apt.dat'
        self.psf       = self.root + '_psf.txt'
        self.psfsub    = self.root + '_psfsub.txt'
        self.psffitarr = self.root + '_psffitarr.fit'
        self.psfdat    = self.root + '_psf.dat'
        self.psfsubdat = self.root + '_psfsub.dat'
        self.standrd   = self.root + '_standrd.txt'
        self.standxy   = self.root + '_standxy.txt'
        self.objectrd  = self.root + '_objectrd.txt'
        self.objectxy  = self.root + '_objectxy.txt'
        self.skytxt    = self.root + '_sky.txt'
        self.skyfit    = self.root + '_sky.fit'
        self.apass     = self.root + '_apass.dat'
        self.zerotxt   = self.root + '_zero.txt'
