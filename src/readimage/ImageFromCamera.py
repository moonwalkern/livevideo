import cv2
from FindImage import compareImages


vidcap = cv2.VideoCapture('/Users/sreeji/Documents/Sreeji/work/LiveStream-update/images_classification/mp4/big_buck_bunny_720p_5mb.mp4')
success,image = vidcap.read()
count = 0
success = True

imageA_circuit = cv2.imread('/Users/sreeji/Documents/Sreeji/work/ImageRecg/images/image1.png')
imageB_circuit = cv2.imread('/Users/sreeji/Documents/Sreeji/work/ImageRecg/images/image2.png')

# compareImages(imageA,imageB)
# this will be first circuit
while success:
    # cv2.imwrite("frame%d.jpg" % count, image)
    success,image = vidcap.read()
    # print 'Read a new frame: ', success
    # count += 1
    ret = compareImages(imageA_circuit,image)

    if(ret == True):
        print 'Image are similar, use this image for further processing (circuit one)'
        break
    else:
        print 'Image are different, checking next frame'


# this will be second circuit
while success:
    # cv2.imwrite("frame%d.jpg" % count, image)
    success,image = vidcap.read()
    # print 'Read a new frame: ', success
    # count += 1
    ret = compareImages(imageB_circuit,image)

    if(ret == True):
        print 'Image are similar, use this image for further processing (circuit two)'
        break
    else:
        print 'Image are different, checking next frame'