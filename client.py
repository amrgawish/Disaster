import sys
import socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = sys.argv[1]
print "Target: ",target
sock.connect((target,30000)) 
msg = sock.recv(1024)
print "Message recieved: ", msg
sock.close()
