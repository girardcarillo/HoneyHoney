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
hx.set_reference_unit(referenceUnit)
```

In your terminal run 
```
sudo python HoneyHoney.py
```
The values printed on your screen 

The correct calibration of the weight sensor and the Raspberry Pi balance is crucial. For this we need a comparison object whose weight we know. 
For example, take two packs of milk (1kg each), but keep in mind it is recommended to choose an average value of the maximum you want to weigh.
Place it on the scale and run the Python code again.
The displayed values can be positive as well as negative.
For example, if at 2kg (= 2000 gramm) values around -882000 are displayed, then the reference value is -882000 ÷ 2000 = -41.
Then edit the HoneyHoney.py file in the same way as above described, remove the comment hashtag and enter this value accordingly. 
The line now looks as follows:

```	
hx.set_reference_unit(-441)
# hx.set_reference_unit(referenceUnit)
```

You can now test to weigh the world.
 
![image](RaspiScale.jpg)
