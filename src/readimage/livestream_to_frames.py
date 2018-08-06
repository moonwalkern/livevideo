import cv2
from datetime import datetime
import pickle
from client import cameraObj

feed = cv2.VideoCapture(0)
feed.set(cv2.CAP_PROP_FPS, 60.0)
count = 0
framerate = feed.get(5)
currentdatetime = datetime.now().strftime("%m-%d-%Y:%H-%M-%S")
print currentdatetime

serverObj = cameraObj()

serverObj.hostname = "localhost"
serverObj.port = 9000

#feed.read()[0] is True unless there is no frame to grab (e.g. camera not working)
while feed.read()[0]:
    # Grab the current frame
    current_frame = feed.read()[1]
    data = pickle.dumps(current_frame)
    serverObj.data = data
    serverObj.sendData()
    currentdatetime = datetime.now().strftime("%m-%d-%Y:%H-%M-%S")
    # Show the current frame in a window called "Me"
    #cv2.imshow('Me', current_frame)

    #feed.set(cv2.CAP_PROP_POS_MSEC,100000)
    # if count%3 == 0:
    filename = "frame {0}.jpg".format(currentdatetime)
    print filename
    # cv2.imwrite(filename, current_frame)
    count += 1
    print('Read a new frame')
    
    # Pauses to make computer time = real time
    # and allows pressing "q" on the keyboard
    # to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break


cv2.destroyWindow('Me')
feed.release()