import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
GPIO.setup(4,GPIO.OUT)
while True:
    if GPIO.input(21):
        print ("no Blink")
        GPIO.output(4,GPIO.LOW)
    else:
        print ("blink")
        GPIO.output(4,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(4,GPIO.LOW)
        time.sleep(0.5)
