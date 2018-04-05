ReadMe
------

Preparations
------------
- Make sure that you have hsmm-pi installed and configured on the required raspberry pi's, if not, please clone this: https://github.com/urlgrey/hsmm-pi and flow the configurations instructions provided in the repo.

- Make sure python-xbee is installed and configured on the required raspberry pi's, if not please clone this: https://github.com/thom-nic/python-xbee and install it by going in the directory and typing: sudo python setup.py install.

- Make sure that you have the xbee's are configured correctly.

- make sure that node-red is installed o the gateway/server node

Starting Code
-------------
- Make sure that every Raspberry Pi has the right sensor-folder depending on the sensor attached to it.

- To start up the gateway, start by executing: node-red-start. go to https://<node-IP>:1880, Make sure that you have node-red configured properly where it points to the right server file. lastly start the code on node-red.

- "Cd" to the folder and run the Client program using: python <name-of-file>.py

Note
---- 
- make sure to start the server before starting the clients in order not to lose data or for the clients to stop.

- For more information please contact one of the "Disaster Response" group members.

