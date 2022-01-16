# resizing an image while preserving its aspect ratio
# terminal command: python 5_resizing_images.py -i ../../Datasets/images/pokemon.png

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
cv2.imshow("orignal image", image)


#resize function                      w, h
resized_normal = cv2.resize(image, (500, 200)) 
cv2.imshow("normal resize", resized_normal)



# preserving aspect ratio
(h,w) = image.shape[:2]
print("height : "+ str(h))
print("width : "+ str(w))

scale = 500
r = scale/w
dim = scale, int(h*r)
resized_aspect = cv2.resize(image, dim)
cv2.imshow("aspect ratio preservation", resized_aspect)



cv2.waitKey(0)
