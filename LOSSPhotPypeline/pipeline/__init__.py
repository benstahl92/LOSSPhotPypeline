# internal imports
from LOSSPhotPypeline.pipeline.LPP import LPP

# convenience functions to access pipeline

def start_pipeline(targetname):
	'''instantiate pipeline and return it'''
	return LPP(targetname)

def run_pipeline(targetname):
	'''instantiate pipeline in non-interactive mode, run it, and return it'''
	p = LPP(targetname, interactive = False)
	p.run()
	return p
