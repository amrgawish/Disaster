import xbee
import time
import serial

def xyz():
	ser = serial.Serial('/dev/ttyUSB0', 9600)
	xbee = xbee.DigiMesh(ser)

	while True:
		print ('waiting for data')
		frame = xbee.wait_read_frame()
		print ('from: ' + frame['source_addr'] + 'data:' + frame['data'])


thread.start_new_thread(xyz,('hala',))

