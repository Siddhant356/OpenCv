import cv2
import numpy as np

img = cv2.imread('data//sudoku.png', 0)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
th1 = cv2.adaptiveThreshold(imgGrey,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# th2 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow('image', img)
cv2.imshow('th1', th1)
# cv2.imshow('th2', th2)

cv2.waitKey(0) 
cv2.destroyAllWindows()
