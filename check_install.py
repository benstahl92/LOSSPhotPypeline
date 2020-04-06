'''
This is a basic setup file that sets paths and suggests modifications to path variables.
Run this once from the code's root directory and then modify your bash login file accordingly
'''

import os
import shutil
import sys

# get root directory of codebase
root_dir = os.path.realpath('.')

# check that required executables can be found
required_execs = ['ds9, sex']
for ex in required_execs:
	s = shutil.which(ex)
	if s == '':
		sys.exit('{} not found!'.format(ex))

# check that ISIS is installed
if not 'ISISPATH' in os.environ:
	sys.exit('ISISPATH not set or ISIS is not installed. Cannot proceed.')

# write so path into get_local_sky procedure
with open(os.path.join(root_dir, 'LOSSPhotPypeline', 'conf', 'lpp_templates', 'get_local_sky.template.pro'), 'r') as f:
	s = f.read()
with open(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_idl', 'get_local_sky.pro'), 'w') as f:
	f.write(s.replace('sopath=', 'sopath="{}/"'.format(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_c'))))

print('\nNB: local_sky_sub.so is compiled from local_sky_sub.c --- you will likely need to recompile on your machine.')

print('\nAdd the following to your .bashrc file (and then source it!):\n')
print('export PATH="{}:$PATH"'.format(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_bin')))
print('export IDL_PATH=+{}:$IDL_PATH'.format(os.path.join(root_dir, 'LOSSPhotPypeline', 'utils', 'LPP_idl')))
print('export PYTHONPATH={}:$PYTHONPATH'.format(root_dir))

print('\nDone!')
