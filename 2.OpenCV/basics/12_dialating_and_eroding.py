# dialating and eroding an image
# terminal command: python 12_dialating_and_eroding.py -i ../../Datasets/images/wallpaper.png


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
(h,w) = image.shape[:2]
scale = 700
r = scale/w
dim = scale, int(h*r)
image = cv2.resize(image, dim)
cv2.imshow("Orignal Image", image)

dialate_kernel = (3,3)
erode_kernel =(7,7)
blur = cv2.GaussianBlur(image, (5,5), cv2.BORDER_DEFAULT)
edge = cv2.Canny(blur, 125, 175)
cv2.imshow("Edges", edge)


dialated = cv2.dilate(edge, dialate_kernel, iterations=1)
cv2.imshow("dialated", dialated)

eroded = cv2.erode(edge, erode_kernel, iterations=3)
cv2.imshow("eroded", eroded)

cv2.waitKey(0)
