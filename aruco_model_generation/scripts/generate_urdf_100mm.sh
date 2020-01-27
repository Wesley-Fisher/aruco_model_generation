#!/bin/sh
pkg_dir=$(rospack find aruco_model_generation)
echo $pkg_dir
. "$pkg_dir"/scripts/generate_urdf_custom_size_mm.sh "100"