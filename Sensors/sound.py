import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
GPIO.setup(4,GPIO.OUT)
while True:
    if GPIO.input(21):
        print ("sound detected")
        GPIO.output(4,GPIO.HIGH)
        time.sleep(1)
    else:
        print ("no sound")
        GPIO.output(4,GPIO.LOW)
        time.sleep(1)
