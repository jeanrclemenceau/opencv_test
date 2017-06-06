# -*- coding: utf-8 -*-
"""
Practicing writing on images using OpenCV
Created on Tue Jun 06 01:59:13 2017

@author: clemenj
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('coins.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150), (255,0,255),15) #image,startpt, endpt, color (bgr), line width
cv2.rectangle(img, (15,25),(200,150), (255,255,0),5)
cv2.circle(img, (600,63), 55, (0,0,0),-1) #image,center,radius,color, -1=fill in shape

#create polyons
points = np.array([[310,305],[320,330],[370,320],[350,310]], np.int32)
points = points.reshape((-1,1,2)) #reshape the array to 1 by 2
cv2.polylines(img, [points],True,(255,0,0),3) #image,numpy array of points, boolean: last point connect to first, color, line weight

#write text
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'Hello World!',(400,500),font,1,(255,255,255),2) #image,text,location,font size,color, thickness,anti-aliasing

#show image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('coinsDrawn.png',img)
