import cv2 as cv
import numpy as np

img= cv.imread('Photos/IMG4.jpg')
cv.imshow('Throne', img)

#translate

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0]) # (width, height)
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

#rotate
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

#resize
resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#flip
flipped = cv.flip(img, 0)  # 1 for horizontal flip 0 for vertical flip -1 for both
cv.imshow('Flipped', flipped)

#crop
cropped = img[50:200, 200:400]  # y1:y2, x1:x2
cv.imshow('Cropped', cropped)

cv.waitKey(0)