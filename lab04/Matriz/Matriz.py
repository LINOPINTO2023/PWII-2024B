def esEscalar(m):
    # Verificar que m sea una matriz válida y cuadrada
    if not isinstance(m, list) or not all(isinstance(row, list) for row in m):
        return "La entrada no es una matriz válida"
    n = len(m)
    if any(len(row) != n for row in m):
        return "La matriz no es cuadrada"
    
    # Obtener el valor de la diagonal
    d = m[0][0]
    
    # Comprobar si es una matriz escalar
    for i in range(n):
        for j in range(n):
            if i != j and m[i][j] != 0:
                return False
            elif i == j and m[i][j] != d:
                return False
    
    return True

def esUnitaria(m):
    # Verificar si es escalar y si el valor en la diagonal es 1
    return esEscalar(m) and m[0][0] == 1

# Ejemplo de uso
matriz1 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

matriz2 = [
    [3, 0, 0],
    [0, 3, 0],
    [0, 0, 3]
]

matriz3 = [
    [1, 2, 3],
    [0, 1, 0],
    [0, 0, 1]
]

print(esUnitaria(matriz1))
print(esUnitaria(matriz2))
print(esUnitaria(matriz3))
