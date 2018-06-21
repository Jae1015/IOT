import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

while True:
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    time.sleep(2)
