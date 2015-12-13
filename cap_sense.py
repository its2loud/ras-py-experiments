#!/user/bin/env python
# https://bitbucket.org/boblemarin/raspberrypi-capacitive-sensor/src/1c18fad88ae70ce1d83dee9c43528e27664a150d/CapSense1/CapSenseAndLEDs.py?at=master&fileviewer=file-view-default
# http://hackaday.com/2011/11/21/simple-touch-sensors-with-the-arduino-capsense-library/

import RPi.GPIO as GPIO
from time import sleep

timeout = 10000
total = 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def CapRead(inPin,outPin):
    total = 0
    
    # set Send Pin Register low
    GPIO.setup(outPin, GPIO.OUT)
    GPIO.output(outPin, GPIO.LOW)
    
    # set receivePin Register low to make sure pullups are off 
    GPIO.setup(inPin, GPIO.OUT)
    GPIO.output(inPin, GPIO.LOW)
    GPIO.setup(inPin, GPIO.IN)
    
    # set send Pin High
    GPIO.output(outPin, GPIO.HIGH)
    
    # while receive pin is LOW AND total is positive value
    while(GPIO.input(inPin) == GPIO.LOW and total < timeout ):
        total+=1
    
    if ( total > timeout ):
        return -2 # total variable over timeout
        
     # set receive pin HIGH briefly to charge up fully - because the while loop above will exit when pin is ~ 2.5V 
    GPIO.setup( inPin, GPIO.OUT )
    GPIO.output( inPin, GPIO.HIGH )
    GPIO.setup( inPin, GPIO.IN )
    
    # set send Pin LOW
    GPIO.output( outPin, GPIO.LOW ) 

    # while receive pin is HIGH  AND total is less than timeout
    while (GPIO.input(inPin)==GPIO.HIGH and total < timeout) :
        total+=1
    
    if ( total >= timeout ):
        return -2
    else:
        return total


GPIO.setup(24, GPIO.OUT)
red = GPIO.PWM(24, 100)
red.start(0) 

while True:
    if CapRead(7,8) > 300:
        red.ChangeDutyCycle(100)
    else:
        red.ChangeDutyCycle(0)
    sleep(.25)


GPIO.cleanup()