import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= cv.imread('Photos/IMG4.jpg')
cv.imshow('Throne', img)

blank= np.zeros(img.shape[:2], dtype='uint8')



b,g,r= cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

blue= cv.merge([b, blank, blank])
green= cv.merge([blank, g, blank])
red= cv.merge([blank, blank, r])

cv.imshow('Blue Channel', blue)
cv.imshow('Green Channel', green)
cv.imshow('Red Channel', red)

print(img.shape)
print(b.shape)
print(g.shape)  
print(r.shape)

merged= cv.merge([b,g,r])
cv.imshow('Merged', merged)


cv.waitKey(0)
