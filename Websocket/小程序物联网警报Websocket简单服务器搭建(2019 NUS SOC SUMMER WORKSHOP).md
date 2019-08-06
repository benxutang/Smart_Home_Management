# 小程序物联网警报Websocket简单服务器搭建(2019 NUS SOC SUMMER WORKSHOP)

## 服务器端

### 配置

1.需要使用SSL证书，我首先配置服务器系统，此处我使用的是Apache，绑定证书，升级垃圾Centos自带的Nodejs，此处非常恶心，略过。

2.新建ws后端工程文件

```linux
npm install ws --save
```

3.新建一个main.js

``` javascript
var fs = require('fs');

var httpServ = require('https');

var WebSocketServer = require('ws').Server;

var alarm;

var app = httpServ.createServer({

​    key: fs.readFileSync('key证书地址.key'),

​    cert: fs.readFileSync('crt证书地址.crt')

});


app.listen(8000,function() {

​    console.log('server started.')

});



var wss = new WebSocketServer({

​    server: app

});



wss.on('connection', function(wsConnect) {

​    wsConnect.on('message', function(message) {

​        console.log("received ",message);

//根据需要修改

​        if(message=='Cancel'){

​            alarm=0

​            wsConnect.send('Cancel Received!');    

​        }

​        else if (message=='Alarm'||alarm==1){

​            alarm=1

​            wsConnect.send('Alarm');

​        }

​        else if(message=='Safe'||alarm==0){

​            wsConnect.send('Safe');

​        }

​    });

});
```

4.在目录下运行

```linux
node main.js
```

如果看到"server started"，证明启动成功。

### 测试

使用chrome的Console发送以下命令测试服务器端

```javascript
var conn = new WebSocket('wss://你的域名地址:8000/');

conn.onmessage = function(e){ console.log(e.data); };

conn.onopen = () => conn.send('message');
```

### 微信端配置

```javascript
//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    motto: 'Welcome Back Home',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),

  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },
  gotohome:function(){
    wx.navigateTo({ url: '/pages/home/home', }) ;
  },

  onShow: function () {
    var thispage = this
    thispage.openWss()
    setInterval(function () { thispage.testWss(); }, 3000);
  },
  //********************************************************************
  //核心代码*************************************************************
  openWss() {
    wx.connectSocket({
      url: 'wss://nussh.happydoudou.xyz:8000/'
    })
  },
  testWss() {
    var thispage = this
    wx.sendSocketMessage({
      data: "connect"
    })
    wx.onSocketMessage(function (res) {
      thispage.setData({ alarm: res.data }),
        console.log('小程序收到服务器消息：' + thispage.data.alarm)
      
      if (thispage.data.alarm=='Alarm')
          wx.showModal({
            title: 'FBI WARNING!!!',
            content: 'Emergency Detected',
            cancelText:'STOP',
            confirmText: 'CALL999',
            cancelColor:'#07c160',
            confirmColor:'#f44',
            success(res) {
              if (res.confirm) {
                wx.makePhoneCall({
                  phoneNumber: '666' 
                })
              } else if (res.cancel) {
                wx.sendSocketMessage({
                  data: "Cancel"
                })
              }
            }
            
          })

    })
  }
})
```



