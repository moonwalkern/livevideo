import socket
import struct



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



