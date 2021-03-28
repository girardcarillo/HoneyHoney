## HoneyHoney project

Python Software developed to build a Raspberry Pi scale, using Weight Sensor HX711.
Main code HoneyHoney.py largely inspired by https://github.com/tatobari/hx711py 
Useful tuto to build your scale: https://tutorials-raspberrypi.com/digital-raspberry-pi-scale-weight-sensor-hx711/

Data are sent to a MQTT broker.

This project was initially developed to remotely control the weigh of a hive, in order to determine the best time for harvest.

Many thanks to Seb ;)

# Using MQTT client with Pyhton

If you want to use this feature, please download the librairy.
For Linux:
```
sudo apt-get install -y python-paho-mqtt
```

# Calibrating your scale

In file HoneyHoney.py search for the line 
```
hx.set_reference_unit(24)
```
and comment it. Uncomment the line
```
# hx.set_reference_unit(referenceUnit)
```

In your terminal run 
```
sudo python HoneyHoney.py
```

![image](RaspiScale.jpg)
