
import time
import serial
import threading

class xyz (threading.Thread):

	def __init__ (self,hi):
		threading.Thread.__init__(self)
		print hi

	def run(self):
		import xbee
		ser = serial.Serial('/dev/ttyUSB0', 9600)
		xbee = xbee.DigiMesh(ser)

		while True:
			print ('waiting for data')
			frame = xbee.wait_read_frame()
			print ('from: ' + frame['source_addr'] + 'data:' + frame['data'])

threads= []
thread = xyz('initilized')

thread.start()
threads.append(threads)

thread.join()
