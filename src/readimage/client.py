import socket
import cv2
import struct
from datetime import datetime

feed = cv2.VideoCapture(0)
feed.set(cv2.CAP_PROP_FPS, 60.0)
count = 0
framerate = feed.get(5)
currentdatetime = datetime.now().strftime("%m-%d-%Y:%H-%M-%S")


class cameraObj():
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.hostname = 'localhost'
        self.port = 9000
        self.data = "starting"

    def sendData(self):
        s = socket.socket()
        host = self.hostname
        port = self.port

        s.connect((host, port))
        s.sendall(struct.pack("L", len(self.data))+self.data)
        print(s.recv(1024))
        s.close()


# camera = cameraObj()
#
# camera.hostname = "localhost"
# camera.port = 9000
# camera.data = "hello yes"
# camera.sendData()



