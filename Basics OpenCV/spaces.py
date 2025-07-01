import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= cv.imread('Photos/IMG4.jpg')
cv.imshow('Throne', img)

# plt.imshow(img)
# plt.show()

# bgr to grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#bgr to hsv
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#bgr to lab
lab= cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('Lab', lab)

# bgr to rgb

rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# hsv to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

# lab to bgr
lab_bgr = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
cv.imshow('Lab to BGR', lab_bgr)

cv.waitKey(0)