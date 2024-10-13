def ingresar_datos():
    tipoCliente = int(input("Ingrese el tipo de cliente (1 o 2): "))
    cantPasajes = int(input("Ingrese la cantidad de pasajes: "))
    genero = input("Ingrese el género del cliente (M/F): ").lower()
    tipoServicio = int(input("Ingrese el tipo de servicio (1-Económica, 2-Ejecutiva, 3-Primera clase): "))
    return tipoCliente, cantPasajes, genero, tipoServicio