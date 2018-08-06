import socket
import struct
import cv2
import pickle
from datetime import datetime

s = socket.socket()
host = '' #ip of raspberry pi
port = 9000
s.bind((host, port))

s.listen(5)

data = ""
payload_size = struct.calcsize("L")

currentdatetime = datetime.now().strftime("%m-%d-%Y:%H-%M-%S")

while True:
    c, addr = s.accept()
    print ('Got connection from',addr)
    c.send('Thank you for connecting')
    data = c.recv(20)
    print 'received ', data

    while len(data) < payload_size:
        data += c.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += c.recv(4096)
    frame_data = data[:msg_size]
    frame=pickle.loads(frame_data)
    print frame
    cv2.imshow('frame',frame)
    currentdatetime = datetime.now().strftime("%m-%d-%Y:%H-%M-%S")
    filename = "frame from client {0}.jpg".format(currentdatetime)
    print filename
    cv2.imwrite(filename, frame)
    # count += 1

    # c.close()