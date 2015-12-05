from time import sleep
from math import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

for i in range(0,361):
	print i
	xt = sqrt(pow(sin(radians(i)),2))
	if i%3 == 0:
		GPIO.output(12, GPIO.HIGH)
	if i%3 == 1:
		GPIO.output(16, GPIO.HIGH)
	if i%3 == 2:
		GPIO.output(18, GPIO.HIGH)
	sleep(xt*.1)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	sleep(.05)


