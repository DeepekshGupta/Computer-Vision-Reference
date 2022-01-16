# Accessing individual pixels
# terminal command: python 3_Accessing_each_pixel.py -i ../../Datasets/images/pokemon.png

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


(b,g,r) = image[100,50]
print("B : " + str(b) + " G : " + str(g) + " R : " + str(r))

cv2.waitKey(0)
