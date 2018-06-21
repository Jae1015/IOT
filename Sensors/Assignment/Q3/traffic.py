
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

R1=4
Y1=17
G1=27

R2=22
Y2=23
G2=24

R3=5
Y3=6
G3=12

R4=13
Y4=19
G4=16


GPIO.setup(R1,GPIO.OUT)
GPIO.setup(Y1,GPIO.OUT)
GPIO.setup(G1,GPIO.OUT)

GPIO.setup(R2,GPIO.OUT)
GPIO.setup(Y2,GPIO.OUT)
GPIO.setup(G2,GPIO.OUT)

GPIO.setup(R3,GPIO.OUT)
GPIO.setup(Y3,GPIO.OUT)
GPIO.setup(G3,GPIO.OUT)

GPIO.setup(R4,GPIO.OUT)
GPIO.setup(Y4,GPIO.OUT)
GPIO.setup(G4,GPIO.OUT)

while True:

    GPIO.output(G3,1)
    GPIO.output(R1,1)
    GPIO.output(Y1,0)
    GPIO.output(G1,0)
    GPIO.output(R2,0)
    GPIO.output(Y2,1)
    GPIO.output(G2,0)
    GPIO.output(R3,0)
    GPIO.output(Y3,0)
    GPIO.output(R4,0)
    GPIO.output(Y4,1)
    GPIO.output(G4,0)
    time.sleep(10)

    GPIO.output(G4,1)
    GPIO.output(R1,0)
    GPIO.output(Y1,1)
    GPIO.output(G1,0)
    GPIO.output(R2,1)
    GPIO.output(Y2,0)
    GPIO.output(G2,0)
    GPIO.output(R3,0)
    GPIO.output(Y3,1)
    GPIO.output(G3,0)
    GPIO.output(R4,0)
    GPIO.output(Y4,0)
    time.sleep(10)

    GPIO.output(R1,0)
    GPIO.output(Y1,0)
    GPIO.output(G1,1)
    GPIO.output(R2,0)
    GPIO.output(Y2,1)
    GPIO.output(G2,0)
    GPIO.output(R3,1)
    GPIO.output(Y3,0)
    GPIO.output(G3,0)
    GPIO.output(R4,0)
    GPIO.output(Y4,1)
    GPIO.output(G4,0)
    time.sleep(10)

    GPIO.output(R1,0)
    GPIO.output(Y1,1)
    GPIO.output(G1,0)
    GPIO.output(R2,0)
    GPIO.output(Y2,0)
    GPIO.output(G2,1)
    GPIO.output(R3,0)
    GPIO.output(Y3,1)
    GPIO.output(G3,0)
    GPIO.output(R4,1)
    GPIO.output(Y4,0)
    GPIO.output(G4,0)
    time.sleep(10)
        
        
       
   
