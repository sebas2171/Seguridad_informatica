import numpy as np
# import math

def hill(opt, m, k, alfabeto, n):
    m = m.replace(' ', '')
    m = m.upper()
    letrasMensaje = list(m)
    j = 0
    matriz = np.zeros((2, int(len(letrasMensaje)/2)+1))
    for i in range(int(len(letrasMensaje)/2)+1):
        if(len(letrasMensaje)%2 == 0):
            matriz[0][i] = alfabeto.index(letrasMensaje[j])
            matriz[1][i] = alfabeto.index(letrasMensaje[j+1])
        else:  
            matriz[0][i] = alfabeto.index(letrasMensaje[j])
            matriz[1][i] = alfabeto.index('X')
        j = j+2

    return(matriz)

    

m = 'SUPER BOWL'
alpha = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
alfabeto = list(alpha)
matriz = hill(1, m, 1, alfabeto, 1)
print(matriz)
print(alfabeto.index('X'))