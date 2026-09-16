import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X_entrenamiento = np.array([
    [20, 30, 0],   
    [40, 50, 2],   
    [35, 45, 1],   
    [22, 28, 0],   
    [45, 60, 3],   
    [30, 40, 1],   
    [50, 70, 2],   
    [25, 32, 0],   
    [38, 48, 2],   
    [28, 35, 0],   
])

Y_entrenamiento = np.array([0, 1, 1, 0, 1, 1, 1, 0, 1, 0])

nuevo_cliente = np.array([[30, 40, 1]])

modelo_knn_k1 = KNeighborsClassifier(n_neighbors=1)
modelo_knn_k1.fit(X_entrenamiento, Y_entrenamiento)
prediccion_k1 = modelo_knn_k1.predict(nuevo_cliente)
print("Predicción con K=1:", prediccion_k1[0])

modelo_knn_k5 = KNeighborsClassifier(n_neighbors=5)
modelo_knn_k5.fit(X_entrenamiento, Y_entrenamiento)
prediccion_k5 = modelo_knn_k5.predict(nuevo_cliente)
print("Predicción con K=5:", prediccion_k5[0])