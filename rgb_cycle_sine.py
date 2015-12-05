# http://raspi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control

from time import sleep
from math import *
import RPi.GPIO as GPIO

def fabsZ(value):
    if value < 0:
    	return 0
    else:
    	return fabs(value)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

delay = .05
freq = 100

red = GPIO.PWM(26, freq)
gre = GPIO.PWM(24, freq)
blu = GPIO.PWM(22, freq)
red.start(0)  
gre.start(0)  
blu.start(0)  

while 1:  
    for i in range(0,361):
    	x_r = fabsZ( 100 * sin(radians(i)) )
    	x_g = fabsZ( 100 * sin(radians(i)+90) )
    	x_b = fabsZ( 100 * sin(radians(i)+180) )
        red.ChangeDutyCycle(x_r)
        gre.ChangeDutyCycle(x_g)
        blu.ChangeDutyCycle(x_b)
        sleep(delay)
