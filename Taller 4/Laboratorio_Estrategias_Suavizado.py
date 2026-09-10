import cv2

imagen = cv2.imread('Taller 4/imagenes/charli.png')

if imagen is None:
    print("Error: no se pudo cargar la imagen ruidosa.")
else:
    # Filtro de Media (7x7)
    blur_media = cv2.blur(imagen, (7, 7))
    cv2.imwrite('Taller 4/1_filtro_media.png', blur_media)

    # Filtro Gaussiano (7x7)
    blur_gauss = cv2.GaussianBlur(imagen, (7, 7), 0)
    cv2.imwrite('Taller 4/2_filtro_gaussiano.png', blur_gauss)

    # Filtro de Mediana (7)
    blur_mediana = cv2.medianBlur(imagen, 7)
    cv2.imwrite('Taller 4/3_filtro_mediana.png', blur_mediana)

    print("Listo. Revisa los 3 archivos en la carpeta Taller 4:")
    print("1_filtro_media.png")
    print("2_filtro_gaussiano.png")
    print("3_filtro_mediana.png")