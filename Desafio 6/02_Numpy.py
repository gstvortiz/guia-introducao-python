import numpy as np


#1- Crie uma matriz 1D com números de 0 a 9
matriz = np.arange(9)

#2- Crie uma matriz booleana numpy 3×3 com ‘True’
np.full(fill_value = True, shape = (3, 3))

#3- Extraia todos os números ímpares de ‘arr’
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
impares = arr[(arr % 2).astype(bool)]

#4- Substitua todos os números ímpares arr por -1
arr = np.where(arr % 2 != 0, arr, -1)

#5- Substitua todos os números ímpares em arr com -1 sem alterar arr
arr = np.arange(10)
print(np.where(arr % 2 != 0, arr, -1))

#6- Converta uma matriz 1D para uma matriz 2D com 2 linhas:
arr = np.arange(10)
arr = arr.reshape(2, 5)

#7- Empilhe matrizes verticalmente:
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
c = np.concatenate([a, b])

#8- Empilhe as matrizes horizontalmente:
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
c = np.concatenate([a, b], axis = 1)