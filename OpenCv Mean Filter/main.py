import cv2
import numpy as np
import argparse

#Create arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to image')
ap.add_argument('-o', '--output', required = True, help = 'Output path')
args = vars(ap.parse_args())

#Read image
image = cv2.imread(args['image'])

#Apply the 3x3 mean filter on the image
kernel = np.ones((3,3),np.float32)/9
processed_image = cv2.filter2D(image, -1, kernel)

#Display image
cv2.imshow('Previous Image', image)
cv2.imshow('Mean Filter Processing', processed_image)

#Save image
cv2.imwrite('processed_img.png', processed_image)

#Pause key
cv2.waitKey(0)