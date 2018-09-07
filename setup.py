'''
This is a basic setup file that suggests modifications to path variables.

It should be run once from the code's root directory and then the .bashrc file should be modified based on the suggestions
'''

import os
import shutil
import sys
from pexpect.exceptions import ExceptionPexpect

try:
	import pidly
except ModuleNotFoundError:
	sys.exit('Please install the python package "pIDLy" before proceeding.')

# get root directory of codebase
root_dir = os.path.realpath('.')

# check that idl is properly configured
try:
	pidly.IDL()
except ExceptionPexpect:
	sys.exit('IDL executable not found. Make sure it is set appropriately in your .bashrc file')

# check that required executables can be found
required_execs = ['ds9, sextractor']
for ex in required_execs:
	s = shutil.which(ex)
	if s == '':
		sys.exit('{} not found!'.format(ex))

# check that ISIS is installed
if not 'ISISPATH' in os.environ:
	sys.exit('ISISPATH not set or ISIS is not installed. Cannot proceed.')

# write scripts with sextractor config path and make them executable

with open(os.path.join(root_dir, 'LOSSPhotPypeline', 'conf', 'lpp_templates', 'LPP-Ssex-kait.template.sh'), 'r') as f:
	s = f.read()
with open(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_bin', 'LPP-Ssex-kait.sh'), 'w') as f:
	f.write(s.replace('SEXCONFPATH=', 'SEXCONFPATH={}/'.format(os.path.join(root_dir, 'LOSSPhotPypeline', 'conf', 'sextractor_config'))))
st = os.stat(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_bin', 'LPP-Ssex-kait.sh'))
os.chmod(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_bin', 'LPP-Ssex-kait.sh'), st.st_mode | 0o111)

with open(os.path.join(root_dir, 'LOSSPhotPypeline', 'conf', 'lpp_templates', 'LPP_get_fwhm.template.sh'), 'r') as f:
	s = f.read()
with open(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_bin', 'LPP_get_fwhm.sh'), 'w') as f:
	f.write(s.replace('sexconfpath=', 'sexconfpath={}/'.format(os.path.join(root_dir, 'LOSSPhotPypeline', 'conf', 'sextractor_config'))))
st = os.stat(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_bin', 'LPP_get_fwhm.sh'))
os.chmod(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_bin', 'LPP_get_fwhm.sh'), st.st_mode | 0o111)

# write so path into get_local_sky procedure
with open(os.path.join(root_dir, 'LOSSPhotPypeline', 'conf', 'lpp_templates', 'get_local_sky.template.pro'), 'r') as f:
	s = f.read()
with open(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_idl', 'get_local_sky.pro'), 'w') as f:
	f.write(s.replace('sopath=', 'sopath="{}/"'.format(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_c'))))

print('\nNB: local_sky_sub.so is compiled from local_sky_sub.c --- you will likely need to recompile on your machine.')

print('\nEnsure that the following IDL packages are installed:')
print('\tAstrolib')

print('\nAdd the following to your .bashrc file (and then source it!):\n')
print('export PATH="{}:$PATH"'.format(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_bin')))
print('export IDL_PATH=+{}:$IDL_PATH'.format(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_idl')))
print('export PYTHONPATH={}:$PYTHONPATH'.format(root_dir))
