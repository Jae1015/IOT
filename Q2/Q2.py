import RPi.GPIO as GPIO
import time

sound=21
motion=26
LED=4
Buzzer=17

GPIO.setmode(GPIO.BCM)
GPIO.setup(sound,GPIO.IN)
GPIO.setup(motion,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(Buzzer,GPIO.OUT)

while True:
    if (GPIO.input(sound) & GPIO.input(motion)):
        GPIO.output(LED,GPIO.HIGH)
        GPIO.output(Buzzer,GPIO.HIGH)
        print ("sound and motion detected")
        time.sleep(1)
    else:
        GPIO.output(LED,GPIO.LOW)
        GPIO.output(Buzzer,GPIO.LOW)
        print ("sound and motion not detected")
        time.sleep(1)
