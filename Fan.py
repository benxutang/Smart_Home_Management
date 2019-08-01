import RPi.GPIO as GPIO
import time
import signal
from Adafruit_BME280 import *
import time
from gpiozero import MCP3008
pot = MCP3008(1)
state=2
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
while True:
    #sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
    degrees = sensor.read_temperature()
    #pascals = sensor.read_pressure()
    #hectopascals = pascals / 100
    #humidity = sensor.read_humidity()
    time.sleep(0.1)
    print ('Temp      = {0:0.3f} deg C'.format(degrees))
    #print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))a
    #print ('Humidity  = {0:0.2f} %'.format(humidity))

    a=int(GPIO.input(23))
    if a>0:
        print("sb")
        if state>=2:
            state=0
        else:
            state=state+1
    if state==0:
        p.ChangeDutyCycle(0)
    elif state==1:
        servalue = Caculator(degrees)
        p.ChangeDutyCycle(servalue)
    else:
        print(int(pot.value*20)*5)
        p.ChangeDutyCycle(int(pot.value*20)*5)
        time.sleep(0.1)       

        
