# http://raspi.tv/how-to-install-wiringpi2-for-python-on-the-raspberry-pi
# https://sites.google.com/site/how2raspberrypi/gpio_library

import wiringpi2
from time import sleep

def tone(io, song):
        pin = 17 # only supported on this pin
        io.softToneCreate(pin)

        for i in range(len(song)):
                io.softToneWrite(pin, song[i])
                io.delay(200)

        io.softToneWrite(pin, 0)
        io.pinMode(pin, io.INPUT)

def toneS(io, tone):
	pin = 17 # only supported on this pin
	io.softToneCreate(pin)
	io.softToneWrite(pin, tone)
	io.delay(400)
	io.softToneWrite(pin, 0)
	#io.pinMode(pin, io.INPUT)

song = [ 659, 659, 0, 659, 523, 659, 0, 784, 0, 0, 0, 392, 0, 0, 0, 523, 0, 0, 392, 0, 0, 330 ]
io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_GPIO)
#tone(io, song)
toneS(io, 400)