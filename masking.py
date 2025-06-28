import cv2 as cv
import numpy as np


img= cv.imread('Photos/IMG4.jpg')
cv.imshow('Throne', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle= cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Circle', circle)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 170), 255, -1)
# cv.imshow('Rectangle', rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

# Bitwise AND operation to apply the mask on the image
# This will keep only the part of the image where the mask is white (255)
# The rest of the image will be black (0)
# Essentially, it will show the part of the image that is within the circle defined by the mask
# The bitwise_and function takes the original image, the original image again, and the mask
# The mask is applied to the image, so only the area where the mask is white will be visible
masked_img= cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Masked Image', masked_img)


cv.waitKey(0)