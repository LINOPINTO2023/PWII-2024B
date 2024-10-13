def ingresar_datos():
    tipoCliente = int(input("Ingrese el tipo de cliente (1 o 2): "))
    cantPasajes = int(input("Ingrese la cantidad de pasajes: "))
    genero = input("Ingrese el género del cliente (M/F): ").lower()
    tipoServicio = int(input("Ingrese el tipo de servicio (1-Económica, 2-Ejecutiva, 3-Primera clase): "))
    return tipoCliente, cantPasajes, genero, tipoServicio
    def calcular_precio(cantPasajes, tipoServicio):
    # Tipo de servicio
    if tipoServicio == 1:
        precio = 70
    elif tipoServicio == 2:
        precio = 140
    elif tipoServicio == 3:
        precio = 280
    else:
        print("Tipo de servicio inválido.")
        return 0, 0, 0
    
    # Descuento por cantidad de pasajes
    if cantPasajes == 1:
        descuento = 0
    elif 2 <= cantPasajes <= 5:
        descuento = 0.05
    elif 6 <= cantPasajes <= 10:
        descuento = 0.12
    else:
        descuento = 0.15

    # Operaciones para calcular importes
    importeBruto = cantPasajes * precio
    montoDescuento = importeBruto * descuento
    importeNeto = importeBruto - montoDescuento
    return importeBruto, montoDescuento, importeNeto