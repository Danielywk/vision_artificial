# Importando las librerias de OpenCV y numpy
import cv2
import numpy as np

# Lectura de la imagen
img = cv2.imread(r'/Users/isa/Pictures/Recursos/figuras.jpg')

# Redimensionando el tamaño
image = cv2.resize(img, (700, 600))

# Convitiendo la imagen a imagen HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definiendo el lower and upper bound HSV values
lower = np.array([110, 100, 100])
upper = np.array([130, 255, 255])

'''
lower = [h-10, 100, 100]
upper = [h+10, 255, 255]
'''

# Definiendo la máscara para detectar el color
mask = cv2.inRange(hsv, lower, upper)

# Muestra las imágenes
cv2.imshow("Image", image)
cv2.imshow("Mask", mask)

# Obtener un color
color = np.uint8([[[0, 0, 255]]])

# Convert color to wish color
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

# Print HSV Value for the color
print(hsv_color)

cv2.waitKey(0)
