import numpy as np
import cv2
# Determinar tamaño de la imagen
img = cv2.imread('gatito.jpg')
height, width = img.shape[:2]
print(height)
print(width)
# Linea recta
# cv2.line(image, Punto inicial, Punto Final, color en BGR, tamaño)
cv2.line(img,(0,0),(559,559),(255,255,255),4)
cv2.line(img,(0,559),(559,0),(255,255,255),4)
# Rectangulo 
# cv2.rectangle(img, Primera diagonal, Diagonal Final, color, tamaño)
cv2.rectangle(img, (15,15), (544,544), (219,237,34),4)
# Circulo
# cv2.circle(img, centro, radio, color, tamaño)
cv2.circle(img, (279,279), 50, (225,69,213),4)
# Figuras geometricas
# cv2.polylines(img, [puntos], true, color, tamaño)
pts = np.array([[6,5],[85,32],[129,320],[321,65],[54,63]], np.int32)
cv2.polylines(img, [pts], True, (170,150,236), 4)
# Texto
# cv2.putText(img, string, int_loclizacion, font, tamaño de la fuente, color, tamaño del contorno)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "GATITO XD", (50,50), font, 2, (170,150,236), 4)
cv2.imshow('Figuras', img)
cv2.waitKey(0)
cv2.destroyAllWindows()