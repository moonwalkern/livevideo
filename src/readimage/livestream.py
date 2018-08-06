import io
import cv2
from datetime import datetime
import picamera


feed = cv2.VideoCapture(0)
count = 0

if feed is None:
    print 'BUT REALLY HERE'
#feed.read()[0] is True unless there is no frame to grab (e.g. camera not working)
while feed.read()[0]:
    print 'GOT HERE'
        
# Grab the current frame
    current_frame = feed.read()[1]
    currentdatetime = datetime.now().strftime("%m-%d-%Y:%H-%M-%S")
                    
# Show the current frame in a window called "Me"
    cv2.imshow('Me', current_frame) 
                                
    if count%10 == 0:
        filename = "frame {0}.jpg".format(currentdatetime)
        print filename
        cv2.imwrite(filename, current_frame)
    count += 1
    print('Read a new frame')
                                                                            
# Pauses to make computer time = real time
# and allows pressing "q" on the keyboard to break the loop

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

    cv2.destroyWindow('Me')
    feed.release()
