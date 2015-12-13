from graphics import *
from time import sleep

# def main():
win = GraphWin()
pt = Point(0, 50)
cir = Circle(pt, 25)
cir.draw(win)
# main()

while True:
	pt = Point(pt.x+1, 50)
	cir = Circle(pt, 25)
	cir.draw(win)
	# sleep(.1)
