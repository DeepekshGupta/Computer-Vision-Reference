# Contour Detection
# terminal command: python 14_contour_detection.py -i ../../Datasets/images/tetris_blocks.png

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
# thresh = cv2.inRange(gray, 100,200)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]


# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
# edge = cv2.Canny(blur, 100, 200)
# cnts = cv2.findContours(edge, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]


cv2.drawContours(image, cnts, -1, [0,0,0], thickness=2)

cv2.imshow("Contours", image)

# output = image.copy()
# # loop over the contours
# for c in cnts:
# 	# draw each contour on the output image with a 3px thick purple
# 	# outline, then display the output contours one at a time
# 	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
# 	cv2.imshow("Contours", output)
# 	cv2.waitKey(5)


text = "I found {} objects!".format(len(cnts))
cv2.putText(image, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", image)



cv2.waitKey(0)




