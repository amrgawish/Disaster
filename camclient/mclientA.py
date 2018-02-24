# Python TCP Client A

from picamera import PiCamera
import time
import os

host = "192.168.43.9"

camera = PiCamera()
count = 0

while True:
    time.sleep(10)
    name = 'tempPic'+str(count)+'.jpg'
    camera.capture(name)
    count+=1
    os.system("sshpass -p 'raspberry' scp "+name+" "+host+":/home/pi/Disaster/pictures && rm "+name)




