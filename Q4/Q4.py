import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
GPIO.setup(4,GPIO.OUT) #led1
GPIO.setup(17,GPIO.OUT) #buzzer
GPIO.setup(26,GPIO.OUT) #led2
GPIO.setup(20,GPIO.OUT) #led3

x=0
GPIO.output(17,GPIO.LOW)
while True:
    if (GPIO.input(21) and x==0):
        print ("1st touch")
       
        x+=1
        GPIO.output(4,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(4,GPIO.LOW)
        time.sleep(2)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(17,GPIO.LOW)
        
    elif (GPIO.input(21) and x==1):
        print ("2nd touch")
        x+=1
        GPIO.output(26,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(26,GPIO.LOW)
        time.sleep(1)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(17,GPIO.LOW)
        
        
    elif (GPIO.input(21) and x==2):
        print ("3rd touch")
        x+=1
        GPIO.output(20,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(20,GPIO.LOW)
        time.sleep(1)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(17,GPIO.LOW)
        
   
