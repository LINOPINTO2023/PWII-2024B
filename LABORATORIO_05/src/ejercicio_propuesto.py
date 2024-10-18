# Ejercicio 1: Determinar si una matriz es escalar
def esEscalar(m):
    d = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != 0:
                    return False
            elif m[i][j] != d:
                return False
    return True

# Ejercicio 2: Determinar si una matriz es unitaria
def esUnitaria(m):
    return m[0][0] == 1 and esEscalar(m)

if __name__ == "__main__":
    matriz1 = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]

    matriz2 = [[2, 0, 0],
                [0, 2, 0],
                [0, 0, 2]]

    matriz3 = [[1, 0, 0],
                [0, 2, 0],
                [0, 0, 1]]

    print("Matriz 1 es unitaria:", esUnitaria(matriz1)) #true
    print("Matriz 2 es escalar:", esEscalar(matriz2)) #true
    print("Matriz 3 es escalar:", esEscalar(matriz3)) #false