import cv2 as cv
import numpy as np

img= cv.imread('Photos/IMG4.jpg')
cv.imshow('Throne', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
cv.imshow('Gray', gray)

blurred=cv.GaussianBlur(gray, (5, 5),cv.BORDER_DEFAULT)
cv.imshow('Blurred', blurred)

canny = cv.Canny(blurred, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresholded', thresh)

countours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'Number of contours found: {len(countours)}')

cv.drawContours(blank, countours, -1, (0, 0, 255), thickness=1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
