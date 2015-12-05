# http://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion

from time import sleep
from math import ceil
from colorsys import hsv_to_rgb
import RPi.GPIO as GPIO

delay = .02
freq = 50

GPIO.setmode(GPIO.BOARD)
pin_rgb = [26,24,22]
pwm_rgb = []
for pin in pin_rgb:
	GPIO.setup(pin, GPIO.OUT)
	pwm_pin = GPIO.PWM(pin, freq)
	pwm_pin.start(0)
	pwm_rgb.append(pwm_pin)

while 1:  
    for hue in range(0,360):
        rgb = tuple(ceil(i * 100) for i in hsv_to_rgb(hue/360.,1,1))
        for c in range(len(rgb)):
            pwm_rgb[c].ChangeDutyCycle(rgb[c])
        sleep(delay)
