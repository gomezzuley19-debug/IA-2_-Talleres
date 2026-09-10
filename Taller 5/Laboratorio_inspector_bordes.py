import cv2
import numpy as np

imagen = cv2.imread('Taller 5/imagenes/edificio.jpg', cv2.IMREAD_GRAYSCALE)

if imagen is None:
    print("Error: no se pudo cargar la imagen. Verifica el nombre y la ruta")
else:
    print("Imagen cargada correctamente. Forma:", imagen.shape)

    sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobel_x_visible = cv2.convertScaleAbs(sobel_x)

    sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    sobel_y_visible = cv2.convertScaleAbs(sobel_y)

    bordes_canny = cv2.Canny(imagen, 50, 150)

    cv2.imwrite('Taller 5/1_sobel_x.png', sobel_x_visible)
    cv2.imwrite('Taller 5/2_sobel_y.png', sobel_y_visible)
    cv2.imwrite('Taller 5/3_canny.png', bordes_canny)

    print("Listo. Revisa los 3 archivos en la carpeta Taller 5:")
    print("1_sobel_x.png -> bordes verticales")
    print("2_sobel_y.png -> bordes horizontales")
    print("3_canny.png -> bordes combinados")

    canny_bajo = cv2.Canny(imagen, 10, 50)
    canny_alto = cv2.Canny(imagen, 200, 250)

    cv2.imwrite('Taller 5/4_canny_umbral_bajo.png', canny_bajo)
    cv2.imwrite('Taller 5/5_canny_umbral_alto.png', canny_alto)

    print("También se generaron 2 pruebas extra:")
    print("4_canny_umbral_bajo.png -> umbrales 10 y 50")
    print("5_canny_umbral_alto.png -> umbrales 200 y 250")