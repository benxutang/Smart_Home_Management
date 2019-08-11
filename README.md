# Smart_Home_Management

## 关于Smart Home 

团队指导老师：

- Dr. Tan Wee Kek(NUS)

团队成员：

- 唐本旭（哈尔滨工业大学（深圳））
- 梁嘉城（电子科技大学）
- 罗洋（电子科技大学）
- 卿博文（南方科技大学）

## 团队目前成果(Code put in here)
### Group Project
#### section TANG BENXU
- 第一步，整出人脸识别的基本框架[Face recoginizer V1.0](人脸检测并识别.md)
- 第二步，访问树莓派中视频，并处理这段视频（对这段视频人脸识别），即[Face recoginizer V2.0](Laptop通过FTP访问树莓派中视频文件.md)
- 最终的成果：按钮通过Breadboard接Micro:bit A，A通过USB连接树莓派；另一个Micro:bit B连接电脑段，负责接收A传输的信息(message transmitted by radio)同时将这个信息发送到电脑(message transmitted by USB UART)。若按钮按下，树莓派接收到信息就开始录像，电脑接收到信息后访问树莓派录制的视频并进行处理，即做人脸识别。如果识别出是注册过的人脸，则通过Micro:bit A 和 B 向树莓派发送True，否则发送Fasle，从而决定是否开门(通过servo模拟门的开关)。各部分代码如下：
![](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Project%20Management/Sequence.JPG)
> [Micro:bit A部分代码](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Face%20ID%20Final%20Version/button_link.js)

> [Micro:bit B部分代码](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Face%20ID%20Final%20Version/Laptop_edge.js)

> [树莓派部分代码](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Face%20ID%20Final%20Version/RPi/Record.py)

> [电脑部分代码(包括信息接收和图像处理)](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Face%20ID%20Final%20Version/Laptop/Laptop.py)

#### section LIANG JIACHENG

* [Bulit Websocket For:'Alarm'](/Websocket)      [小程序物联网警报Websocket简单服务器搭建](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Websocket/%E5%B0%8F%E7%A8%8B%E5%BA%8F%E7%89%A9%E8%81%94%E7%BD%91%E8%AD%A6%E6%8A%A5Websocket%E7%AE%80%E5%8D%95%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%90%AD%E5%BB%BA.md)
* [Built RESTful Sevice(Server) For:'GET-PUT'](/Server_get_put)      [RESTFUL SERVICE 的搭建 & 服务端JSON处理](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Server_get_put/RESTFUL%20SERVICE%20%E7%9A%84%E6%90%AD%E5%BB%BA%20%26%20%E6%9C%8D%E5%8A%A1%E7%AB%AFJSON%E5%A4%84%E7%90%86.md)
* [Built Mini-Program For:'Remote Control'](https://github.com/JACKPURCELL/NUSSmartHome)
* [Rpi Network Link For:RPI PUT&GET](/Run_on_Rpi)      [RESTFUL SERVICE 的搭建 & 服务端JSON处理](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Server_get_put/RESTFUL%20SERVICE%20%E7%9A%84%E6%90%AD%E5%BB%BA%20%26%20%E6%9C%8D%E5%8A%A1%E7%AB%AFJSON%E5%A4%84%E7%90%86.md)
* Home System(Rpi), Server, Mini-Program Joint Adjustment

#### section QIN BOWEN
- [FTP](树莓派搭建ftp服务器配置本地用户访问.md)
- [路由器配置](树莓派热点路由器配置.md)
- [蓝牙UART](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Run_on_Rpi/Light_Rpi.py)读取传感器数据，树莓派上处理数据，控制灯泡亮度；代码中包含与小程序的对接部分
- 通过树莓派GPIO[控制风扇转速]()；代码包含与小程序的对接部分
#### section LUO YANG

* [Built RESTful Sevice(Server) For:'GET-PUT'](/Server_get_put)
* [Build The Dream House](1.jpg)

### Assignment 1: Game

- step1: 
- [x] section LUO YANG: [名称输入](/down-1.js)
- step2:
- [x] section QIN BOWEN: [手势识别](/ges-1.js)
- step3:
- [x] section LIANG JIACHENG: [Micro:bit to Receive](/receive.js)
- step4:
- [x] section TANG BENXU: [Micro:bit to Display on RPi](/树莓派启动与通信.md)

> - 源码在.md中

- step5:
- [x] section LIANG JIACHENG: [Joint Adjustment](https://github.com/TANGBEN7/Smart_Home_Management/tree/master/Assignment)

### 

## 团队工作安排历史记录

- [0724工作计划](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Project%20Management/7-24%20Schedule.md)
- [0727工作总结](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Project%20Management/0727-Review.md)
- [0727工作计划](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Project%20Management/0727%20Schedule.md)
- [0730工作总结](https://github.com/TANGBEN7/Smart_Home_Management/blob/master/Project%20Management/0730%20Review.md)

## 其他注意事项
- [Markdown语法](https://www.zybuluo.com/mdeditor)
- [Markdown安装](https://www.zybuluo.com/cmd/)

