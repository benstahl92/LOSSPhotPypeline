# LOSSPhotPypeline

This is the Lick Observatory Supernova Search Photometry Pipeline. It is designed to perform photometry on images collected with the KAIT and Nickel telescopes at Lick Observatory (though it could be extended to other telescopes). Python is used to automate, organize, and interact with the pipeline, which itself leverages several other languages (IDL, C, bash) and software packages (DS9, ISIS, SExtractor).

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

   Your system needs to know where to find the LOSSPhotPypeline codes. The setup.py script will print three commands that you can use to set these environment variables. It is recommended that you include these commands in your bash login file (e.g., `~/.bashrc`). An example of these three commands follows:

    ```sh
    export PATH="<LOSSPhotPypeline_DIRECTORY>/LOSSPhotPypeline/utils/LPP_bin:$PATH"
    export IDL_PATH=+<LOSSPhotPypeline_DIRECTORY>/LOSSPhotPypeline/utils/LPP_idl:$IDL_PATH
    export PYTHONPATH=<LOSSPhotPypeline_DIRECTORY>:$PYTHONPATH
    ```

## Running the Pipeline

LOSSPhotPypeline is organized by means of three subpackages:

* ```LOSSPhotPypeline.pipeline``` provides top-level access to the pipeline and is responsible for running all steps. In normal use, this is the only subpackage that the user will directly interact with.
* ```LOSSPhotPypeline.image``` provides a framework for directly interacting with image files (reading properties, calculating quantities, doing photometry, etc.).
* ```LOSSPhotPypeline.utils``` provides functionality needed by the pipeline including fetching reference catalogs, plotting light curves, etc.

While full documentation is (someday) on its way, an example of a typical workflow is presented below.

1. Create and enter a working directory for the object (in this case, we call the object "sntest")

   ```sh
   mkdir sntest
   cd sntest
   ```

2. From the python interpreter, import and initialize the pipeline

   ```python
   >>> import LOSSPhotPypeline.pipeline as lpp
   >>> sn = sn = lpp.start_pipeline('sntest')
   ```

   A welcome message will be printed and then (assuming this is the first time running the pipeline in this directory) a template configuration file will be made.

3. Create a configuration file

   The template configuration file will look something like the following:

   ```txt
   targetname          sntest
   targetra
   targetdec
   photsub             no
   calsource           auto
   photmethod          all
   refname
   photlistfile         sntest.photlist
   forcecolorterm      none
   ```

   The three blank entries must be added --- "targetra" and "targetdec" are the coordinates of the target in decimal degrees, and "refname" is the filename (including relative path) of the image to be used when for determining the coordinates of reference stars.

   If galaxy subtraction is desired, set "photsub" to "yes".

   Unless you know what you are doing, don't change anything else.

   Finally, save the configuration as "sntest.conf"

4. Create photlist file

   As you will see in the configuration file, the pipeline expects there to be a file name "sntest.photlist". This file should contain a single column where each line is the name (including relative path) of an image containing the target to run the pipeline on. The images need not be located in the same place, however it is recommended to organize them in some sort of reasonable way. The pipeline will cause new files to be written in the same directories as the images.

5. Run the pipeline

   Re-initialize and run the pipeline:

   ```python
   >>> sn = sn = lpp.start_pipeline('sntest')
   >>> sn.run()
   ```

   The pipeline will run through all steps automatically, and keep you apprised of the progress (both through terminal output and a log maintained in "sntest.log"). In the end, this will yield a "lightcurve" directory containing plots and ```.dat``` files based on photometry via a number of different apertures.

Miscellaneous notes on running the pipeline

* Saving and loading

   The pipeline will automatically save its state after successful completion of each step, but the user may manually save the state as well.

   ```python
   >>> sn.save()
   ```

   This creates or updates "sntest.sav", a binary file containing the pipeline state. The pipeline can be restored to the state in "sntest.sav" as follows:

   ```python
   >>> sn.load()
   ```

* Specific operations

   After running the pipeline, there may be cases where one would like to remove points from a light curve, or add new images, etc. Common cases such as these can be handled with minimal effort.

   ```python
   >>> sn.go_to()

   [...]

   Choose an option:

   primary reduction steps:
   0 --- find_ref_stars
   1 --- get_images
   2 --- do_galaxy_subtraction_all_image (current step)
   3 --- do_photometry_all_image
   4 --- get_sky_all_image
   5 --- do_calibration
   6 --- get_limmag_all_image
   7 --- generate_lc
   
   additional options:
   n  --- add new image(s) by filename(s)
   nf --- add new images from file of names
   p  --- plot light curve from file
   c  --- cut points from specific light curve
   cr --- cut points from raw light curves
   cs --- cut points from standard light curves
   q  --- quit
   
   selection >
   ```

   By selecting the appropriate option from "additional options", one can achieve most of these tasks. Notice also the listing of "primary reduction steps", which can be used to reset the pipeline to a certain place in the process if needed.

* Variables and methods

   For those that may need to accomplish more sophisticated tasks than those enumerated above, the following methods can be used see all available instance variables and methods:

   ```python
   >>> sn.show_variables()
   [...]
   >>> sn.show_methods()
   [...]
   ```
## References

