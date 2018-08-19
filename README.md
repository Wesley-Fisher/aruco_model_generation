# aruco_model_generation
A repo for creating urdf models of aruco markers for use in Gazebo.

This package comes with 250 markers, spaning id values from 0 to 249, in both 100mm and 500mm squares.

Aruco markers are generated via OpenCV [(See this page)](https://docs.opencv.org/3.1.0/d5/dae/tutorial_aruco_detection.html). This package can create 250 aruco markers in different sizes.

## Spawning Models
See the ```launch/spawn_aruco.launch``` file

## Creating Differently-Sized URDF Files
To create a new set of urdf files in different sizes, run the /scripts/generate_urdf_custom_size_mm.sh file, with the size in mm as an arugment. For example, to create square markers 200mm in side length, run:
```
source ./scripts/generate_urdf_custom_size_mm.sh 200
```

This will create the /urdf/aruco_200mm folder, and populate it with urdf files.

## Referencing URDF Files
The urdf files can be referenced as:
```
{aruco_model_generation}/urdf/aruco_{size; see above}mm_{id; 0 to 249}.urdf
```
