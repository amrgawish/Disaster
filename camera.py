from picamera import PiCamera
from time import sleep

camera = PiCamera()
count = 0
while (True):
	sleep(10)
	camera.capture('shahad'+str(count)+'.jpg')
	count += 1
