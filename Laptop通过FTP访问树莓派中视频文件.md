# Laptop通过FTP访问树莓派中视频文件

标签（空格分隔）： NUSProgram

---

# FTP配置
## [树莓派中配置](树莓派搭建ftp服务器配置本地用户访问.md)
## 电脑上配置
- 网络连接树莓派
- 在“此电脑”处可见树莓派的ID，打开之后可以复制文件到这里，做一下测试

# FTP函数
- [函数](https://www.cnblogs.com/hltswd/p/6228992.html)
- 将FTP地址（树莓派地址）中的文件复制到电脑实体硬盘上，从而人脸识别的程序可以访问到这个视频
```
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()
if __name__ == "__main__":
    ftp = ftpconnect('10.3.141.144', 'pi', 'raspberry')
    downloadfile(ftp, 'Me.avi','G:/img/Me.avi')

    ftp.quit()    
    print('Complete')
```

# FTP+人脸识别整合
Code
```
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
    downloadfile(ftp, 'Me.avi','G:/img/Me.avi')
    #uploadfile(ftp, "test.jpg", "C:/Users/LEN/Desktop/_DSC7212.jpg")

    ftp.quit()    
    print('Complete')
   
recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer = cv2.createLBPHFaceRecognizer() # in OpenCV 2
recognizer.read('trainner/trainner.yml')
# recognizer.load('trainner/trainner.yml') # in OpenCV 2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cam = cv2.VideoCapture('G:/img/Me.avi')
# font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) # in OpenCV 2
font = cv2.FONT_HERSHEY_SIMPLEX
check=0

while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 6, minSize = (20, 20))
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x - 25, y - 25), (x + w + 25, y + h + 25), (225, 0, 0), 2)
        img_id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        if conf > 60:
            if img_id == 1:
                img_id = 'TANG BENXU'
            elif img_id == 2:
                img_id = 'QIN BOWEN'
            elif img_id == 3:
                img_id = 'LIANG JIACHENG'
            elif img_id == 4:
                img_id = 'LUO YANG'
            
            check=check+1
        else:
            img_id = "Unknown"
        # cv2.cv.PutText(cv2.cv.fromarray(im), str(Id), (x, y + h), font, 255)
        cv2.putText(im, str(img_id), (x, y + h), font, 0.55, (0, 255, 0), 1)
    cv2.imshow('im', im)
    if check > 4:
        print('Access is Permitted.\nWelcome',img_id)
        break

cam.release()
cv2.destroyAllWindows()  
```


