# http://raspi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control

from time import sleep
from math import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

pause_time = 0.01
freq = 60

red = GPIO.PWM(12, freq)
yel = GPIO.PWM(16, freq)
gre = GPIO.PWM(18, freq)
red.start(0)  
yel.start(0)  
gre.start(0)  

while 1:  
    for i in range(0,181):
    	xt_r = sqrt(pow( 100 * sin(radians(i)) ,2))
    	xt_y = sqrt(pow( 100 * sin(radians(i)+70) ,2))
    	xt_g = sqrt(pow( 100 * sin(radians(i)+140) ,2))
        red.ChangeDutyCycle(100-xt_r)
        yel.ChangeDutyCycle(100-xt_y)
        gre.ChangeDutyCycle(100-xt_g)
        sleep(pause_time)
