import numpy as np
from sklearn.svm import SVC

print("===== PARTE 1: MODELO LINEAL ORIGINAL =====\n")

X = np.array([[2,2], [3,3], [4,2], [6,6], [7,8], [8,7]])
Y = np.array([0, 0, 0, 1, 1, 1])

modelo_svm = SVC(kernel='linear')
modelo_svm.fit(X, Y)

print("Los Vectores de Soporte son:")
print(modelo_svm.support_vectors_)

nuevo_punto = np.array([[5, 4]])
pred = modelo_svm.predict(nuevo_punto)
print("El punto [5,4] pertenece a la clase:", pred[0])


print("\n===== PARTE 2: AGREGANDO EL PUNTO 'PROBLEMÁTICO' [5,5] =====\n")

X_nuevo = np.array([[2,2], [3,3], [4,2], [6,6], [7,8], [8,7], [5,5]])
Y_nuevo = np.array([0, 0, 0, 1, 1, 1, 0])

modelo_lineal = SVC(kernel='linear')
modelo_lineal.fit(X_nuevo, Y_nuevo)

print("--- Modelo LINEAL con el nuevo punto ---")
print("Vectores de Soporte:")
print(modelo_lineal.support_vectors_)
print("Precisión del modelo lineal:", modelo_lineal.score(X_nuevo, Y_nuevo))
print("Predicción para [5,5]:", modelo_lineal.predict([[5,5]])[0], "(debería ser 0)")


print("\n===== PARTE 3: CAMBIANDO A KERNEL RBF =====\n")

modelo_rbf = SVC(kernel='rbf')
modelo_rbf.fit(X_nuevo, Y_nuevo)

print("--- Modelo RBF con el nuevo punto ---")
print("Vectores de Soporte:")
print(modelo_rbf.support_vectors_)
print("Precisión del modelo RBF:", modelo_rbf.score(X_nuevo, Y_nuevo))
print("Predicción para [5,5]:", modelo_rbf.predict([[5,5]])[0], "(debería ser 0)")