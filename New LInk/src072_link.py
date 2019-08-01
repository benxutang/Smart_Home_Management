# demo uart transmit and receive



import time
from bluetooth import ble
import util
from bleuartlib import BleUartDevice
from gpiozero import MCP3008
from gpiozero import PWMLED
import RPi.GPIO as GPIO
import RPi.GPIO
import urllib.request
import json
import ssl

context = ssl._create_unverified_context()
    
RPi.GPIO.cleanup()
RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(37, RPi.GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
p = GPIO.PWM(37, 500)
p.start(0)

pot = MCP3008(0)

def http_get():
    url='https://nussh.happydoudou.xyz:5000/Light'
    response = urllib.request.urlopen(url,context=context)
    return response.read()

def bleUartReceiveCallback(data):
    ret = http_get()
    global state
    data=json.loads(ret.decode('utf-8'))

    for dict_data in data:
        print(dict_data)
        print("\n")

    time="0000-00-00 00:00:00"
    Ligcon=[]
    State=[]
    Timestamp=[]

    index=0

    for dict_data in data:
        Ligcon.append(dict_data['Ligcon'])
        State.append(dict_data['State'])
        Timestamp.append(dict_data['Timestamp'])

    for i ,value in enumerate(Timestamp):
        if value>time:
            index=i
            time=value
    if State[index]=='0':
        state=0
        Lightin=int(Ligcon)

    a=int(GPIO.input(18))
    if a>0:
        if state>=2:
            state=1
        else:
            state=state+1
        print("sb")

    if state==0:
        p.ChangeDutyCycle(Lightin)
    elif state==1:
        print('Received data = {}'.format(data))
        data = data.strip()[1:]
    
        if int(data)<50:
            p.ChangeDutyCycle(100)
            time.sleep(0.1)
            print(100)
        elif int(data)>1000:
            p.ChangeDutyCycle(0)
            time.sleep(0.1)
            print(0)
        else:
            p.ChangeDutyCycle(int(100.0-float((float(data))/10.0)))
            time.sleep(0.1)
            print(100.0-float((float(data))/10.0))
    else:
        print(int(pot.value*20)*5)
        p.ChangeDutyCycle(int(pot.value*20)*5)
        time.sleep(0.1)
    
    


try:
    state=1
    bleUartDevice1 = None
    found_microbit = False

    service = ble.DiscoveryService()
    devices = service.discover(2)

    print('********** Initiating device discovery......')

    for address,name in devices.items():

        found_microbit = False

        if address == 'CC:32:B1:DB:9F:07':

            print('Found BBC micro:bit [vavug]: {}'.format(address))
            found_microbit = True
            break       
    
    if found_microbit:

        bleUartDevice1 = BleUartDevice(address)
        bleUartDevice1.connect()
        print('Connected to micro:bit device')
        
        bleUartDevice1.enable_uart_receive(bleUartReceiveCallback)
        print('Receiving data...')
       
        while True:
           
            time.sleep(0.1)
            
except KeyboardInterrupt:
    
    print('********** END')
    
except Error as err:

    print('********** ERROR: {}'.format(err))

finally:

    if bleUartDevice1 != None:
        bleUartDevice1.disconnect()
        bleUartDevice1 = None
        print('Disconnected from micro:bit device')
        p.stop()
        RPi.GPIO.cleanup()
