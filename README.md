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
    * pyzaphotdb (not publicly available yet, but not needed for bulk of features)
    * sewpy (<https://github.com/megalut/sewpy>)
* IDL 8.5
    * ASTROLIB (<https://idlastro.gsfc.nasa.gov>)
* DS9 (<http://ds9.si.edu/site/Home.html>)
* ISIS (<http://www2.iap.fr/users/alard/package.html>)
* SExtractor (<https://www.astromatic.net/software/sextractor>)

## Installation and Setup

1. Install Dependencies

    * Python and packages without links would ideally be installed with [Anaconda](https://www.anaconda.com) or `pip`
    * Python packages with links should be installed in accordance with the instructions at those links
    * IDL should be installed so that typing `idl` in a shell starts it *with* ASTROLIB system variables added
    * DS9 should be installed so that typing `ds9` in a shell starts it
    * ISIS should be installed, and the system variable `ISISPATH` should be set appropriately
    * SExtractor should be installed so that typing `sex` in a shell runs it

2. Download LOSSPhotPypeline

   ```sh
   git clone https://github.com/benstahl92/LOSSPhotPypeline
   ```

3. Run setup.py

   The `setup.py` script sets hard-coded paths in the code base where needed and does some basic checks to make sure needed packages and executables are installed appropriately. Note that this is **not** a normal python setup script. Once you have downloaded LOSSPhotPypeline and moved it where you'd like it live, run this script from the LOSSPhotPypeline root directory.

   ```sh
   # from within the LOSSPhotPypeline root directory
   python setup.py
   ```

   The script will print "Done!" if it runs all the way through successfully.

4. Set Environment Variables

   Your system needs to know where to find the LOSSPhotPypeline code base. The setup.py script will print three commands that you can use to set these environment variables. It is recommended that you include these commands in your bash login file (e.g. `~/.bashrc`). An example of these three commands follows:

    ```sh
    export PATH="<LOSSPhotPypeline_DIRECTORY>/LOSSPhotPypeline/utils/LPP_bin:$PATH"
    export IDL_PATH=+<LOSSPhotPypeline_DIRECTORY>/LOSSPhotPypeline/utils/LPP_idl:$IDL_PATH
    export PYTHONPATH=<LOSSPhotPypeline_DIRECTORY>:$PYTHONPATH
    ```

## Running the Pipeline

LOSSPhotPypeline is organized into three subpackages:

* ```LOSSPhotPypeline.pipeline``` provides top-level access to the pipeline and is responsible for running all steps. In normal use, this is the only subpackage that the user will directly interact with.
* ```LOSSPhotPypeline.image``` provides a framework for directly interacting with image files (reading properties, calculating quantities, subtracting host-galaxy light, doing photometry, etc.).
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
   >>> sn = lpp.start_pipeline('sntest')
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
   photlistfile        sntest.photlist
   forcecolorterm      none
   ```

    * The three blank entries must be added --- "targetra" and "targetdec" are the coordinates of the target in decimal degrees, and "refname" is the filename (including relative path) of the image to be used when for determining the coordinates of reference stars. 

    * If galaxy subtraction is desired, set "photsub" to "yes". Note that the pipeline will expect to find template images of host galaxy in a directory called "templates". *BVRI* images should always use template images from the Nickel telescope (even if the science images are from KAIT --- the pipeline will automatically rescale Nickel template images for use with KAIT).

    * Unless you know what you are doing, don't change anything else.

    * Finally, save the configuration as "sntest.conf"

4. Create photlist file

   As you will see in the configuration file, the pipeline expects there to be a file named "sntest.photlist". This file should contain a single column where each line is the name (including relative path) of an image containing the target to run the pipeline on. The images need not be located in the same place, however it is recommended to organize them in some sort of reasonable way. The pipeline will cause new files to be written in the same directories as the images.

5. Run the pipeline

   Re-initialize and run the pipeline:

   ```python
   >>> sn = lpp.start_pipeline('sntest')
   >>> sn.run()
   ```

   The pipeline will run through all steps automatically, and keep you apprised of the progress (both through terminal output and a log maintained in "sntest.log"). In the end, this will yield a "lightcurve" directory containing plots and ```.dat``` files based on photometry via a number of different apertures.

### Miscellaneous notes on running the pipeline

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

   After running the pipeline, there may be cases where one would like to remove points from a light curve, add new images, check the calibration, etc. Common cases such as these can be handled with minimal effort.

   ```python
   >>> sn.go_to()
   [...]
   ```
   ```
    Choose an option:

    primary reduction steps:
    0 --- load_images
    1 --- check_images
    2 --- find_ref_stars
    3 --- match_refcal_stars
    4 --- do_galaxy_subtraction_all_image
    5 --- do_photometry_all_image
    6 --- get_sky_all_image
    7 --- do_calibration
    8 --- get_zeromag_all_image
    9 --- get_limmag_all_image
    10 --- generate_lc
    11 --- write_summary

    additional options:
    n  --- add new image(s) by filename(s)
    nf --- add new images from file of names
    p  --- plot light curve from file
    c  --- cut points from specific light curve
    cr --- cut points from specific raw light curve and regenerate subsequent light curves
    q  --- quit
   
   selection >
   ```

   By selecting the appropriate option from "additional options", one can achieve most of these tasks. Notice also the listing of "primary reduction steps", which can be used to reset the pipeline to a certain place in the process if needed (particularly useful if you want to do the calibration manually).

* Variables and methods

   For those that may need to accomplish more sophisticated tasks than those enumerated above, the following methods can be used see all available instance variables and methods:

   ```python
   >>> sn.show_variables()
   [...]
   >>> sn.show_methods()
   [...]
   ```

### A note on calibration

Calibration (as done in the `do_calibration` reduction step) is by far the stage of the pipeline that requires the most supervision. While running in non-interactive mode, calibration decisions are made as follows:

  1. Select only the reference stars that are common to all images being processed. If less than 2 reference stars meet this criterion, then "all images" will be loosened to 95% of images. The tolerance will continue to loosen in increments of 5% until at least 2 reference stars satisfy the criterion, however if the tolerance increments below 80% the calibration process exits with a warning. Note: the numbers involved in this check are all instance attributes and are hence adjustable, furthermore this check can be completely turned off by setting the instance attribute `cal_use_common_ref_stars` to `False`.

  2. Assuming step 1 is successfully completed, all images will be calibrated using all available reference stars.

  3. After the first time step 2 is performed, the measured magnitudes of each reference star in every image for each filter/system combination are tabulated and used to identify images that differ by 3 standard deviations from the mean measured magnitude of that reference star in that filter/system. Such differing images are removed, as it is likely that the underlying images were contaminated in some way. These images are logged internally and png versions are saved in the calibration directory for easy review. This step is only performed one time.

  4. After step 3 is run, step 2 is performed again. If the difference between the median measured magnitude and reference magnitude exceeds 0.05 mag for any calibration star, the one with the largest difference is cut. This procedure iterates until either the aforementioned difference is less than 0.05 mag for all reference stars or only two reference stars remain. If the former, the calibration process ends successfully. If the latter, the tolerance of 0.05 mag is incremented up by 0.05 mag and the process repeats. If the tolerance reaches 0.2 mag without ending successfully, the calibration process exits with a warning.

At the very least, it is important to do a visual inspection of the final reference stars chosen by this process (this can be done by looking at the "ref_stars.png" file that gets written in the calibration directory). If the calibration is unsatisfactory, it is recommend to run the process in interactive mode --- this affords much more control over the steps above. To do this one, one needs only to start the pipeline, set the instance attribute `interactive` to `True`, and go to the appropriate step.

## FAQ
