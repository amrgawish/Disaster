import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import socket

DO = 17
GPIO.setmode(GPIO.BCM)
ADC.setup(0x48)
GPIO.setup(DO, GPIO.IN)

host = "192.168.43.9"
port = 2004
BUFFER_SIZE = 2000
timeoutCount = 0

while True:
	try:
		tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcpClientA.settimeout(3)
		tcpClientA.connect((host, port))
		while True:
       			MESSAGE = "Light : "+str(ADC.read(0))
				tcpClientA.send(MESSAGE)
       			data = tcpClientA.recv(BUFFER_SIZE)
				print " Client2 received data:", data
				time.sleep(10)
	except socket.timeout:
		tcpClientA.close()
		print "client reinitiated!"
                timeoutCount+= 1
                if timeoutCount > 3:
			print "server does not exist"
			break

	except socket.error, msg:
		tcpClientA.close()
		print "client reinitiated!"
		continue