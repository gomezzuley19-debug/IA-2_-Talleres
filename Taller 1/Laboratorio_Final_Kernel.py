import numpy as np
I = np.array([
    [100, 100, 100],
    [100, 200, 100],
    [100, 100, 100]
])

K = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

print("Sección de Imagen (I):")
print(I)

print("\nKernel (K):")
print(K)

producto_hadamard = I * K

print("\nProducto Hadamard (I * K):")
print(producto_hadamard)

pixel_central = np.sum(producto_hadamard)

print("\nValor del píxel central calculado:", pixel_central)