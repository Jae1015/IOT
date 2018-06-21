import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)


while True:
    if GPIO.input(21):
        print ("led and buzzen on")
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(1)
    else:
        print ("led and buzzer off")
        GPIO.output(4,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)
        time.sleep(1)
