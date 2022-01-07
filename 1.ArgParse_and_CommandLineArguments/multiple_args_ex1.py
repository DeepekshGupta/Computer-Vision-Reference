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

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)

cnts = cv2.findContours(edged,
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]

cv2.drawContours(image, cnts,-1,(0,0,255),1)
# loop over the contours and draw them on the input image
for c in cnts:
	cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
# display the total number of shapes on the image
text = "I found {} total shapes".format(len(cnts))
cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
		(0, 0, 255), 2)
# write the output image to disk
cv2.imshow(args["output"], image)
cv2.waitKey(0)

