import numpy as np

def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0

def perceptron(X, W, b):
    Z = np.dot(X, W) + b
    salida = funcion_escalon(Z)
    return salida

print("\n===== COMPUERTA OR =====")
pesos_or = np.array([0.5, 0.5])   # los pesos se quedan igual
sesgo_or = -0.3                    # ESTE es el cambio clave

casos = [[1,1], [1,0], [0,1], [0,0]]

for caso in casos:
    entrada = np.array(caso)
    resultado = perceptron(entrada, pesos_or, sesgo_or)
    print(f"Entrada {caso} -> Salida: {resultado}")