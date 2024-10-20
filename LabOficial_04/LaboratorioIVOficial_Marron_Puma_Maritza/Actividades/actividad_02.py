from actividad_01 import esEscalar

def esUnitaria(m):
    if m[0][0] != 1 or not esEscalar(m):
        return False
    
    n = len(m)
    identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    trans_conjugada = [[m[j][i] for j in range(n)] for i in range(n)]
    producto = [[sum(m[i][k] * trans_conjugada[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    
    return producto == identidad

matriz = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

resultado = esUnitaria(matriz)
if resultado:
    print("La matriz que proporcionaste es unitaria :)")
else:
    print("La matriz que ingresaste no es unitaria ")
