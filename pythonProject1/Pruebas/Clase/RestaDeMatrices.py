import cv2

img1 = cv2.imread('/Users/isa/Pictures/Recursos/J.jpeg')
img2 = cv2.imread('/Users/isa/Pictures/Recursos/gatito.jpeg')

# resultado= cv2.absdiff(img1, img2)

resultado = cv2.subtract(img1, img2)
print('img1[0,0] = ', img1[0, 0])
print('img2[0,0] = ', img2[0, 0])
print('resultado[0,0] = ', resultado[0, 0])

cv2.imshow('resulstado', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
