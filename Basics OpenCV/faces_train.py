import os
import numpy as np
import cv2 as cv

people =['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR= r'F:\OpenCV\train'
haar_casacde = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []

def create_train():
    for person in people:
        path= os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect= haar_casacde.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()
print("training done -----------")

features = np.array(features, dtype='object')
labels = np.array(labels, dtype=np.int32)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#train the recognizer
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)