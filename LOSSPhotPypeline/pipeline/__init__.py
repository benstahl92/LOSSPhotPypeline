from LOSSPhotPypeline.pipeline.LPP import LPP

def start_pipeline(targetname):
	return LPP(targetname)

def run_pipeline(targetname):
	p = LPP(targetname, interactive = False)
	p.run()
	return p

def add_new_images(targetname, new_image_list):
	p = LPP(targetname, interactive = False)
	p.process_new_images(new_image_list)
	return p

def galaxy_subtract(targetname):
	pass

def run_pipeline_bulk():
	pass

