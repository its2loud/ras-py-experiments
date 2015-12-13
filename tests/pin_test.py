import time
import RPi.GPIO as GPIO

pin = 23

# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

while 1:
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)

	
GPIO.cleanup()