import cv2
import numpy as np

apple = cv2.imread('data\\apple.jpg')
orange = cv2.imread('data\\orange.jpg')
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)


orange_copy = orange_copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)


apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], )


for i in range(5, 0, -1):
    gaussian_ 

print(apple.shape)
print(orange.shape)

cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('apple_orange', apple_orange)

cv2.waitKey(0)
cv2.destroyAllWindows()