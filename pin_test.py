import time
import RPi.GPIO as GPIO

pin = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

while 1:
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(2)

