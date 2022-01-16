# Thresholding
# terminal command: python 13_thresholding.py -i ../../Datasets/images/pokemon.png


import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")
# ap.add_argument("-o", "--output", required=True,
# 	help="path to output image")
args = vars(ap.parse_args())
# load the input image from disk
image = cv2.imread(args["input"])
cv2.imshow("Orignal Image", image)


# binary thresholding
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.inRange(gray, 100,150)
cv2.imshow("Binary Thresholding", thresh)



Redl = np.array([17,15,100])
RedU = np.array([50,56,200])
red_section = cv2.inRange(image, Redl,RedU)
cv2.imshow("Red section of image", red_section)



# Bluel = np.array([34,60,135])
# BlueU = np.array([9,39,255])
# Blue_section = cv2.inRange(image, Bluel, BlueU)
# cv2.imshow("Blue section of image", Blue_section)



# i = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# plt.imshow(i)
# plt.show()


cv2.waitKey(0)

