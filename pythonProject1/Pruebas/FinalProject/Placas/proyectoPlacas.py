import cv2
import numpy as np
import pytesseract
from PIL import Image

cap = cv2.VideoCapture(1)

Ctexto = ""

while True:
	ret, frame = cap.read()

	if ret == False:
		break

	cv2.rectangle(frame, (1050, 500), (1250, 1500), (0, 0, 0), cv2.FILLED)
	cv2.putText(frame, Ctexto[0:9], (200, 370), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

	al, an, c = frame.shape

	x1 = int(an / 3) 
	x2 = int(x1 * 2) 

	y1 = int(al / 3) 
	y2 = int(y1 * 2) 
	cv2.rectangle(frame, (x1 + -180, y1 + 300), (1240, 460), (0, 0, 0), cv2.FILLED)
	cv2.putText(frame, 'Detectar Placa', (x1 + -100, y1 + 280), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 2)

	cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

	recorte = frame[y1:y2, x1:x2]

	mB = np.matrix(recorte[:, :, 0])
	mG = np.matrix(recorte[:, :, 1])
	mR = np.matrix(recorte[:, :, 2])

	Color = cv2.absdiff(mB, mG)

	_, umbral = cv2.threshold(Color, 40,255, cv2.THRESH_BINARY)

	contornos, _ = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
	contornos = sorted(contornos, key=lambda x: cv2.contourArea(x), reverse=True)

	for contorno in contornos:
		area = cv2.contourArea(contorno)
		if area > 500 and area < 7000:
			x, y, ancho, alto = cv2.boundingRect(contorno)

			xpi = x + x1  
			ypi = y + y1 

			xpf = x + ancho + x1  
			ypf = y + alto + y1  

			cv2.rectangle(frame, (xpi, ypi), (xpf, ypf), (255, 255, 0), 2)

			placa = frame[ypi:ypf, xpi:xpf]
			alp, anp, cp = placa.shape

			Mva = np.zeros((alp, anp))

			mBp = np.matrix(placa[:, :, 0])
			mGp = np.matrix(placa[:, :, 1])
			mRp = np.matrix(placa[:, :, 2])

			for col in range(0,alp):
				for fil in range(0,anp):
				     Max = max(mRp[col,fil] ,mGp[col,fil] ,mBp[col,fil])
				     Mva[col,fil] = 255 - Max

			_, bin = cv2.threshold(Mva, 150, 255, cv2.THRESH_BINARY)

			bin = bin.reshape(alp, anp)
			bin = Image.fromarray(bin)
			bin = bin.convert("L")
            
			if alp >= 32 and anp >= 86:

				pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

				config = "--psm 1"
				texto = pytesseract.image_to_string(bin, config=config)


				if len(texto) >= 7:

					Ctexto = texto


			break


	cv2.imshow("Detectar Placas", frame)
	t = cv2.waitKey(1)

	if t == 27:
	   break

cap.release()
cv2.destroyAllWindows()