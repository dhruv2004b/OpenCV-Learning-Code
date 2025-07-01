import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()

mpDraw = mp.solutions.drawing_utils


while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms,mphands.HAND_CONNECTIONS)

    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

  
    