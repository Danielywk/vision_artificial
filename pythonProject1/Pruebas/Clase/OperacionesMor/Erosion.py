import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/isa/Pictures/Recursos/paisajeb.png', 0)

kernel = np.ones((7,7), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)

newImg = cv2.resize(img, (0,0), fx=2, fy=2)
newerosion = cv2.resize(erosion, (0,0), fx=2, fy=2)

cv2.imshow(' Image Original', newImg)
cv2.imshow(' Image erosión', newerosion)

cv2.waitKey(0)