import cv2

img1 = cv2.imread('/Users/isa/Pictures/Recursos/J.jpeg')
img2 = cv2.imread('/Users/isa/Pictures/Recursos/gatito.jpeg')

resAW = cv2.addWeighted(img1, 0.2, img2, 0.8, 0)

# resA= cv2.add(img1, img2)
print('img1[0,0] = ', img1[0, 0])
print('img2[0,0] = ', img2[0, 0])
print('resA[0,0] = ', resAW[0, 0])

cv2.imshow('resA', resAW)
cv2.waitKey(0)
cv2.destroyAllWindows()
