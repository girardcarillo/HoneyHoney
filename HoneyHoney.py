#! /usr/bin/python2

import time
import sys
import paho.mqtt.client as mqtt

EMULATE_HX711=False

HourSec = lambda hour : hour*60*60

referenceUnit = 1
DataTime = HourSec(3) # Data taking frequency in hour

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

hx = HX711(5, 6)

hx.set_reading_format("MSB", "MSB")

hx.set_reference_unit(24)
# hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()

print("Tare done! Add weight now...")

while True:
    try:
        val = hx.get_weight(5)
        print(val)

        hx.power_down()
        hx.power_up()

        myClient = mqtt.Client()

        # myClient.connect("test.mosquitto.org", 1883)
        myClient.connect("mqtt.avsit.io", 1883)
        myClient.publish("HoneyWeight",val)

        time.sleep(DataTime)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
