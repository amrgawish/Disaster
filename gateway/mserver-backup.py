
import socket
import threading
from SocketServer import ThreadingMixIn
import serial
import xbee
import json
import time

ACK = 'ACK'

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(threading.Thread):

    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        while True :
            data = conn.recv(2048).split(" : ")  # for temperature
            print  json.dumps({"d" : {data[0] : data[1]}, "Source" : self.ip, "TimeStamp" : time.time(), "CommunicationTech" : "WIFI"})
            conn.send(ACK)

class xbeelistner (threading.Thread):

        def __init__ (self):
                threading.Thread.__init__(self)

        def run(self):
                import xbee
                ser = serial.Serial('/dev/ttyUSB0', 9600)
                xbee = xbee.DigiMesh(ser)
		print ('Server XBEE communication established:  Waiting for data from XBEE clients ...')
                while True:
                        frame = xbee.wait_read_frame()
			data = frame['data'].split(" : ")
			addr = ':'.join("{:02x}".format(ord(c)) for c in frame['source_addr'])
			print  json.dumps({"d" : {data[0] : data[1]}, "Source" : addr , "TimeStamp" : time.time(), "CommunicationTech" : "XBEE"})


# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0'
TCP_PORT = 2004
BUFFER_SIZE = 1024

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

#setting the xbee listener
thread = xbeelistner ()
thread.start()
threads.append(thread)



while True:
    tcpServer.listen(4)
    print "Server WIFI communication established : Waiting for connections from TCP clients..."
    (conn, (ip,port)) = tcpServer.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)


for t in threads:
    t.join()
