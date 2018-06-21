import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
GPIO.setup(4,GPIO.OUT)
while True:
    if GPIO.input(21):
        print ("Natural light present")
        GPIO.output(4,GPIO.LOW)
    else:
        print ("NO natural light")
        GPIO.output(4,GPIO.HIGH)
        print ("high")
        time.sleep(0.5)
        GPIO.output(4,GPIO.LOW)
        print ("low")
        time.sleep(0.5)
