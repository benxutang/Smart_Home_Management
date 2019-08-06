# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:14:23 2019

@author: LEN
"""
import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture('G:\img\Me.avi')
sampleNum = 0
Id = input('enter your id: ')

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 7, minSize = (60, 60))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # incrementing sample number
        sampleNum = sampleNum + 1
        # saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User." + str(Id) + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])  #

        cv2.imshow('frame', img)
    # wait for 100 miliseconds
    if cv2.waitKey(350) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum > 250:
        break

cap.release()
cv2.destroyAllWindows()