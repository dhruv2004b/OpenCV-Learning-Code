import cv2 as cv
import numpy as np

img= cv.imread('Photos/IMG4.jpg')
cv.imshow('Throne', img)

# averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# gausian blur
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian', gaussian)

# median blur
median = cv.medianBlur(img, 3)      
cv.imshow('Median', median)

# bilateral filter
bilateral = cv.bilateralFilter(img, 10, 35, 25) 
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)
