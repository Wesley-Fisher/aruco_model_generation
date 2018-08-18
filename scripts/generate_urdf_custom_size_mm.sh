#!/bin/sh

if [ -n "$1" ]; then echo "Creating markers with size $1 mm"; else echo "Add size in mm as first argument"; return 0; fi

size=$1
mm_to_m=0.001

pkg_dir=$(rospack find aruco_model_generation)

urdf_common_dir="$pkg_dir/urdf/common"
mkdir "$pkg_dir/urdf/aruco_$size""mm"
urdf_out_dir="$pkg_dir/urdf/aruco_$size""mm"

for id in $(seq 0 249)
do
    echo $id
    sizem=`echo $size \\* $mm_to_m | bc`
    rosrun xacro xacro.py -o "$urdf_out_dir/aruco_$size""mm_$id.urdf" "$urdf_common_dir/aruco_robot.urdf.xacro" size:=$sizem id:=$id
done