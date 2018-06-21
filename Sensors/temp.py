import Adafruit_DHT
import time
import serial
sensor=Adafruit_DHT.DHT11
pin=22
while True:
	humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
	if humidity is not None and temperature is not None:
		print "temp={0:0.1f}*C Humidity={1:0.1f}% ".format(temperature,humidity)
	else:
            print"fail to get reading"
