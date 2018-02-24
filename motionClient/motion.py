import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
while True:
       time.sleep(0.1)
       i=GPIO.input(11)
       print i
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
