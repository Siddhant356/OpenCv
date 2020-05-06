# -*- coding: utf-8 -*-
"""
Created on Thu May  7 00:00:43 2020

@author: Siddi
"""
import cv2

#read image
img = cv2.imread('data/lena.jpg', 1)        

print(img)

#show image
cv2.imshow('image', img)
k = cv2.waitKey(0) 

#press escape key to exit and s for saving image
if k== 27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('lena_copy.png',img) 
    cv2.destroyAllWindows()
