def esEscalar(m):
    d = m[0][0]
    
    for i in range(len(m)):
        for j in range(len(m)):
            if (i != j and m[i][j] != 0):
                print(f"Elemento en posición ({i}, {j}) no es cero: {m[i][j]}")
                return False
            elif (i == j and m[i][j] != d):
                print(f"Elemento en posición ({i}, {j}) no es igual a {d}: {m[i][j]}")
                return False
    return True

def esUnitaria(m):
    if m[0][0] != 1:
        print(f"Elemento en posición (0, 0) no es uno: {m[0][0]}")
        return False

    if not esEscalar(m):
        return False

    return True

def ingresar_matriz():
    n = int(input("Ingrese el tamaño de la matriz NxN: "))
    
    m = []
    print("Ingrese los elementos de la matriz fila por fila (separados por espacios):")
    for i in range(n):
        fila = list(map(int, input(f"Fila {i + 1}: ").split()))
        if len(fila) != n:
            print(f"Error: La fila debe contener exactamente {n} elementos.")
            return None  # Retorna None para indicar que hay un error
        m.append(fila)

    return m

def menu():
    while True:
        print("\nElija una opción:")
        print("1. Verificar si la matriz es escalar")
        print("2. Verificar si la matriz es unitaria")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == '3':
            break
        
        matriz = ingresar_matriz()

        if matriz is None:  # Verificar si hubo un error en la entrada
            continue

        if opcion == '1':
            if esEscalar(matriz):
                print("La matriz es escalar.")
            else:
                print("La matriz no es escalar.")
        elif opcion == '2':
            if esUnitaria(matriz):
                print("La matriz es unitaria.")
            else:
                print("La matriz no es unitaria.")
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
