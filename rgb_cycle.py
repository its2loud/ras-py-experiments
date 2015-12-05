import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.OUT) #R
GPIO.setup(24, GPIO.OUT) #G
GPIO.setup(22, GPIO.OUT) #B

delay = .5

while 1:
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	time.sleep(delay)
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(22, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(26, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(22, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(26, GPIO.LOW)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(22, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(26, GPIO.LOW)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(22, GPIO.LOW)
	time.sleep(delay)
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(22, GPIO.LOW)
	time.sleep(delay)

