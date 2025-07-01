import cv2 as cv
import numpy as np


haar_casacde = cv.CascadeClassifier('haar_face.xml')
# Load the trained model and labels
people =['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Load the trained model
face_recognizer.read('face_trained.yml')

img= cv.imread(r'D:\Downloads\testBA3.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#detect the face
faces_rect = haar_casacde.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)   
print(f'Number of faces detected: {len(faces_rect)}')
for (x, y, w, h) in faces_rect:
    face_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(face_roi)
    
    print(f'Label: {people[label]}, Confidence: {confidence}')
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)
    
