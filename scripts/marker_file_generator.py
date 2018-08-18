#!/usr/bin/env python

import cv2
import cv2.aruco as ar
import os
import numpy as np


def create_expanded_image(src):
    expand_factor = 2
    src_size = src.shape[0]
    exp_size = src_size * expand_factor

    new = np.zeros((exp_size, exp_size, 1), np.uint8)
    print(new.shape)

    copy_offset = int(src_size/2.0)
    for x in range(src_size):
        for y in range(src_size):

            new[x+copy_offset][y+copy_offset] = src[x][y]

    return new

def create_aruco_marker(id, ar_dict):
    px_size = 100
    border_size = 1
    return ar.drawMarker(ar_dict, id, px_size, None, border_size)

def write_material_script(id, script_dir):
    filename = "script_" + str(id) + ".material"
    with open(script_dir + "/" + filename, 'w+') as f:
        lines = []
        f.write("material Aruco/Aruco" + str(id) + "\n")
        f.write("{\n")
        f.write("  receive_shadows on\n")
        f.write("  technique\n")
        f.write("  {\n")
        f.write("    pass\n")
        f.write("    {\n")
        f.write("      texture_unit\n")
        f.write("      {\n")
        f.write("        texture ../texture/aruco_" + str(id) + ".png\n")
        f.write("      }\n")
        f.write("    }\n")
        f.write("  }\n")
        f.write("\n}")

N_preknown = 250
aruco_dict = ar.Dictionary_get(ar.DICT_6X6_250)
script_dir = os.path.dirname(os.path.realpath(__file__))
pkg_dir = script_dir + "/.."
media_dir = pkg_dir + "/media/materials/texture"
material_script_dir = pkg_dir + "/media/materials/scripts"
for i in range(N_preknown):
    print("Generating %s of %s..." % (i, N_preknown))
    base = create_aruco_marker(i, aruco_dict)
    #exp = create_expanded_image(base)
    save_file_name = media_dir + "/aruco_" + str(i) + ".png"
    cv2.imwrite(save_file_name, base)
    write_material_script(i, material_script_dir)