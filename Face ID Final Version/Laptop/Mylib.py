
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:13:10 2019

@author: LEN
"""
from ftplib import FTP
import cv2
import numpy as np
import time
#连接
def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    
if __name__ == "__main__":
    ftp = ftpconnect('10.3.141.144', 'pi', 'raspberry')
    downloadfile(ftp, 'video.avi','G:/img/video.avi')
    #uploadfile(ftp, "test.jpg", "C:/Users/LEN/Desktop/_DSC7212.jpg")

    ftp.quit()    
    print('Complete')

def recognizer(video_path):
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # recognizer = cv2.createLBPHFaceRecognizer() # in OpenCV 2
    recognizer.read('trainner/trainner.yml')
    # recognizer.load('trainner/trainner.yml') # in OpenCV 2
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    cam = cv2.VideoCapture(video_path)
    # font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) # in OpenCV 2
    font = cv2.FONT_HERSHEY_SIMPLEX
    check=0
    
    if cam.isOpened():
        timeprevious = time.time()
        print('Cam open')
    
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 10, minSize = (80, 80))
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x - 25, y - 25), (x + w + 25, y + h + 25), (225, 0, 0), 2)
            img_id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if conf > 70:
                if img_id == 1:
                    img_id = 'TANG BENXU'
                elif img_id == 2:
                    img_id = 'QIN BOWEN'
                elif img_id == 3:
                    img_id = 'LIANG JIACHENG'
                elif img_id == 4:
                    img_id = 'LUO YANG'
                
                check=check+1
                if check > 4:
                    break
            else:
                img_id = "Unknown"
            # cv2.cv.PutText(cv2.cv.fromarray(im), str(Id), (x, y + h), font, 255)
            cv2.putText(im, str(img_id), (x, y + h), font, 0.55, (0, 255, 0), 1)
        cv2.imshow('im', im)
        if check > 4:
            cv2.imwrite('user.jpg', im)
            print('Access is Permitted.\nWelcome',img_id)
            break
        time2 = time.time()
        if time2 - timeprevious > 5:
            print('Access is Rejected')
            break
        
    cam.release()
    cv2.destroyAllWindows() 
    
    user = cv2.imread('user.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('user',user)
    cv2.waitKey() #等待 
    cv2.destroyAllWindows() 

        