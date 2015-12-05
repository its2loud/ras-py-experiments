import time
import math
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
# delay_time=0.1

for i in range(0,2):
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	time.sleep(2)
	GPIO.output(16, GPIO.HIGH)
	time.sleep(.5)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(18, GPIO.HIGH)
	time.sleep(2.5)


GPIO.output(18, GPIO.LOW)

