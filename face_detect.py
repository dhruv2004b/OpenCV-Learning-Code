import cv2 as cv
import numpy as np


img= cv.imread('Photos/IMG10.jpg')
cv.imshow('IMG', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_casacde = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_casacde.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

print(f'Number of faces detected: {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2) 
cv.imshow('Detected Faces', img)






cv.waitKey(0)