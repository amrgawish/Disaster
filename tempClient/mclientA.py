# Python TCP Client A
import socket
import RPi.GPIO as GPIO
import dht11
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=4)

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
    			result = instance.read()
    			if result.is_valid():
       				MESSAGE = "Temperature : "+str(result.temperature)
				tcpClientA.send(MESSAGE)
       				data = tcpClientA.recv(BUFFER_SIZE)
       				MESSAGE = "Humidity : "+str(result.humidity)
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
