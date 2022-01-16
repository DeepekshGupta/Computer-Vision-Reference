# Loading and displaying and saving an image
# terminal command: python 1_loading_displaying_saving.py -i ../../Datasets/images/pokemon.png -o ../../Datasets/output/output.png


import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")
ap.add_argument("-o", "--output", required=True,
	help="path to output image")
args = vars(ap.parse_args())
# load the input image from disk
image = cv2.imread(args["input"])


# displaying the output image
cv2.imshow("output", image)

# displaying the output image to disk
cv2.imwrite(args["output"], image)
cv2.waitKey(0)
