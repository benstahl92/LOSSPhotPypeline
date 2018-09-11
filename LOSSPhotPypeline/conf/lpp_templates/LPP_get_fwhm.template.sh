#!/bin/bash
sexconfpath=
workdir=./

#this file is for configuration file fwhm.sex
tmp_fwhm_file=tmp_fwhm.cat

if [ $# -le 0 ]
then
        echo "Usage:$0 fitfilename"
        exit 0
fi

filename=$1

HEAD=`echo $filename | sed 's/_c\.fits//' | sed 's/_c\.fit//' |  sed 's/\.fits//' | sed 's/\.fit//' |  sed 's/\.imh//'`

fwhmfile=${HEAD}_fwhm.txt

sextractor $filename -c ${sexconfpath}/fwhm.sex -PARAMETERS_NAME ${sexconfpath}/fwhm.par -FILTER_NAME ${sexconfpath}/gauss_2.0_5x5.conv -STARNNW_NAME ${sexconfpath}/default.nnw

fwhm=`awk '{print $1}' $tmp_fwhm_file | sort | awk ' { a[i++]=$1; } END { x=int((i+1)/2); if (x < (i+1)/2) print (a[x-1]+a[x])/2; else print a[x-1]; }'`
echo $fwhm > $fwhmfile
sethead FWHM=$fwhm $filename
rm -f $tmp_fwhm_file
