##!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math
import serial
import xbee

DO = 17
GPIO.setmode(GPIO.BCM)

ser = serial.Serial('/dev/ttyUSB0', 9600)
xbee = xbee.DigiMesh(ser)

def setup():
	ADC.setup(0x48)
	GPIO.setup(DO, GPIO.IN)

def loop():
	status = 1
	while True:
		fire = ADC.read(0)
		print fire
		if fire <= 123:
			fire = 1
			print 'fire'
		else:
			print 'no fire'
			fire = 0 
		xbee.tx(dest_addr=b'\x00\x00\x00\x00\x00\x00\xff\xff', data="Fire : "+ str(fire))
		tmp = GPIO.input(DO);
		if tmp != status:
			Print(tmp)
			status = tmp
		
		time.sleep(5)

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		pass	
