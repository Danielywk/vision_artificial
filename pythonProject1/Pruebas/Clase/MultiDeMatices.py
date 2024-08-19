import cv2

img1 = cv2.imread('/Users/isa/Pictures/Recursos/J.jpeg')
img2 = cv2.imread('/Users/isa/Pictures/Recursos/J.png')

# Imagen por escalar
imgMultiply = cv2.multiply(img1, 9.2)
# imgMultiply = cv2.multiply(img1, (1.5, 1.5, 1.5, 1.5))
# Imagen por imagen
# imgMultiply = cv2.multiply(img1, img2)

print('img1[0,0] = ', img1[0, 0])
print('resAW[0,0] = ', imgMultiply[0, 0])

cv2.imshow('resAW', imgMultiply)
cv2.waitKey(0)
cv2.destroyAllWindows()
