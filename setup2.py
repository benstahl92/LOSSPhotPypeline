'''
This is a basic setup file that suggests modifications to path variables.

It should be run once from the code's root directory and then the .bashrc file should be modified based on the suggestions
'''
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
'''

import os
import glob
import shutil
from setuptools import setup, find_packages, Command


class CleanCommand(Command):
    '''Custom clean command to tidy up the project root'''

    CLEAN_FILES = './build ./dist ./*.egg-info'.split(' ')
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        here = os.path.dirname(os.path.abspath(__file__))
        for path_spec in self.CLEAN_FILES:
            # Make paths absolute and relative to this path
            abs_paths = glob.glob(os.path.normpath(os.path.join(here, path_spec)))
            for path in [str(p) for p in abs_paths]:
                if not path.startswith(here):
                    # Die if path in CLEAN_FILES is absolute + outside this directory
                    raise ValueError('{} is not a path inside {}'.format(path, here))
                print('removing {}'.format(os.path.relpath(path)))
                shutil.rmtree(path)


dep = ['numpy >= 1.14.2']
pack = find_packages()
print(pack)

setup(
	name = 'LOSSPhotPypeline',
	version = '0.1.dev0',
	description = 'Lick Observatory Supernova Search Photometry Reduction Pipeline',
	author = 'Benjamin Stahl, WeiKang Zheng',
	author_email = 'benjamin_stahl@berkeley.edu',
	url = 'https://github.com/benstahl92/LOSSPhotPypeline',
	license = 'MIT',
	packages = pack,
	package_data = {key: ['*'] for key in pack},	
	include_package_data = True,
	zip_safe = False,
	install_requires = dep,
	cmdclass = {'clean': CleanCommand})
