import numpy as np
import cv2
 
# Cargamos la imagen del disco duro
# Dependiendo como es que quieras mostrar la imagen es el indicador que se pone
# 1 imagen Color, 0 escala de grises, -1 sin modificacion 
# La imagen debe de estar en la carpeta del archivo
imagen = cv2.imread("./gatito.jpg",0)
# Esta parte se usa para mostrar una imagen
# El string entre las comillas es como se mostrara la imagen
cv2.imshow("prueba", imagen)
# Este comando crea una nueva imagen con las caracteristicas con las que se muestra
cv2.imwrite("./gatogris.jpg",imagen)
# Esta funcion espera los milisegundos definidos, a que suceda un evento en el teclado
cv2.waitKey(0)
# Destruye todas ventanas que hemos creado
cv2.destryAllWindows()