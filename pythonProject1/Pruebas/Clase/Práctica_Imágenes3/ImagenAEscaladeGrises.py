import cv2
img = cv2.imread(r'/Users/isa/Pictures/Recursos/gatito.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600, 336)
cv2.imshow('image', gray_img)
cv2.waitKey(0)