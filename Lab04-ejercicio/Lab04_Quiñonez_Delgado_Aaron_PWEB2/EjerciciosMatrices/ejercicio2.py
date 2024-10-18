def esEscalar(m):
    d = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != 0:
                    print(f"Los elementos que no son parte de la diagonal deben ser 0. Posición:[{i}][{j}]: {m[i][j]}")
                    return False
            elif m[i][j] != d:
                print(f"La diagonal no tiene los mismos valores en la posición:[{i}][{j}]: {m[i][j]}")
                return False
    return True
def esUnitaria(m):
    return m[0][0] == 1 and esEscalar(m)
#Realizamos los mismos pasos que se pidió al usuario en el ejercicio 1
matrizN = int(input("Bienvenido usuario\nIngrese el numero N para la matriz de NxN: "))
array = [[0 for fila in range(matrizN)] for columna in range(matrizN)]
print("Su matriz es:")
for cont in array:
    print(cont)
#Pediremos que ingrese los valores de cada posición de la matriz mientras esta va actualizándose
for i in range(len(array)):
    for j in range(len(array)):
        pos = int(input(f"\nIngrese el valor para {i}x{j}: "))
        array[i][j] = pos
        #Imprimimos la matriz
        print("Su matriz es:")
        for cont in array:
            print(cont)
#Comprobación si la matriz es unitaria
if esUnitaria(array):
    print("Su matriz es unitaria")
else:
    print("Su matriz no es unitaria, la diagonal debe contener solo 1 como valores")