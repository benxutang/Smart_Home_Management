# -*- coding: UTF-8 -*-
from threading import Timer
import time
import datetime


import RPi.GPIO as GPIO
import time
import signal
from Adafruit_BME280 import *
import time
from gpiozero import MCP3008


#put

import urllib2
import json
import ssl
context = ssl._create_unverified_context()

degrees=0
pascals=0
hectopascals=0
humidity=0

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
GPIO.setup(servopin, GPIO.OUT, initial = False)

p = GPIO.PWM(servopin, 100)
p.start(0)
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)


def TimeFan(logfile = None):
    global degrees,pascals,hectopascals,humidity
    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()

    print ('Temp      = {0:0.3f} deg C'.format(degrees))
    #print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))
    #print ('Humidity  = {0:0.2f} %'.format(humidity))

    servalue = Caculator(degrees)
    p.ChangeDutyCycle(servalue)
    #启动定时器任务，每三秒执行一次
    Timer(1, TimeFan).start()

def TimePut(logfile = None):
    global degrees,pascals,hectopascals,humidity
    http_put()
    #启动定时器任务，每秒执行一次
    Timer(10, TimePut).start()
TimeFan()
TimePut()