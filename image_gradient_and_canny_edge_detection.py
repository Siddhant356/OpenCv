import cv2
from matplotlib import pyplot as plt
import numpy as np


img = cv2.imread('data//messi5.jpg', cv2.IMREAD_GRAYSCALE)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombine = cv2.bitwise_or(sobelX, sobelY)
canny = cv2.Canny(img, 100, 200)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombine', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombine, canny]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    


plt.show()

