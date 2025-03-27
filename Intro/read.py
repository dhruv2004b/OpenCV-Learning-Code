import cv2 as cv


# img = cv.imread('Photos\Ghost Riley.png')

# cv.imshow('GhostRiley',img)

capture= cv.VideoCapture('Videos/v1.mp4')

while True:
    isTrue, frame= capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()