import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/isa/Pictures/Recursos/gatitob.png', 0)

kernel = np.ones((9, 9), np.uint8)
# erosion = cv2.erode(img, kernel, iterations = 1)

sombrero = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
newImg = cv2.resize(img, (0, 0), fx=1, fy=1)
# newerosion = cv2.resize(erosion, (0,0), fx=2, fy=2)
newcierre = cv2.resize(sombrero, (0, 0), fx=1, fy=1)

cv2.imshow(' Image Original', newImg)
cv2.imshow(' Image sombrero de copa', newcierre)

cv2.waitKey(0)
