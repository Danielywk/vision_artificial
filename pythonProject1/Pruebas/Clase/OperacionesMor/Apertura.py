import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/isa/Pictures/Recursos/gatitob.png', 0)

kernel = np.ones((7,7), np.uint8)
# dilatacion = cv2.dilate(img, kernel, iterations = 1)
apertura = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

newImg = cv2.resize(img, (0,0), fx=1, fy=1)
# newerosion = cv2.resize(erosion, (0,0), fx=2, fy=2)
newapertura = cv2.resize(apertura, (0,0), fx=1, fy=1)
cv2.imshow(' Image Original', newImg)
cv2.imshow(' Image apertura', newapertura)

cv2.waitKey(0)