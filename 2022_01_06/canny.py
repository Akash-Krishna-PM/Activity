#canny trackbar

import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing():
    pass

img=cv2.imread("C:\\Users\\Windows 10\\Downloads\\lena.jpg")

cv2.namedWindow("Trackbar thresholds")
cv2.createTrackbar("Lower Threshold","Trackbar thresholds",0,255,nothing)
cv2.createTrackbar("Upper Threshold","Trackbar thresholds",0,255,nothing)
while True:
    l_th=cv2.getTrackbarPos("Lower Threshold","Trackbar thresholds")
    u_th=cv2.getTrackbarPos("Upper Threshold","Trackbar thresholds")

    canny=cv2.Canny(img,l_th,u_th)
    cv2.imshow('gray',canny)
    k=cv2.waitKey(1) & 0xFF
    if k==27: #esc key
        break