# Edge Detection
# terminal command: python 11_edge_detection.py -i ../../Datasets/images/pokemon.png


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
cv2.imshow("Orignal Image", image)

threshold1 = 125
threshold2 = 175
blur = cv2.GaussianBlur(image, (5,5), cv2.BORDER_DEFAULT)
edge = cv2.Canny(blur, threshold1, threshold2)
cv2.imshow("Edges", edge)

cv2.waitKey(0)
