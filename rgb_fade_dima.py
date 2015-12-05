from math import sin, radians
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
channels = [12, 10, 16]
GPIO.setup(channels, GPIO.OUT)

freq = 60

red = GPIO.PWM(12, freq)
gre = GPIO.PWM(10, freq)
blu = GPIO.PWM(16, freq)
colors = [red, gre, blu]

map(lambda x: x.start(0), colors)

timeout = 0.01

while True:
 for i in range(0, 179):
 xt_r = abs(100 * sin(radians(i)))
 xt_g = abs(100 * sin(radians(i)+70))
 xt_b = abs(100 * sin(radians(i)+140))
 red.ChangeDutyCycle(100 - xt_r)
 blu.ChangeDutyCycle(100 - xt_b)
 gre.ChangeDutyCycle(100 - xt_g)
 sleep(timeout)