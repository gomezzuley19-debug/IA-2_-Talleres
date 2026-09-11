import cv2
import numpy as np

imagen_color = cv2.imread('Taller 6/imagenes/herramienta.jpg')

if imagen_color is None:
    print("Error: no se pudo cargar la imagen. Verifica el nombre y la ruta.")
else:
    print("Imagen cargada correctamente. Forma:", imagen_color.shape)

    imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

    _, imagen_binaria = cv2.threshold(imagen_gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = np.ones((5, 5), np.uint8)
    imagen_limpia = cv2.morphologyEx(imagen_binaria, cv2.MORPH_OPEN, kernel)

    contornos, jerarquia = cv2.findContours(imagen_limpia, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    umbral_area = 3000  # ajusta este número según el tamaño de tu imagen

    print(f"Se encontraron {len(contornos)} objetos en la imagen.\n")

    contador = 1
    for cnt in contornos:
        area = cv2.contourArea(cnt)

        if area > 500:
            print(f"Objeto {contador}: área = {area} píxeles")

            x, y, w, h = cv2.boundingRect(cnt)

            if area > umbral_area:
                color = (255, 0, 0)  # Azul = objeto grande
                etiqueta = "grande"
            else:
                color = (0, 0, 255)  # Rojo = objeto pequeño
                etiqueta = "pequeño"

            cv2.rectangle(imagen_color, (x, y), (x + w, y + h), color, 2)

            cv2.putText(imagen_color, etiqueta, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            contador += 1

    cv2.imwrite('Taller 6/resultado_clasificacion.png', imagen_color)
    print("\nProceso completado. Revisa el archivo: resultado_clasificacion.png")