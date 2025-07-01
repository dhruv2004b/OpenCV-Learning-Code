import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img= cv.imread('Photos/IMG1.jpg')
cv.imshow('Throne', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')



circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100,255, -1)

mask = cv.bitwise_and(gray,gray,mask= circle)
cv.imshow('Mask', mask)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# grascale histogram
# hist_gray = cv.calcHist([gray], [0], mask, [256], [0, 256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.plot(hist_gray)
# plt.xlim([0, 256])
# plt.show()

# color histogram

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()



cv.waitKey(0)