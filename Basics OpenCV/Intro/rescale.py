import cv2 as cv


# resize function works for both Image ,Videos and Live videos
# def reScale(frame,scale=0.75):
#     width =int (frame.shape[1] * scale)
#     height =int (frame.shape[0] * scale)

#     dimensions= (width,height)

#     return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)



# resizing image
# img= cv.imread('Photos\Ghost Riley.png')
# cv.imshow('Ghost',img)

# resImage= reScale(img,0.2)
# cv.imshow('resImage',resImage)


# resize function works specifically for Live videos only(eg camera live)

def res_Vid(width,height): 
    liveCapture.set(3,width)
    liveCapture.set(4,height)

#live video capturre and resize example
liveCapture= cv.VideoCapture(0)
while True:
    isTrue, frame= liveCapture.read()
    reFramed= res_Vid(0.25,0.25)

    cv.imshow('live Video',frame)
    cv.imshow(' live Video Resize',reFramed)
   

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

liveCapture.release()
cv.destroyAllWindows()


# Reading video
# capture= cv.VideoCapture('Videos/v1.mp4')

# while True:
#     isTrue, frame= capture.read()
#     reFramed= reScale(frame,0.25)

#     cv.imshow('Video',frame)
#     cv.imshow('Video Resize',reFramed)
#     cv.imshow('Live Video')

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()




