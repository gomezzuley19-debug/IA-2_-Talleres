import numpy as np
matriz_original = np.random.randint(200, 255, (5, 5))

alpha = 0.5   
beta = -50  

matriz_nueva= (alpha * matriz_original) + beta

matriz_procesada =np.clip(matriz_nueva, 0, 255).astype(np.uint8)

matriz_original, matriz_procesada