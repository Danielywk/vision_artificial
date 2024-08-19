import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/isa/Pictures/Recursos/gatitob.png', 0)

kernel = np.ones((7, 7), np.uint8)
dilatacion = cv2.dilate(img, kernel, iterations=1)

newImg = cv2.resize(img, (0, 0), fx=1, fy=1)
# newerosion = cv2.resize(erosion, (0,0), fx=2, fy=2)
newdilatacion = cv2.resize(dilatacion, (0, 0), fx=1, fy=1)
cv2.imshow(' Image Original', newImg)
cv2.imshow(' Image dilatacion', newdilatacion)

cv2.waitKey(0)
