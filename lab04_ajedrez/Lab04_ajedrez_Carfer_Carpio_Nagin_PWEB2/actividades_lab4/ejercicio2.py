def esEscalar(m):
    d = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != 0:
                    print(f"Elementos que no sean parte de la diagonal deben ser 0")
                    return False
            elif m[i][j] != d:
                print(f"La diagonal no tiene los mismos valores")
                return False
    return True
def esUnitaria(m):
    return m[0][0] == 1 and esEscalar(m)
#Pedimos un numero para el tamaño de la matriz
matrizN = int(input("Ingrese el tamaño de la matriz NxN "))
array = [[0 for fila in range(matrizN)] for columna in range(matrizN)]
print("Su matriz es ")
for cont in array:
    print(cont)
#Pedimos los valores dentro de la matriz
for i in range(len(array)):
    for j in range(len(array)):
        pos = int(input(f"\nIngrese el valor para {i}x{j} "))
        array[i][j] = pos
        #Imprime la matriz
        print("Su matriz es:")
        for cont in array:
            print(cont)
#Corroboracion si es o no unitaria
if esUnitaria(array):
    print("Su matriz es unitaria")
else:
    print("Su matriz no es unitaria")
