import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Trig=23
Echo=24
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

while True:

    GPIO.output(Trig,False)
    print "waiting for sensor to setup"
    time.sleep(2)

    GPIO.output(Trig,True)
    time.sleep(0.00001)
    GPIO.output(Trig,False)

    while GPIO.input(Echo)==0 :
        st=time.time()

    while GPIO.input(Echo)==1 :
        ft=time.time()

    du=ft-st
    dist=du*17150
    dist=round(dist,2)

    if dist>2 and dist<400 :
        print "Distance ",dist-0.5,"cm"

    else:
        print "OUT OF RANGE"
     
