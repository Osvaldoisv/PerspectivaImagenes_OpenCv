import cv2
import numpy as np

imagen = cv2.imread('gato.jpeg')

cv2.circle(imagen, (84,69), 7, (255,0,0), 2)
cv2.circle(imagen, (513,77), 7, (0,255,0), 2)
cv2.circle(imagen, (113,358), 7, (0,0,255), 2)
cv2.circle(imagen, (542,366), 7, (255,255,0), 2)

cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()