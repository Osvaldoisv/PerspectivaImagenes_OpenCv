import cv2
import numpy as np

imagen = cv2.imread('perro.jpeg')
cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()