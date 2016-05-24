#!/usr/bin/env bash
# Parameters
rgbname_img=$1
output_png_path=$2
output_tms_path=$3
link_base=$4
# Concat paths to libs
if [ ! -f "$rgbname_img" ] ; then
  echo "The file '$rgbname_img' not exist" >&2
  exit 1
fi
# -- Creating TMS
#fcontrast=$rgbname_img".contrast"
16b_2_8b_convert.sh $rgbname_img > /dev/null
#gdal_contrast_stretch -ndv 0 -outndv 0 -percentile-range 0.02 0.98  $rgbname_img $fcontrast  > /dev/null
#mv -f $fcontrast $rgbname_img
mk_tiles.sh $rgbname_img 2 15 $output_png_path $output_tms_path $link_base
# --
code=$?
if [ "$code" != 0 ]
then
  exit $code
fi
#
exit 0