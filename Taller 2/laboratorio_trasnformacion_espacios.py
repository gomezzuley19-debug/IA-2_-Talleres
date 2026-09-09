import numpy as np

pixel = np.array([0, 255, 255])  # [Azul, Verde, Rojo]

print("Píxel BGR original:", pixel)

B = pixel[0]
G = pixel[1]
R = pixel[2]

gris = (0.114 * B) + (0.587 * G) + (0.299 * R)

print("Valor en escala de grises:", gris)