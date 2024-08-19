import numpy as np
import cv2

img = cv2.imread('/Users/isa/Pictures/Recursos/mon.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# Eliminación de ruido
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# Encuentra el área de primer
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
# Encuentra la región desconocida (bordes)
sure_fg = np.uint8(sure_fg)
unknow = cv2.subtract(sure_bg, sure_fg)
ret, makers = cv2.connectedComponents(sure_fg)

makers = makers + 1

makers[unknow == 255] = 0
makers = cv2.watershed(img, makers)
#cv2.imshow('makers', makers)
img[makers == -1] = [255, 0, 0]
cv2.imshow('resultado', img)
# Imprime las imágenes
#cv2.imshow('ruido', opening)
#cv2.imshow('original', gray)
#cv2.imshow('fondo', sure_bg)
#cv2.imshow('área del fondo', sure_fg)
#cv2.imshow('bordes', unknow)

cv2.waitKey(0)
# Encuentra el área del fondo
