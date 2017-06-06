# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 02:42:16 2017

@author: clemenj
"""
import cv2
import numpy as np

#import image
img = cv2.imread('coins.jpg',cv2.IMREAD_COLOR)

#address pixel
px = img[55,55]
print(px)
img[55,55] = [255,255,255]
print(px)

#Region of Image (ROI): Subimage
roi = img[100:150,100:150]
img[100:150,100:150] = [255,255,255]

coin1 = img[70:276,454:677] #206x223 ROI (Yaxis,Xaxis)
img[0:206,0:223] = coin1

#cv2.imwrite('onepenny.png',coin1)

########Image Arythmetic
img1=cv2.imread('coins.jpg')
img2=cv2.imread('coins_gray_rotated.png')
img3=cv2.imread('onepenny.png')

#add = img1 + img2 #Add both images using numpy (modulo addition, eg. 103 % 50 = 3)
#add=cv2.add(img1,img2) #Adds every corresponding pixel value (eg. 103 + 50 = 153)

#overlap differences (blend images)
weighted= cv2.addWeighted(img1,0.6,img2,0.4,0) #operand1,weight1,operand2,weigh2,gamma value(scalar added to each )

######Image Logic
rows,cols,channels = img2.shape #get image data
roi2 = img1[0:rows,0:cols] #create ROI size of img3

#Mask
img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY) #convert to grayscale
ret,mask = cv2.threshold(img2gray,200,255,cv2.THRESH_BINARY_INV) #Image used, threshold value (above=max,below=black), replace value(max),threshold type (binary, inverse colors)
mask_inv = cv2.bitwise_not(mask) #return black area of mask
#img1_bg = cv2.bitwise_and(roi2,roi2,mask=mask_inv)
#img3_fg = cv2.bitwise_and(img3,img3,mask=mask)

#dst = cv2.add(img1_bg, img3_fg)
#img1[0,rows,0:cols] = dst


#show image
#cv2.imshow('image',img)
#cv2.imshow('add',add)
#cv2.imshow('weight',weighted)
#cv2.imshow('mask',mask)
#cv2.imshow('res',img1)
#cv2.imshow('img2gray',img2gray)
#cv2.imshow('roi2',roi2)
#cv2.imshow('mask_inv',mask_inv)
#cv2.imshow('img1_bg',img1_bg)
#cv2.imshow('img3_fg',img3_fg)
#cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()