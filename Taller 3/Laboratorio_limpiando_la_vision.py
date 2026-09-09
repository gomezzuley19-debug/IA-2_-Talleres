import cv2
import numpy as np

imagen = cv2.imread('Taller 3/imagenes/contraste.jpg', cv2.IMREAD_GRAYSCALE)
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
else:
    print("Imagen cargada correctamente. Forma:", imagen.shape)

_, imagen_binaria = cv2.threshold(imagen, 90, 255, cv2.THRESH_BINARY)

cv2.imwrite('1_imagen_binaria.png', imagen_binaria)

kernel = np.ones((3, 3), np.uint8)

apertura = cv2.morphologyEx(imagen_binaria, cv2.MORPH_OPEN, kernel)
cv2.imwrite('2_apertura.png', apertura)

cierre = cv2.morphologyEx(imagen_binaria, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('3_cierre.png', cierre)

print("Proceso completado. Revisa los 3 archivos generados:")
print("1_imagen_binaria.png -> Original binarizada con ruido")
print("2_apertura.png -> Resultado de Apertura")
print("3_cierre.png -> Resultado de Cierre")