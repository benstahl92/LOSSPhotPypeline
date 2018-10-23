import pandas as pd
from pyzaphotdb import zaphot_search_by_objname, storelocation

def proc_SN(objname):
	'''
	query database to find images, and move them to appropriate place
	NB: objname should include prefix!
	'''

	res = zaphot_search_by_objname(objname)
	if len(res) == 0:
		return None