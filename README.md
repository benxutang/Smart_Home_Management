# About Smart Home 

## Team Advisor

- Dr. Tan Wee Kek(NUS)

## Team Member

- TANG BENXU 唐本旭（哈尔滨工业大学（深圳））
- LIANG JIACHENG 梁嘉城（电子科技大学）
- LUO YANG 罗洋（电子科技大学）
- QING BOWEN 卿博文（南方科技大学）

# History Summary of Teamwork

- [0724 Schedule](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Project%20Management/7-24%20Schedule.md)
- [0724 Review](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Project%20Management/0727-Review.md)
- [0727 Schedule](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Project%20Management/0727%20Schedule.md)
- [0730 Review](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Project%20Management/0730%20Review.md)

# DONE
## Group Project
### **section TANG BENXU**
- Research process and documentations (documentations are .md files. `Check out the hyperlink`)
- [x] Step 1，Recoginize human's face [Face recoginizer V1.0](人脸检测并识别.md)
- [x] Step 2，Access video which was recorded by RPi (and stored on RPi) through File Transfer Protocol(FTP) [Face recoginizer V2.0](Laptop通过FTP访问树莓派中视频文件.md)
- [x] Finally, the door (powerd by the servo) will open for the one whose face was registered before.

- The idea map

![Sequence](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Project%20Management/Sequence.JPG)

- Sourse code on RPi, laptop and 2 microbits.

- [x] [Source code](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Face%20ID%20Final%20Version/button_link.js) on Micro:bit A

- [x] [Source code](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Face%20ID%20Final%20Version/Laptop_edge.js) on Micro:bit B

- [x] [Source code](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Face%20ID%20Final%20Version/RPi/Record.py) on RPi

- [x] [Source code](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Face%20ID%20Final%20Version/Laptop/Laptop.py) on laptop, including message and images receiving and image processing

- Detail explanation of how the whole system work in English. 

> The botton (which simulates a door bell) connects with Micro:bit A through breadboard. Micro:bit A connects with RPi through USB cable (message transmitts by UART). Micro:bit B connects with the laptop and can receive message sent by radio from Micro:bit A.

> If the button is pressed, RPi will receive a "botton is pressed" message from Micro:bit and start to record a short video of the face of "the guest". Laptop will then access run face recoginizing program on the video after receiving message. If the face is registered before, the laptop will send "true" through Micro:bit and start the servo and open the door. If the face isn't resistered, the door won't open. 

- Chinese version

> 按钮通过Breadboard接Micro:bit A，A通过USB连接树莓派；另一个Micro:bit B连接电脑段，负责接收A传输的信息(message transmitted by radio)同时将这个信息发送到电脑(message transmitted by USB UART)。若按钮按下，树莓派接收到信息就开始录像，电脑接收到信息后访问树莓派录制的视频并进行处理，即做人脸识别。如果识别出是注册过的人脸，则通过Micro:bit A 和 B 向树莓派发送True，否则发送Fasle，从而决定是否开门(通过servo模拟门的开关)。


### section LIANG JIACHENG

* [Bulit Websocket For:'Alarm'](/Websocket)   中   [小程序物联网警报Websocket简单服务器搭建](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Websocket/%E5%B0%8F%E7%A8%8B%E5%BA%8F%E7%89%A9%E8%81%94%E7%BD%91%E8%AD%A6%E6%8A%A5Websocket%E7%AE%80%E5%8D%95%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%90%AD%E5%BB%BA.md)
* [Built RESTful Sevice(Server) For:'GET-PUT'](/Server_get_put)   中   [RESTFUL SERVICE 的搭建 & 服务端JSON处理](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Server_get_put/RESTFUL%20SERVICE%20%E7%9A%84%E6%90%AD%E5%BB%BA%20%26%20%E6%9C%8D%E5%8A%A1%E7%AB%AFJSON%E5%A4%84%E7%90%86.md)
* [Built Mini-Program For:'Remote Control'](https://github.com/JACKPURCELL/NUSSmartHome)
* [Rpi Network Link For:RPI PUT&GET](/Run_on_Rpi)    中    [RESTFUL SERVICE 的搭建 & 服务端JSON处理](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Server_get_put/RESTFUL%20SERVICE%20%E7%9A%84%E6%90%AD%E5%BB%BA%20%26%20%E6%9C%8D%E5%8A%A1%E7%AB%AFJSON%E5%A4%84%E7%90%86.md)
* Home System(Rpi), Server, Mini-Program Joint Adjustment

### section QIN BOWEN
- [FTP](树莓派搭建ftp服务器配置本地用户访问.md)
- [路由器配置](树莓派热点路由器配置.md)
- [蓝牙UART](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Run_on_Rpi/Light_Rpi.py)读取传感器数据，树莓派上处理数据，控制灯泡亮度；代码中包含与小程序的对接部分
- 通过树莓派GPIO[控制风扇转速](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Run_on_Rpi/Fan_Rpi.py)；代码包含与小程序的对接部分
#### section LUO YANG

* [Built RESTful Sevice(Server) For:'GET-PUT'](/Server_get_put)
* [Build The Dream House](1.jpg)

## Assignment 1: Game

- step1: 
- [x] section LUO YANG: [名称输入](/down-1.js)
- step2:
- [x] section QIN BOWEN: [手势识别](/ges-1.js)
- step3:
- [x] section LIANG JIACHENG: [Micro:bit Receiving](/receive.js)
- step4:
- [x] section TANG BENXU: [Displaying on RPi](/树莓派启动与通信.md)
- step5:
- [x] section LIANG JIACHENG: [Joint Adjustment](https://github.com/TANGBEN7/Smart_Home_Management/tree/master/Assignment)

`Sorce codes are included in the .md files(hyperlink)`


# [Our Final Showcase](https://github.com/TANGBEN7/Smart_Home_Management/tree/master/Final%20Showcase)
## Quick View
Our mission is to make our house a more comfortable and safe place to live in. We have smart IoT LEDs and Air-con/Fan, and a house security system based on computer version.

![](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Final%20Showcase/img/01_small.JPG)

## Parts
- [x] Mini program on mobile to control things in the house remotely
- [x] Front door with Face ID
- [x] Alarm with motion detect
- [x] Auto-adjusted smart LED and fan

## Why We are Special
- Our smart home is a ture IoT system, which is able to access to the Internet, instead of the local area network
- Face ID and Motion detection programs are all based on open source library including OpenCV, codes are written by ourselves
- We built a beautifully decorated paperboard house to do the simulation

# Others
## Markdown
We use markdown to write

- [x] Team Plan & Review
- [x] Gantt Chart
- [x] Documentation

Useful links

- [Using Markdown](https://www.zybuluo.com/mdeditor)
- [Downloading Markdown](https://www.zybuluo.com/cmd/)

## Google Coding Style

- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) 

  创新工场董事长兼 CEO 李开复曾经对 Google C++ 编码规范给予了极高的评价：“我认为这是地球上最好的一份 C++ 编程规范，没有之一，建议广大国内外 IT 研究使用。”
  
  
- [Doxygen annotating style](http://www.doxygen.nl/)
  
  需要文档化的注释统一使用Doxygen的注释风格，即/*! … */和//!和//!< 三种方法
  
  不需要文档化的注释统一使用普通的注释风格，即2斜杠//
  
  这样又同时符合了Google C++风格（Google推荐/*…*/和//2种，上面的三种方式是从这2种演变而来）






