from time import sleep
from picamera import PiCamera
from fractions import Fraction

camera = PiCamera()
camera.resolution = (3280, 2464)
camera.framerate = Fraction(1, 6)
camera.sensor_mode = 3
camera.shutter_speed = 6000000
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(2) # wait 5 minutes
