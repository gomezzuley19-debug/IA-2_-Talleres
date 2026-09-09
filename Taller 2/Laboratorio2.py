import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread('Taller 2/Imagenes/mar.jpg')

canal_azul = imagen[:, :, 0]
canal_verde = imagen[:, :, 1]
canal_rojo = imagen[:, :, 2]

hist_azul = cv2.calcHist([imagen], [0], None, [256], [0, 256])
hist_verde = cv2.calcHist([imagen], [1], None, [256], [0, 256])
hist_rojo = cv2.calcHist([imagen], [2], None, [256], [0, 256])

plt.plot(hist_azul, color='blue', label='Azul')
plt.plot(hist_verde, color='green', label='Verde')
plt.plot(hist_rojo, color='red', label='Rojo')

plt.title("Histograma por Canal de Color")
plt.xlabel("Valor del Píxel (0-255)")
plt.ylabel("Frecuencia (Cantidad de píxeles)")
plt.legend()
plt.savefig('histograma_resultado.png')
print("Gráfica guardada como histograma_resultado.png")