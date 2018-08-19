# aruco_model_generation
A repo for creating urdf models of aruco markers for use in Gazebo.

This package comes with 250 markers, spaning id values from 0 to 249, in both 100mm and 500mm squares.

Aruco markers are generated via OpenCV 3.1.0 [(See this page)](https://docs.opencv.org/3.1.0/d5/dae/tutorial_aruco_detection.html). This package can create 250 aruco markers in different sizes.

Note: testing has yet to be done on non-development systems.

## Spawning Models
See the ```launch/spawn_aruco.launch``` file

Note: the ```/scripts/source_paths.sh``` files may need to be sourced before the urdf files can be properly loaded.

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

## Generating New Aruco Markers
The aruco markers themselves (the .png files) were originally generated in Ubuntu14.04/Python3.4. If needed, markers can be re-generated.

Run ```setup_virtual_environment.sh``` to create a virtual python environment ```.venv```, which can be used to run the ```scripts/marker_file_generator.py``` file. This file will generate both the .png files, and necessary material files within ```/media/scripts```.

RUN ```clean_aruco_generation.sh``` to generate the virtual environment, create the markers, and remove the virtual environment, all in one command.
