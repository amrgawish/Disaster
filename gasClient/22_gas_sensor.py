#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math
import serial
import xbee

DO = 17
GPIO.setmode(GPIO.BCM)
ser = serial.Serial('/dev/ttyUSB0',9600)
xbee = xbee.DigiMesh(ser)

def setup():
	ADC.setup(0x48)
	GPIO.setup	(DO, 	GPIO.IN)

def Print(x):
	if x == 1:
		print ''
		print '   *********'
		print '   * Safe~ *'
		print '   *********'
		print ''
	if x == 0:
		print ''
		print '   ***************'
		print '   * Danger Gas! *'
		print '   ***************'
		print ''

def loop():
	status = 1
	count = 0
	while True:
		x = ADC.read(0)
		print x
		xbee.tx(dest_addr=b'\x00\x00\x00\x00\x00\x00\xff\xff', data="Gas : "+str(x))
		tmp = GPIO.input(DO);
		if tmp != status:
			status = tmp
		time.sleep(6)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		destroy()
