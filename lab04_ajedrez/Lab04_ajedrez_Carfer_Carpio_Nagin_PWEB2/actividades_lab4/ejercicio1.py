def esEscalar(m):
    d = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != 0:
                    print(f"Elementos que no sean parte de la diagonal deben ser 0")
                    return False
            elif m[i][j] != d:
                print(f"Los elementos de la diagonal deben ser iguales")
                return False
    return True
#Pedimos un numero para el tamaño de la matriz
matrizN = int(input("Ingrese el numero N para la matriz de NxN: "))
array = [[0 for fila in range(matrizN)] for columna in range(matrizN)]
print("Su matriz es")
for cont in array:
    print(cont)
#Pedimos los valores dentro de la matriz
for i in range(len(array)):
    for j in range(len(array)):
        pos = int(input(f"\nIngrese valores para {i}x{j} "))
        array[i][j] = pos
        #Imprimimos la matriz
        print("Su matriz es:")
        for cont in array:
            print(cont)
# corroboramos si es o no escalar
if esEscalar(array):
    print("Su matriz es escalar")
else:
    print("La matriz ingresada no es escalar")
