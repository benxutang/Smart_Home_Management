# -*- coding: UTF-8 -*-
import datetime
from threading import Timer
import RPi.GPIO as GPIO
import time
import signal
from Adafruit_BME280 import *

from gpiozero import MCP3008

import urllib2
import json
import ssl
degrees=0
pascals=0
hectopascals=0
humidity=0
context = ssl._create_unverified_context()

def http_get():
    url='https://nussh.happydoudou.xyz:5000/api/Fan'
    response = urllib2.urlopen(url,context=context)
    return response.read()

def http_put():
    url='https://nussh.happydoudou.xyz:5000/api/Environmentfull'
    values={
        "Hum": "{0:0.2f}".format(humidity),
        "Pre": "{0:0.2f}".format(hectopascals),
        "Tem": "{0:0.3f}".format(degrees),
    }
    jdata = json.dumps(values)# 对数据进行JSON格式化编码
    request = urllib2.Request(url, jdata)
    request.add_header('Content-Type', 'application/json')
    request.get_method = lambda:'PUT'# 设置HTTP的访问方式
    request = urllib2.urlopen(request, context = context)
    print("Success Put!")
    return request.read()

pot = MCP3008(1)
state=1

def Caculator(sensordata):
    if sensordata >= 28:
        fan = 100
    if sensordata <=25.5:
        fan = 0
    if 25.5 < sensordata and sensordata < 28:
        fan = 100*(sensordata - 25)/3       
    return fan
 
servopin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(servopin, GPIO.OUT, initial = False)

p = GPIO.PWM(servopin, 100)
p.start(0)
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)


def TimeFan():
    #sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
    global degrees,pascals,hectopascals,humidity
    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()

    #time.sleep(0.1)
    print ('Temp      = {0:0.3f} deg C'.format(degrees))
    #print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))a
    #print ('Humidity  = {0:0.2f} %'.format(humidity))

    ret = http_get()
    global state
    Fanlin=json.loads(ret.decode('utf-8'))

    for dict_data in Fanlin:
        print(dict_data)
        print("\n")

    time="0000-00-00 00:00:00"
    Speed=[]
    State1=[]
    Timestamp=[]

    index=0

    for dict_data in Fanlin:
        Speed.append(dict_data['Speed'])
        State1.append(dict_data['State'])
        Timestamp.append(dict_data['Timestamp'])

    for i ,value in enumerate(Timestamp):
        if value>time:
            index=i
            time=value

    
    print(Speed[index]+'<<<<<<'+State1[index])

    if State1[index]=='0':
        state=0
        Fansp=int(Speed[index])
    elif State1[index]=='1' and state==0:
        state=1
        
    a=int(GPIO.input(23))
    if a>0:
        print("sb")
        if state>=2:
            state=1
        else:
            state=state+1
    if state==0:
        p.ChangeDutyCycle(Fansp)
    elif state==1:
        servalue = Caculator(degrees)
        p.ChangeDutyCycle(servalue)
    else:
        print(int(pot.value*20)*5)
        p.ChangeDutyCycle(int(pot.value*20)*5)

    
        #启动定时器任务，每一秒执行一次
    Timer(1, TimeFan).start()

        
def TimePut(logfile = None):
    global degrees,pascals,hectopascals,humidity
    http_put()
    #启动定时器任务，每十秒执行一次
    Timer(10, TimePut).start()


TimeFan()
TimePut()
