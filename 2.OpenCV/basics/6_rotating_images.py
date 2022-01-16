# rotaing an image
# terminal command: python 6_rotating_images.py -i ../../Datasets/images/pokemon.png -a 45

import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")
ap.add_argument("-a", "--angle", type = int, required=True,
	help="angle of rotation")
args = vars(ap.parse_args())
# load the input image from disk
image = cv2.imread(args["input"])
cv2.imshow("orignal image", image)


# rotated image
(h,w) = image.shape[:2]

center = (w//2, h//2)
RotMat = cv2.getRotationMatrix2D(center, args["angle"], 1.0)
rotated = cv2.warpAffine(image, RotMat, (w,h))
cv2.imshow("Rotated image", rotated)

# -ive rotation
opp = args["angle"] * -1
RotMat = cv2.getRotationMatrix2D(center, opp, 1.0)
rotated = cv2.warpAffine(image, RotMat, (w,h))
cv2.imshow("opposite Rotated image", rotated)


cv2.waitKey(0)
