# Cropping an image
# terminal command: python 4_cropping_ROIs.py -i ../../Datasets/images/pokemon.png

import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")
# ap.add_argument("-o", "--output", required=True,
# 	help="path to output image")
args = vars(ap.parse_args())
# load the input image from disk
image = cv2.imread(args["input"])

#            y1:y2,   x1:x2
roi = image[100:250, 100:350]

cv2.imshow("cropped image", roi)

cv2.waitKey(0)
