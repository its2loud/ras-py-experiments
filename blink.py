import time
import math
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
delay_time=0.1

for i in range(0,40):
	GPIO.output(12, GPIO.LOW)
	GPIO.output(18, GPIO.HIGH)
	time.sleep(delay_time)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(12, GPIO.HIGH)
	time.sleep(delay_time)

GPIO.output(12, GPIO.LOW)

