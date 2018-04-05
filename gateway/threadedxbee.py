import xbee
import time
import serial
import thread

def xyz(name,xbee):
# 	ser = serial.Serial('/dev/ttyUSB0', 9600)
#	xbee = xbee.DigiMesh(ser)

	while True:
        	print ('waiting for data')
        	frame = xbee.wait_read_frame()
       		print ('from: ' + frame['source_addr'] + 'data:' + frame['data'])


ser = serial.Serial('/dev/ttyUSB0', 9600)
xbee = xbee.DigiMesh(ser)

try:
	thread.start_new_thread(xyz,('hala',xbee,))
except:
	print('error')
