#!/usr/bin/python

# Standard import
import cv2


k = 0
# Initiates param variables in default value
params = cv2.SimpleBlobDetector_Params()

def nothing(valueArea):
    global params, detector

    minimumArea = cv2.getTrackbarPos("minimum area", "image")
    #print(minimumArea)
    params.filterByArea = True
    params.minArea = minimumArea
    #print(params.maxArea)
    detector = cv2.SimpleBlobDetector_create(params)
    return params.minArea, params, detector

def nothing2(valueArea2):
    global params, detector

    maximumArea = cv2.getTrackbarPos("maximum area", "image")
    #print(minimumArea)
    params.filterByArea = True
    params.maxArea = maximumArea
    detector = cv2.SimpleBlobDetector_create(params)
    #print(params.maxArea)
    return params.maxArea, params, detector


def reseting(resetToggle):
    global img, params, detector, k
    #print(resetToggle)
    if resetToggle == True:
        
        """if k == 0:
            print("k is 0", k)
            params = cv2.SimpleBlobDetector_Params()
            detector = cv2.SimpleBlobDetector_create(params)
            k = k + 1
        else:"""
        #print(k)
        print(params.minArea, params.maxArea)
        keypoints = detector.detect(img)
        print("the number of blobs:", len(keypoints))
        for k in keypoints:
            cv2.circle(img, (int(k.pt[0]), int(k.pt[1])), int(k.size/2), (0, 0, 255), -1)
    else:
        img = cv2.imread('circles/holes_3.jpeg')
        keypoints = []
        #params.minArea = 0

    return params.minArea, params.maxArea, params, detector
# Read image
img = cv2.imread('circles/holes_3.jpeg')

# Setup SimpleBlobDetector parameters.
#params.filterByArea = True
#params.minArea = 10 #  100          10
#params.maxArea = 800 # 800 for 6 ; 800 for 102
# Change thresholds

cv2.namedWindow('image')
# the "nothing" functions change the params, 
# and the reset toggle is a switch to display the blobs detectes
cv2.createTrackbar('minimum area','image',0,400,nothing)
cv2.createTrackbar('maximum area','image',100,800,nothing2)
"""
cv2.createTrackbar('minimum threshold','image',0,400,nothing)
cv2.createTrackbar('maximum threshold','image',100,400,nothing2)
cv2.createTrackbar('minimum circularity','image',0,400,nothing)
cv2.createTrackbar('maximum circularity','image',100,400,nothing2)
cv2.createTrackbar('minimum convexity','image',0,400,nothing)
cv2.createTrackbar('maximum convexity','image',100,400,nothing2)
cv2.createTrackbar('minimum inertia','image',0,400,nothing)
cv2.createTrackbar('maximum inertia','image',100,400,nothing2)
cv2.createTrackbar('minimum distance between Blobs','image',0,400,nothing)
cv2.createTrackbar('maximum distance between Blobs','image',100,400,nothing2)"""
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'

cv2.createTrackbar(switch,'image',0,1,reseting)
while(1):
    #cv2.imshow("Object Detection", img)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

    im = cv2.resize(img, None,fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)
    cv2.imshow("image", im)


cv2.destroyAllWindows()