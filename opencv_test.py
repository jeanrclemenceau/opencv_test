# -*- coding: utf-8 -*-
"""
Practicing importing images and videos using OpenCV
Created on Tue Jun 06 00:59:13 2017

@author: clemenj
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

############################################
#Import Video
#cap= cv2.VideoCapture(0) #0=first camera in system
#fourcc = cv2.VideoWriter_fourcc(*'XVID') #establish codec
#out = cv2.VideoWriter('output.avi',fourcc,20,(640,480)) #open file as write

# (python2 version)
#fourcc = cv2.cv.CV_FOURCC(*'XVID') #establish codec
#out = cv2.VideoWriter('output.avi',-1,20,(640,480)) #open file as write
#
#while True:
#    ret,frame = cap.read() #ret=bool(is there a feed?)
#    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #cvtColor: convert color
#    out.write(gray) #save frame
#    cv2.imshow('frame',frame)
#    cv2.imshow('gray',gray)
#    
#    if cv2.waitKey(1) & 0xFF==ord('q'):
#        break
#cap.release() #free camera
#out.release() #free video file
#cv2.destroyAllWindows()
###########################################

#Import Image
#IMREAD_COLOR : 1
#IMREAD_COLOR: 0
#IMREAD_UNCHANGED = -1
img = cv2.imread('coins.jpg',cv2.IMREAD_GRAYSCALE)

#Show image using CV
cv2.imshow('coinimg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plot with matplotlib
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,100],[80,100],'c',linewidth=5)
#plt.show()

#save image
cv2.imwrite('coins_gray.png',img)
