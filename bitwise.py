import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1) 

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitewise and --> intersecting region
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise or --> union of both shapes(non intersecting and intersecting regions)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwisee xor --> non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise not --> flips the colors of the shapes
# for rectangle, it will make the rectangle black and the rest white
# for circle, it will make the circle black and the rest white
bitwise_not_rectangle = cv.bitwise_not(rectangle)
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT Rectangle', bitwise_not_rectangle)
cv.imshow('Bitwise NOT Circle', bitwise_not_circle)


cv.waitKey(0)