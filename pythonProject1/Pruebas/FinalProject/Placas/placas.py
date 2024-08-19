# Se importa la libreria
import cv2
# Reconocimiento optico de caracteres
import pytesseract
# Uso de matrices
import numpy as numpy
# Nueva ventana
from tkinter import *

# Array vacio para colocar solamente la imagen de la placa detectada
placa = []
# image = cv2.imread('auto04.jpg')
image = cv2.imread('auto2.jpg')
# image = cv2.imread('auto03.jpg')
# Escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Atenuando el ruido se usa
gray = cv2.blur(gray, (3, 3))
# Deteccion de bordes
canny = cv2.Canny(gray, 150, 200)
# Se mejora la imagen binaria. Emgrosar las areas blancas
# canny = cv2.dilate(canny,None,iterations=1)

# Versiones anteriores. Encontrar los contornos binarios de canny
# ,cnts, = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts, _ = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# Dibujar los contonros encontrados
# cv2.drawContours(image,cnts,-1,(0,255,0),2)

# Encontrar la forma rectangular de la placa
for c in cnts:
    # Determinar el area de un contorno
    area = cv2.contourArea(c)
    # Area minima y maxima
    # Detectar un rectangulo en un rectangulo f
    x, y, w, h = cv2.boundingRect(c)
    # Parametro necesario para determinar los vertices del contorno
    epsilon = 0.07 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if len(approx) == 4 and area > 1400 and area < 1450:
        print('area', area)
        cv2.drawContours(image, [c], 0, (0, 255, 0), 2)
        # Conocer las dimensiones de las placas
        aspect_ratio = float(w) / h
        if aspect_ratio > 2.4:
            placa = gray[y:y + h, x:x + w]
            # Reconocimiento de caracteres
            text = pytesseract.image_to_string(placa, config='--psm 11')
            print('PLACA: ', text)
            # Se muestra la imagen s
            cv2.imshow('placa', placa)
            # Se mueve al centro
            cv2.moveWindow('placa', 750, 80)
            # Colocar el texto de las placas
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(image, text, (x - 20, y - 10), 1, 2.2, (0, 255, 0), 3)
            # Datos del auto
            cv2.imshow('Imagen', image)
            root = Tk()
            # Insercion de datos
            Label(root, text="¡Datos del auto!").pack()
            Label(root, text="¡Conductor: Teresa Sucedo Moreno!").pack()
            Label(root, text="¡Estado de mexico!").pack()
            Label(root, text="¡Codigo de motor:458712390!").pack()
            Label(root, text="¡Modelo:1256POS56 !").pack()
            root.mainloop()
    if len(approx) == 4 and area > 3000 and area < 3511.5:
        print('area', area)
        cv2.drawContours(image, [c], 0, (0, 255, 0), 2)
        # Conocer las dimensiones de las placas
        aspect_ratio = float(w) / h
        if aspect_ratio > 2.4:
            placa = gray[y:y + h, x:x + w]
            # Reconocimiento de caracteres
            text = pytesseract.image_to_string(placa, config='--psm 11')
            print('PLACA: ', text)
            # Se muestra la imagen s
            cv2.imshow('placa', placa)
            # Se mueve al centro
            cv2.moveWindow('placa', 750, 80)
            # Colocar el texto de las placas
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(image, text, (x - 20, y - 10), 1, 2.2, (0, 255, 0), 3)
            # Datos del auto
            cv2.imshow('Imagen', image)
            root = Tk()
            # Insercion de datos
            Label(root, text="¡Datos del auto!").pack()
            Label(root, text="¡Conductor: Jose Ariel Muñiz Cedillo!").pack()
            Label(root, text="¡Estado de San Luis Potosi!").pack()
            Label(root, text="¡Codigo de motor:754126983!").pack()
            Label(root, text="¡Modelo:15968FRD86 !").pack()
            root.mainloop()

    if len(approx) == 4 and area > 1700 and area < 17355:
        print('area', area)
        cv2.drawContours(image, [c], 0, (0, 255, 0), 2)
        # Conocer las dimensiones de las placas
        aspect_ratio = float(w) / h
        if aspect_ratio > 2.4:
            placa = gray[y:y + h, x:x + w]
            # Reconocimiento de caracteres
            text = pytesseract.image_to_string(placa, config='--psm 11')
            print('PLACA: ', text)
            # Se muestra la imagen s
            cv2.imshow('placa', placa)
            # Se mueve al centro
            cv2.moveWindow('placa', 750, 80)
            # Colocar el texto de las placas
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(image, text, (x - 20, y - 10), 1, 2.2, (0, 255, 0), 3)
            # Datos del auto
            cv2.imshow('Imagen', image)
            root = Tk()
            # Insercion de datos
            Label(root, text="¡Datos del auto!").pack()
            Label(root, text="¡Conductor:Paola Lizbeth Sanchez Monroy !").pack()
            Label(root, text="¡Estado de Mexico!").pack()
            Label(root, text="¡Codigo de motor:854163298!").pack()
            Label(root, text="¡Modelo:89674QRS85 !").pack()
            root.mainloop()

        # Se ve la imagen  original

# Se ve la imagen  con canny con deteccion de bordes
cv2.imshow('Canny',canny)
# Se mueve la imagen al centro
# cv2.imshow('PLACA', image)
cv2.moveWindow('PLACA', 780, 10)
# Se espera una tecla para cerrar
cv2.waitKey(0)
