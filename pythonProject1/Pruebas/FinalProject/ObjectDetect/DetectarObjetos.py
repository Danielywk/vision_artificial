import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/Users/isa/Pictures/Recursos/image.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()

# Usaremos la detectMultiScale() función de openCV para reconocer
# signos grandes como pequeños

stop_data = cv2.CascadeClassifier('/Users/isa/Pictures/Recursos/stop_data.xml')
found = stop_data.detectMultiScale(img_gray, minSize=(20, 20))

amount_found = len(found)
if amount_found != 0:
    for (x, y, width, height) in found:
        cv2.rectangle(img_rgb, (x, y), (x + height, y + width), (0, 255, 0), 5)
        plt.subplot(1, 1, 1)
        plt.imshow(img_rgb)
        plt.show()