import time
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

random.seed(time.time())

while 1:
	GPIO.output(random.randrange(22, 27, 2), GPIO.HIGH)
	GPIO.output(random.randrange(22, 27, 2), GPIO.LOW)
	time.sleep(.1)
