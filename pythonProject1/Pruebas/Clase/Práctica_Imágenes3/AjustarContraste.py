import cv2
import numpy as np

apha = 0.3
beta = 80
img_path = "/Users/isa/Pictures/leon.bmp"
img = cv2.imread(img_path)
img2 = cv2.imread(img_path)


# Ajusta contraste
def updateAlpha(x):
    global alpha, img, img2
    alpha = cv2.getTrackbarPos('Contraste', 'image')
    alpha = alpha * 0.01
    img = np.uint8(np.clip((alpha * img2 + beta), 0, 255))


# Ajusta brillo
def updateBeta(x):
    global beta, img, img2
    beta = cv2.getTrackbarPos('Brillo', 'image')
    img = np.uint8(np.clip((alpha * img2 + beta), 0, 255))


# Crear ventana
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 300, 400)
cv2.createTrackbar('Contraste', 'image', 0, 300, updateAlpha)
cv2.createTrackbar('Brillo', 'image', 0, 255, updateBeta)
cv2.setTrackbarPos('Contraste', 'image', 100)
cv2.setTrackbarPos('Brillo', 'image', 10)
while (True):
    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
