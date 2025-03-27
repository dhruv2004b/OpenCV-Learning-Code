import cv2 as cv
import numpy as np

blank= np.zeros((1000,1000,3),dtype='uint8')

cv.imshow('Blank',blank)
# blank[250:750,250:750]= 0,0,255


# cv.imshow('Red',blank)

cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=4)
cv.imshow('rect',blank)

cv.waitKey(0)