#!/bin/bash
pkg_dir=$(rospack find aruco_model_generation)
echo $pkg_dir
file="$pkg_dir/scripts/generate_urdf_custom_size_mm.sh"
echo "Calling script ${file}"
. $pkg_dir/scripts/generate_urdf_custom_size_mm.sh "100"