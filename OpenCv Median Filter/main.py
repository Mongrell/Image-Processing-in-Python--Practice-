import  cv2
import argparse

#Create the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to the input image')
ap.add_argument('-o', '--output', required = True, help = 'Path to the output image')
args = vars(ap.parse_args())

#Read the image
image = cv2.imread(args['image'])

#Apply the 3x3 median filter on the image
processed_image = cv2.medianBlur(image, 3)

#Display image
cv2.imshow('Median filter processing', processed_image)

#Save image to disk
cv2.imwrite(args['output'] + '\processed_img(2).png', processed_image)

#Pause the execution of the script until a key on the keyboard is pressed
cv2.waitKey(0)