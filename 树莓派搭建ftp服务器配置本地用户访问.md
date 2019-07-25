# 树莓派搭建ftp服务器配置本地用户访问
标签： 树莓派 raspberry debian ftp vsftpd 本地用户


## 安装ftp服务器
```
sudo apt-get install vsftpd
```

## 启动ftp服务
```
sudo service vsftpd start
```

## 修改默认配置

sudo nano /etc/vsftpd.conf

### 寻找并打开如下注释：
```
# 不允许匿名访问
anonymous_enable=NO
# 可以写入
write_enable=YES
# 设置上传文件掩码
local_umask=022
# 使用utf-8字符集
utf8_filesystem=YES
```
### 不允许用户浏览自己根目录以外目录需额外做如下修改：
```
#取消注释并将其改为NO
chroot_local_user=NO
#设置通过读取文件确定哪些用户不允许离开自己的用户目录
chroot_list_enable=YES
```
### 存盘退出nano：
```
ctrl+o
ctrl+x
```
注意，需指定限制用户列表
设置了chroot_list_enable=YES后，必须建立列表文件，
否则客户端连接失败
建立/etc/vsftpd.chroot_list文件，将不允许离开自己根目录的用户加入到该文件中，一行一个用户名比如：
sudo nano /etc/vsftpd.chroot_list
```
# 在文件中添加限制的用户名
student
test
```

## 重启ftp服务：
```
sudo service vsftpd restart
```

## 测试ftp服务
如果暂时没有安装ftp客户端可以在windows下通以下方式访问
在资源管理器地址栏中输入：
```
ftp://ip地址
```

此时树莓派默认用户：pi基本上可以访问ftp

作者：snowyvalley
[链接](https://www.jianshu.com/p/42df944d349d)
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
