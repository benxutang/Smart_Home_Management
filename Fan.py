import RPi.GPIO as GPIO
import time
import signal
from Adafruit_BME280 import *
import time
from gpiozero import MCP3008

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
while True:
    #sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
    degrees = sensor.read_temperature()
    #pascals = sensor.read_pressure()
    #hectopascals = pascals / 100
    #humidity = sensor.read_humidity()
    time.sleep(1)
    print ('Temp      = {0:0.3f} deg C'.format(degrees))
    #print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))
    #print ('Humidity  = {0:0.2f} %'.format(humidity))

    servalue = Caculator(degrees)
    p.ChangeDutyCycle(servalue)    
