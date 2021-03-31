#! /usr/bin/python2

import time
import sys
import paho.mqtt.client as mqtt
import os.path
from datetime import date
from datetime import datetime

EMULATE_HX711=False

HourSec = lambda hour : hour*60*60

referenceUnit = 1
DataTime = HourSec(3*0.0001) # Data taking frequency in hour
today = date.today()
now = datetime.now()

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()

    print("Bye!")
    sys.exit()

# Method to check whether or not your raspi is connected to the internet
# to use this method add 
# import socket
# import requests 
# def is_connected():
#      try:
#          # connect to the host -- tells us if the host is actually
#          # reachable 
#          if socket.create_connection(("1.1.1.1", 53)):
#              # requests.get('https://1.1.1.1/').status_code
#              return True
#          else:
#              return False
#      except OSError:
#          pass
#      return False


# waiting for the internet connection to establish
# a more sophisticated way can be obtained by using the is_connected() method at the beginning of this code.
time.sleep(60)

hx = HX711(5, 6)

hx.set_reading_format("MSB", "MSB")

# hx.set_reference_unit(25)
hx.set_reference_unit(referenceUnit)

hx.reset()
hx.tare()

# Tare scale if not already done
if not os.path.isfile('/home/pi/HoneyHoney/tare.txt'):
    print ("First use of the scale, taring...")

    date = today.strftime("%m/%d/%y")
    hour = now.strftime("%H:%M:%S")

    text_list = ["The tare has been done the ", date, " at ", hour, " (pi time)"]
    f = open("tare.txt", "a")
    f.writelines(text_list)
    f.close()

print("Tare done! Add weight now...")


while True:
    try:
            
        val = hx.get_weight(5)
        print(val)

        hx.power_down()
        hx.power_up()
                
        myClient = mqtt.Client()
        myClient.connect("mqtt.avsit.io", 1883)
        myClient.publish("HoneyWeight",val)

        time.sleep(DataTime)

    except (KeyboardInterrupt, SystemExit):
            cleanAndExit()

