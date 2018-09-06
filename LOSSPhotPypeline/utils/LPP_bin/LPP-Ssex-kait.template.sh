
if [ $# -le 0 ]
then
        echo "Usage:$0 fitfilename(s)"
        exit 0
fi

for file in $*
do

  if [ ! -e $file ]
  then
          echo "File $file not exit!"
          exit 0
  fi
  
  HEAD=`echo $file | sed 's/_c\.fits//' | sed 's/_c\.fit//' |  sed 's/\.fits//' | sed 's/\.fit//' |  sed 's/\.imh//'`
  Sobjfile=${HEAD}_sobj.fit
  Skyfile=${HEAD}_sky.fit
  
  sex_args=" -c $SEXCONFPATH/kait.sex -PARAMETERS_NAME $SEXCONFPATH/kait.par -FILTER_NAME $SEXCONFPATH/gauss_2.0_5x5.conv -STARNNW_NAME $SEXCONFPATH/default.nnw -VERBOSE_TYPE QUIET"
  
  cmd="sextractor $file $sex_args -CATALOG_NAME $Sobjfile -CHECKIMAGE_NAME $Skyfile"
  $cmd

done
