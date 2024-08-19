# Importar las librerias de OpenCV, Numpy y Matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Lee una imagen
img = cv2.imread('/Users/isa/Pictures/Recursos/gatito.jpeg')
# Crea el kernel de 5x5 y resultante 25p (matríz)
# kernel = np.ones((5, 5), np.float32) / 25
# Aplica el filtro a un kernel de dimensión 5x5
# blur = cv2.blur(img,(5,5))
# Aplicación del filtro de caja a una imagen de kernel 5x5
boxFilter = cv2.boxFilter(img, -1, (5,5))
'''
# Aplica el filtro a un kernel de dimensión 5x5 a un núcleo Gaussiano
# Gblur = cv2.GaussianBlur(img,(5,5),0)
# Aplica el filtro de la media a una imagen de dimensiones 5x5
# median = cv2.medianBlur(img, 5)
# Crea el plot de la imagen original en sus componentes X y Y
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
# Crea el plot de la imagen promediada en sus componentes X y Y
plt.subplot(122), plt.imshow(boxFilter), plt.title('BoxFilter')
plt.xticks([]), plt.yticks([])
# Muestra los resultados
plt.show()
'''

# Muestra los resultados
cv2.imshow('Original', img)
cv2.imshow('Promediada', boxFilter)
cv2.waitKey(0)

'''
El filtro pasabajas difumina la imagen
El filtro pasa altas detecta los bordes de la imagen
Si se tiene o altera una letra no aplica o funciona el código
L a funcion filtros2D(), permite aplicar el filtro que promedia un filtro pasabaja 
con un kernel
'''
