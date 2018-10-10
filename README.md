# LOSSPhotPypeline

This is the Lick Observatory Supernova Search Photometry Pipeline. It is designed to perform photometry on images collected with the KAIT and Nickel telescopes at Lick Observatory (though it could be extended to other telescopes). Python is used to automate, organize, and interact with the pipeline, which itself leverages several other languages (IDL, C, Bash) and software packages (DS9, ISIS, SExtractor).

## Features

* as automated as possible
* clean python interface (no need to interact directly with other languages/software)
* computationally expensive steps are parallelized
* detailed logging of every step
* easy to start/stop/resume/save/reload at any point in the processing

## Dependencies

* Python 3.x
    * astropy
    * astroquery
    * numpy
    * pandas
    * requests
    * seaborn
    * tqdm
    * AstroSQL (<https://github.com/ketozhang/astroSQL>)
    * p_tqdm (<https://github.com/swansonk14/p_tqdm>)
    * pIDLy (<https://github.com/anthonyjsmith/pIDLy>)
    * pyzaphotdb (not publicly available yet, but not needed for bulk of features)
    * sewpy (<https://github.com/megalut/sewpy>)
* IDL 8.5
    * ASTROLIB (<https://idlastro.gsfc.nasa.gov>)
* DS9 (<http://ds9.si.edu/site/Home.html>)
* ISIS (<http://www2.iap.fr/users/alard/package.html>)
* SExtractor (<https://www.astromatic.net/software/sextractor>)

## Installation and Setup

1. Install Dependencies

    * Python and packages without links would ideally be installed with through [Anaconda](https://www.anaconda.com)
    * Python packages with links should be installed according to the appropriate instructions
    * IDL should be installed so that typing `idl` in a shell starts IDL and automatically adds ASTROLIB system variables
    * DS9 should be installed so that typing `ds9` in a shell starts it
    * ISIS should be installed, and the system variable `ISISPATH` should be set appropriately
    * SExtractor should be installed so that typing `sex` in a shell runs it

2. Download LOSSPhotPypeline

```sh
git clone https://github.com/benstahl92/LOSSPhotPypeline
```

3. Run setup.py

The setup.py script sets paths in files where needed and does some basic checks to make sure needed packages and executables are installed appropriately. Note that this is **not** a normal python setup script. Once you have downloaded LOSSPhotPypeline and moved it where you'd like it live, run this script from LOSSPhotPypeline root directory.

```sh
# from within the LOSSPHotPypeline root directory
python setup.py
```

The script will print "Done!" if it runs all the way through successfully.

4. Set Environment Variables

Your system needs to know where to find the LOSSPhotPypeline codes. The setup.py script will print three commands that you can use to set these environment variables. It is recommended that you include these commands in your bahs login file (e.g., `~/.bashrc`). An example of these three commands follows:

```sh
export PATH="<path to LOSSPhotPypeline>/LOSSPhotPypeline/utils/LPP_bin:$PATH"
export IDL_PATH=+<path to LOSSPhotPypeline>/LOSSPhotPypeline/utils/LPP_idl:$IDL_PATH
export PYTHONPATH=<path to LOSSPhotPypeline>:$PYTHONPATH
```

## Running the Pipeline

## References