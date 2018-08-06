from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-f", "--first", required=True,
#                 help="first input image")
# ap.add_argument("-s", "--second", required=True,
#                 help="second")
# args = vars(ap.parse_args())

imageA = cv2.imread('/Users/sreeji/Documents/Sreeji/work/ImageRecg/images/image1.png')
imageB = cv2.imread('/Users/sreeji/Documents/Sreeji/work/ImageRecg/images/image2.png')


# load the two input images
def compareImages(imageA, imageB):

    height, width, channels = imageA.shape          ## pick the original image size and resize the image that would be compared
    # print height
    # print width

    imageB = cv2.resize(imageB,(width,height),fx=0.0, fy=0.0)
    # print imageB.shape
    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # print imageA.shape
    # print imageB.shape

    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

    if(score == 1.0):
        print "good image"
        return True
    else:
        print "bad image"
        return False



print compareImages(imageA, imageB)