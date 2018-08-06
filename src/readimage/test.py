# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from datetime import datetime
import time
import cv2
import pickle
from client import cameraObj

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1296, 972)
camera.framerate = 30
# camera.brightness = 60
rawCapture = PiRGBArray(camera, size=(1296, 972))
count = 0
# allow the camera to warmup
time.sleep(0.1)


serverObj = cameraObj()

serverObj.hostname = "localhost"
serverObj.port = 9000

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array4
    currentdatetime = datetime.now().strftime("%m-%d-%Y:%H-%M-%S")
    # show the frame

    data = pickle.dumps(image);]
    serverObj.data = data
    serverObj.sendData()

    cv2.imshow("Frame", image)
    if count%10 == 0:
        filename = "frame {0}.jpg".format(currentdatetime)
        print filename
        cv2.imwrite(filename, image)
    count += 1
    print('Read a new frame')
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break