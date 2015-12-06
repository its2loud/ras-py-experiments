# http://raspberrypi.stackexchange.com/questions/14680/raspberry-pi-gpio-input-pins-give-random-values

try:
	import RPi.GPIO as GPIO
	from time import sleep

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(8, GPIO.OUT)

	while True:
		if not GPIO.input(7):
			GPIO.output(8, GPIO.HIGH)
		else:
			GPIO.output(8, GPIO.LOW)

except KeyboardInterrupt:
	#GPIO.output(22, GPIO.LOW)
	GPIO.cleanup()