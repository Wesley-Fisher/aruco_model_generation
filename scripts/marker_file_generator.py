#!/usr/bin/env python

import cv2
import cv2.aruco as ar
import os
import numpy as np


def create_aruco_marker(id, ar_dict):
    px_size = 100
    border_size = 2
    return ar.drawMarker(ar_dict, id, px_size, None, border_size)

def process_base_image(img, id):
    a = flip_image(img)
    b = cv2.cvtColor(a,cv2.COLOR_GRAY2RGB)
    c = draw_labels(b, id)
    return c

def draw_labels(img, id):
    size = img.shape[0]

    text_shade_main = 100
    text_shade_other = 40
    text_green = (text_shade_other, text_shade_main, text_shade_other)
    text_red = (text_shade_other, text_shade_other, text_shade_main)
    text_blue = (text_shade_main, text_shade_other, text_shade_other)
    text_grey = (text_shade_other, text_shade_other, text_shade_other)
    text_scale = 1.2
    text_height_est = int(16 * text_scale)
    text_thick = 2

    cv2.putText(img, '[A]X ^', ((size/2),text_height_est), cv2.FONT_HERSHEY_PLAIN, text_scale, text_red, text_thick, cv2.LINE_AA)
    
    cv2.putText(img, '[A]Y', (2,(size/2)), cv2.FONT_HERSHEY_PLAIN, text_scale, text_green, text_thick, cv2.LINE_AA)
    cv2.putText(img, '(R)Z', (2,(size/2)+text_height_est), cv2.FONT_HERSHEY_PLAIN, text_scale, text_blue, text_thick, cv2.LINE_AA)
    cv2.putText(img, '<', (2,(size/2)-text_height_est), cv2.FONT_HERSHEY_PLAIN, text_scale, text_grey, text_thick, cv2.LINE_AA)

    cv2.putText(img, '(R)X v', ((size/2),size-text_height_est), cv2.FONT_HERSHEY_PLAIN, text_scale, text_red, text_thick, cv2.LINE_AA)

    cv2.putText(img, 'ID: ' + str(id), (2,size-text_height_est), cv2.FONT_HERSHEY_PLAIN, text_scale, text_grey, text_thick, cv2.LINE_AA)
    return img



def flip_image(img):
    out = cv2.flip(img, 1)
    return out

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
aruco_dict = ar.Dictionary_get(ar.DICT_ARUCO_ORIGINAL)
script_dir = os.path.dirname(os.path.realpath(__file__))
pkg_dir = script_dir + "/.."
media_dir = pkg_dir + "/media/materials/texture"
material_script_dir = pkg_dir + "/media/materials/scripts"
for i in range(N_preknown):
    print("Generating %s of %s..." % (i, N_preknown))
    base = create_aruco_marker(i, aruco_dict)
    scale=4.0
    exp = cv2.resize(base, (0,0), fx=scale, fy=scale) 
    img = process_base_image(exp, i)
    save_file_name = media_dir + "/aruco_" + str(i) + ".png"
    cv2.imwrite(save_file_name, img)
    write_material_script(i, material_script_dir)
