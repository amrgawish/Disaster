#!/usr/bin/python

from SimpleServer import SimpleServer
import socket
server = SimpleServer("0.0.0.0", 30000) # listen on port 30000 
server.initialise()
server.serve_forever()
