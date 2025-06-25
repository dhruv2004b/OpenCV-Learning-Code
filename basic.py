import cv2 as cv
import numpy as np

img = cv.imread('Photos/IMG4.jpg')
cv.imshow('Cat', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascade
canny = cv.Canny(blur, 125, 175) 
cv.imshow('Canny Edges', canny)

#dilating image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(img, (250, 150), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#cropping
cropped = img[50:150, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
