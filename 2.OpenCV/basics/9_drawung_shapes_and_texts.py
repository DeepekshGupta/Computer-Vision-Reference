# adding text and shapes to an image
# terminal command: python 9_drawung_shapes_and_texts.py -i ../../Datasets/images/pokemon.png -t hello_world

import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")
ap.add_argument("-t", "--text",
	help="enter text")
args = vars(ap.parse_args())
# load the input image from disk
image = cv2.imread(args["input"])
cv2.imshow("orignal image", image)



# coloring a region with a color
color_region = image.copy()
color_region[100:250, 100:350] = 255,150,100
cv2.imshow("colored region", color_region)




# adding a line
line_img = image.copy()
#                    x1, y1     x2,y2        color
cv2.line(line_img, (100,100), (350,250), (255,255,255), thickness=3)
cv2.imshow("line", line_img )





# Shapes
shape_img = image.copy()
pt1 = (200,100)
pt2 = (400,450)
color = (0,255,0)
rad = 100
cv2.rectangle(shape_img, pt1, pt2, color, thickness=3)
cv2.circle(shape_img, pt1, rad, (255,0,0), thickness=-1)
cv2.imshow("shape", shape_img)




# text
text_img = image.copy() 
text = args["text"]
pt = (200,100)
scaling = 1.0
cv2.putText(text_img, text, pt, cv2.FONT_ITALIC, scaling, (255,100,223), thickness=2)
cv2.imshow("text", text_img)


# # ---------------------------uncomment all of this in one go--------------------------------

# # coloring a region with a color
# image[100:250, 100:350] = 255,150,100 # region coloring
# cv2.line(image, (100,100), (350,250), (255,255,255), thickness=3) # line
# cv2.rectangle(image, pt1, pt2, color, thickness=3) # rectangle
# cv2.circle(image, pt1, rad, (255,0,0), thickness=-1) # circle
# cv2.putText(image, text, pt, cv2.FONT_ITALIC, scaling, (255,100,223), thickness=2) # text
# cv2.imshow("Final image", image)


cv2.waitKey(0)
