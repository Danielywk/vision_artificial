# Obtener las distancias
# Euclidina, City-black, Chessboard
# Matríz completa y cada distancia

# Cambiar el tamaño de una imagen, método resize()

import cv2

img = cv2.imread("/Users/isa/Pictures/Recursos/gatito.jpeg")
newImg = cv2.resize(img, (0, 0), fx=0.6, fy=0.6)
cv2.imshow('Resized Image', newImg)
cv2.waitKey(0)
