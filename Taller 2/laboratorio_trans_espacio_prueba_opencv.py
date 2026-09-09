import cv2

imagen = cv2.imread('Taller 2/paisaje.jpg')
img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

cv2.imwrite('imagen_gris.jpg', img_gris)
print("Conversión completada. Forma de la imagen en grises:", img_gris.shape)