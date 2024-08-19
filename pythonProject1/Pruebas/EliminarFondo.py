# Importar modulos numpy y cv2

import cv2
import numpy as np

# Lee una imagen y la convierte a escala de grises
img = cv2.imread(r'/Users/isa/Pictures/Recursos/J.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# El método threshold define el estilo del umbral
_, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# Encuentra los contornos
img_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
# Ordena los contornos
img_contours = sorted(img_contours, key=cv2.contourArea)
for i in img_contours:
    if cv2.contourArea(i) > 100:
        break
# Encuentra los contornos para detectar los bordes del objeto principal
# y crear una máscara con np.zeros() para el fondo, para luego, combinar
# La máscara y la imagen usando el operador bitwise_and
mask = np.zeros(img.shape[:2], np.uint8)
# Dibujar los contornos
cv2.drawContours(mask, [i], -1, 255, -1)
# Aplica el operador bitwise_and
new_img = cv2.bitwise_and(img, img, mask=mask)
# Muestra la imagen original
cv2.imshow("Oriiginal_Image", img)
# Muestra la imagen resultante
cv2.imshow("Image with background removed", new_img)
cv2.waitKey(0)
