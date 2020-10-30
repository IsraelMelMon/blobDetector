#!/usr/bin/python

# Standard import
import cv2


k = 0
# Initiates param variables in default value
params = cv2.SimpleBlobDetector_Params()

def areaMax(value):
    global params, detector

    maximumArea = cv2.getTrackbarPos("maximum area", "image2")
    #print(minimumArea)
    params.filterByArea = True
    params.maxArea = maximumArea
    #print(params.maxArea)
    detector = cv2.SimpleBlobDetector_create(params)
    return params.maxArea, params, detector

def areaMin(value2):
    global params, detector

    minimumArea = cv2.getTrackbarPos("minimum area", "image2")
    #print(minimumArea)
    params.filterByArea = True
    params.minArea = minimumArea
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.minArea, params, detector

def threshMin(value3):
    global params, detector

    minimumThreshold = cv2.getTrackbarPos("minimum threshold", "image2")
    #print(minimumArea)
    #params.filterByArea = True
    params.minThreshold = minimumThreshold
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.minThreshold, params, detector

def threshMax(value4):
    global params, detector

    maximumThreshold = cv2.getTrackbarPos("maximum threshold", "image2")
    #print(minimumArea)
    #params.filterByArea = True
    params.maxThreshold = maximumThreshold
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.maxThreshold, params, detector

def circMin(value5):
    global params, detector

    minimumCircularity = cv2.getTrackbarPos("minimum circularity", "image2")
    #print(minimumArea)
    params.filterByCircularity = True
    params.minCircularity = minimumCircularity / 100
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.minCircularity, params, detector

def circMax(value6):
    global params, detector

    maximumCircularity = cv2.getTrackbarPos("maximum circularity", "image2")
    #print(minimumArea)
    params.filterByCircularity= True
    params.maxCircularity = maximumCircularity / 100
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.maxCircularity, params, detector

def convMin(value7):
    global params, detector

    minimumConvexity = cv2.getTrackbarPos("minimum convexity", "image2")
    #print(minimumArea)
    params.filterByConvexity = True
    params.minConvexity = minimumConvexity / 100
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.minConvexity, params, detector

def convMax(value8):
    global params, detector

    maximumConvexity = cv2.getTrackbarPos("maximum convexity", "image2")
    #print(minimumArea)
    params.filterByConvexity = True
    params.maxConvexity = maximumConvexity / 100
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.maxConvexity, params, detector

def inertMin(value9):
    global params, detector

    minimumInertia = cv2.getTrackbarPos("minimum inertia", "image2")
    #print(minimumArea)
    params.filterByInertia = True
    params.minInertiaRatio = minimumInertia / 100
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.minInertiaRatio, params, detector

def inertMax(value10):
    global params, detector

    maximumInertia = cv2.getTrackbarPos("maximum inertia", "image2") 
    #print(minimumArea)
    params.filterByInertia = True
    params.maxInertiaRatio = maximumInertia / 100
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.maxInertiaRatio, params, detector

def distMin(value11):
    global params, detector

    minimumDist = cv2.getTrackbarPos("minimum distance", "image2")
    #print(minimumArea)
    params.minDistBetweenBlobs = minimumDist
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.minDistBetweenBlobs, params, detector


def reseting(resetToggle):
    global img, params, detector, k
    #print(resetToggle)
    if resetToggle == True:
        #default parameters
        """if k == 0:
            print("k is 0", k)
            params = cv2.SimpleBlobDetector_Params()
            detector = cv2.SimpleBlobDetector_create(params)
            k = k + 1
        else:"""
        #print(k)
        #print(params.minArea, params.maxArea)
        keypoints = detector.detect(img)
        print("the number of blobs:", len(keypoints))
        
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10,500)
        fontScale              = 1
        fontColor              = (255,255,255)
        lineType               = 2

        cv2.putText(img,"# blobs:"+ str(len(keypoints)), 
            bottomLeftCornerOfText, 
            font, 
            fontScale,
            fontColor,
            lineType)
        for k in keypoints:
            cv2.circle(img, (int(k.pt[0]), int(k.pt[1])), int(k.size/2), (0, 0, 255), -1)
    else:
        img = cv2.imread('circles/holes_14.jpeg')
        keypoints = []
        #params.minArea = 0

    return params.minArea, params.maxArea, params, detector # check
# Read image
img = cv2.imread('circles/holes_14.jpeg')

# Setup SimpleBlobDetector parameters.
#params.filterByArea = True
#params.minArea = 10 #  100          10
#params.maxArea = 800 # 800 for 6 ; 800 for 102
# Change thresholds

cv2.namedWindow('image2')
# the "nothing" functions change the params, 
# and the reset toggle is a switch to display the blobs detectes

cv2.createTrackbar('minimum area','image2',0,400,areaMin)
cv2.createTrackbar('maximum area','image2',0,1000,areaMax)
cv2.createTrackbar('minimum threshold','image2',0,1000,threshMin)
cv2.createTrackbar('maximum threshold','image2',0,1000,threshMax)
cv2.createTrackbar('minimum circularity','image2',0,100,circMin)
cv2.createTrackbar('maximum circularity','image2',0,100,circMax)
cv2.createTrackbar('minimum convexity','image2',0,100,convMin)
cv2.createTrackbar('maximum convexity','image2',0,100,convMax)
cv2.createTrackbar('minimum inertia','image2',0,100,inertMin)
cv2.createTrackbar('maximum inertia','image2',0,100,inertMax)
cv2.createTrackbar('minimum distance between Blobs','image2',0,100,distMin)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'

cv2.createTrackbar(switch,'image2',0,1,reseting)
while(1):
    #cv2.imshow("Object Detection", img)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

    im = cv2.resize(img, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    cv2.imshow("image", im)


cv2.destroyAllWindows()