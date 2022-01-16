# Blurring an image
# terminal command: python 7_blurring_an_image.py -i ../../Datasets/images/pokemon.png -k 9

import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")
ap.add_argument("-k", "--kernel", type = int, required=True,
	help="enter odd number for kernel size")
args = vars(ap.parse_args())
# load the input image from disk
image = cv2.imread(args["input"])
cv2.imshow("orignal image", image)

# blurring or smoothening
kernel = args["kernel"]
kernel_size = (kernel, kernel)

blur = cv2.GaussianBlur(image, kernel_size , cv2.BORDER_DEFAULT)
cv2.imshow("blurred", blur)


cv2.waitKey(0)
