# Importar las librerias de OpenCV, Numpy y Matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Lee una imagen
img = cv2.imread('/Users/isa/Pictures/Recursos/gatito.jpeg')
# Crea el kernel de 5x5 y resultante 25p (matríz)
kernel = np.ones((5, 5), np.float32) / 25
# Filtra la imagen utilizando el kernel anterior
dst = cv2.filter2D(img, -1, kernel)
# Crea el plot de la imagen original en sus componentes X y Y
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
# Crea el plot de la imagen promediada en sus componentes X y Y
plt.subplot(122), plt.imshow(dst), plt.title('Promediada')
plt.xticks([]), plt.yticks([])
# Muestra los resultados
plt.show()
cv2.waitKey(0)
'''
# Muestra los resultados
cv2.imshow('Original', img)
cv2.imshow('Promediada', dst)
cv2.waitKey(0)
'''

'''
El filtro pasabajas difumina la imagen
El filtro pasa altas detecta los bordes de la imagen
Si se tiene o altera una letra no aplica o funciona el código
L a funcion filtros2D(), permite aplicar el filtro que promedia un filtro pasabaja 
con un kernel
'''
