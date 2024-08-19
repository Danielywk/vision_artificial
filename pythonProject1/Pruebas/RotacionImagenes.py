import cv2

# Lee una imagen
image1 = cv2.imread(r'/Users/isa/Pictures/Recursos/J.png')
width = 821
height = 1094
# Parámetros de ángulo y escala (ajuste de imagen en pantalla)
# Para obtener la matriz de rotación, se usa el método getRotationMatrix2D() de cv2
rotationMatrix = cv2.getRotationMatrix2D((width / 2, height / 2), 360, .9)
# Para lograr la rotación de la imagen, usamos la matriz de rotación y el método de cv2 llamado
# warpAffine que toma como argumentos la imagen original, la matriz de rotación de la imagen
# Y el ancho y alto de la imagen
# La imagen rotada se almacena en la matriz rotatedImage
rotatedImage = cv2.warpAffine(image1, rotationMatrix, (width, height))
# Muestra la imagen rotada
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(0)
