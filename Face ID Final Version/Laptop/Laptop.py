# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:49:41 2019

@author: LEN
"""

import serial
import cv2
import numpy as np
from Mylib import ftpconnect
from Mylib import downloadfile
from time import sleep

check = 1

ser = serial.Serial(port='COM9', baudrate=115200, timeout=1) #端口设置，改动‘’内值

while True:

    if check == 1:
        
        print("Listening on COM9... ")
        check = 0
        
    msg = ser.readline() #从串口读取信息
    smsg = msg.decode('utf-8').strip() #转码

    if smsg == '1':
        
        check = 1
        sleep(4.5)
        print('RX:{}\nLoading...'.format(smsg))
        if __name__ == "__main__":
            
            ftp = ftpconnect('192.168.43.19', 'pi', 'raspberry')
            downloadfile(ftp, 'video.mp4','G:/img/video.mp4')#first address is RPi, second is Laptop
        
            ftp.quit()    
            print('Complete\nAnalyzing')
            
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        # recognizer = cv2.createLBPHFaceRecognizer() # in OpenCV 2
        recognizer.read('trainner/trainner.yml')
        # recognizer.load('trainner/trainner.yml') # in OpenCV 2
        
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        cam = cv2.VideoCapture('G:/img/video.mp4')
        # font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) # in OpenCV 2
        font = cv2.FONT_HERSHEY_SIMPLEX
        count = 0
        
        while True:
            ret, im = cam.read()
            if im is None:
                print('Access is rejected')
                myopen = 0
                break
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 6, minSize = (50, 50))
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x - 25, y - 25), (x + w + 25, y + h + 25), (225, 0, 0), 2)
                img_id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if conf > 50:
                    count = count + 1
                    if img_id == 1:
                        img_id = 'TANG BENXU'
                    elif img_id == 2:
                        img_id = 'QIN BOWEN'
                    elif img_id == 3:
                        img_id = 'LIANG JIACHENG'
                    elif img_id == 4:
                        img_id = 'LUO YANG'
                else:
                    img_id = "Unknown"
                # cv2.cv.PutText(cv2.cv.fromarray(im), str(Id), (x, y + h), font, 255)
                cv2.putText(im, str(img_id), (x, y + h), font, 0.55, (0, 255, 0), 1)
            cv2.imshow('im', im)
            if cv2.waitKey(3) & 0xFF == ord('q'):
                print('Access is rejected')
                myopen = 0
                break
            if count > 15:
                print('Access is permitted')
                cv2.imwrite('user.jpg', im)
                myopen = 1
                
                break
        
        cam.release()
        cv2.destroyAllWindows()
        user = cv2.imread('user.jpg', cv2.IMREAD_COLOR)
        cv2.imshow('user',user)
        cv2.waitKey() #等待 	
        cv2.destroyAllWindows()
        
        if myopen == 1:
            ser.write(str.encode('2'+'\n'))
            print('sent')
        if myopen == 0:
            ser.write(str.encode('3'+'\n'))
            print('sent')

