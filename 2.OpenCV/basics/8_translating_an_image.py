# moving an image
# terminal command: python 8_translating_an_image.py -i ../../Datasets/images/pokemon.png -mx 100 -my 200

import argparse
import cv2
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")
ap.add_argument("-mx", "--movex", type = int, required=True,
	help="move x by amt")
ap.add_argument("-my", "--movey", type = int, required=True,
	help="move y by amt")
args = vars(ap.parse_args())
# load the input image from disk
image = cv2.imread(args["input"])
cv2.imshow("orignal image", image)

# Translating


x = args["movex"]
y = args["movey"]

transMat = np.float32([[1,0,x],[0,1,y]])
dim = (image.shape[1], image.shape[0])
moved = cv2.warpAffine(image, transMat, dim)
cv2.imshow("translated image", moved)


cv2.waitKey(0)
