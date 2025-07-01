import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')

cv.imshow('blank',blank)

# blank[:] = 255,0,255

# cv.imshow('red',blank)
# Draw rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('rectangle', blank)

# # Draw circle

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow('circle', blank)

# # Draw line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('line', blank)

# Draw text
cv.putText(blank, 'Hello', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)