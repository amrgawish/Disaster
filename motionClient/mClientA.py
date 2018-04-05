import socket
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor

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
       			time.sleep(10)
       			i = GPIO.input(11)
       			if True: #i == 1:
       				MESSAGE = "motion : 1"
       				tcpClientA.send(MESSAGE)
				data = tcpClientA.recv(BUFFER_SIZE)
	                        print " Client2 received data:", data
#				time.sleep(10)
       			elif i == 0:
				continue
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
