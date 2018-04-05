#!/usr/bin/python
import serial
import xbee
ser = serial.Serial(‘/dev/ttyUSB0’, 9600)
xbee = xbee.DigiMesh(ser)

xbee.tx(dest_addr=b'\x00\x00\x00\x00\x00\x00\xff\xff', data="{'d':{ 'temprature' : 23 }, 'Soucrce' : 'node 1'}")
