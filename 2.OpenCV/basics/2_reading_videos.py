# Loading and displaying videos
# terminal command: python 2_reading_videos.py -i ../../Datasets/videos/crosswalk.avi 

import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image and press q to exit")
# ap.add_argument("-o", "--output", required=True,
# 	help="path to output image")
args = vars(ap.parse_args())


capture = cv2.VideoCapture(args["input"])
while True:
  isTrue, frame = capture.read()
  # frame = cv.flip(frame,1)
  # frame = cv.flip(frame,0)

  cv2.imshow('Video', frame)
  if cv2.waitKey(20) & 0xFF == ord('q') :
    break

print("Video ended")

capture.release()
cv2.destroyAllWindows()