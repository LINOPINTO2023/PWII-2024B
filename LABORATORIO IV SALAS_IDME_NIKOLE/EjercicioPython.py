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
    def main():
    totalVentas = 0
    totalMasculinos = 0
    rango70_500 = 0
    femeninas_rango140_1000 = 0
    acumulado1 = 0
    cant1 = 0
    continuar = True
    
    while continuar:
        opcion = input("1. Ingresar ventas\n2. Ver total de ventas\n3. Salir\nSeleccione una opción: ")
        if opcion == '1':
            tipoCliente, cantPasajes, genero, tipoServicio = ingresar_datos()
            importeBruto, montoDescuento, importeNeto = calcular_precio(cantPasajes, tipoServicio)
            totalVentas += importeNeto
            
            # Clientes masculinos
            if genero == 'm':
                totalMasculinos += 1
                
            # Ventas en rango de 70 a 500
            if 70 <= importeNeto <= 500:
                rango70_500 += 1
                
            # Clientes femeninos en rango de 140 a 1000
            if genero == 'f' and 140 <= importeNeto <= 1000:
                femeninas_rango140_1000 += 1
                
            # Acumulado de ventas de clientes tipo 1
            if tipoCliente == 1:
                acumulado1 += importeNeto
                cant1 += 1
            
            print(f"Importe bruto: ${importeBruto:.2f}")
            print(f"Monto de descuento: ${montoDescuento:.2f}")
            print(f"Importe neto: ${importeNeto:.2f}")
            elif opcion == '2':
            if cant1 > 0:
                promedio1 = acumulado1 / cant1
            else:
                promedio1 = 0

            print(f"\n--- Resultados Totales ---")
            print(f"Cantidad de clientes de género masculino: {totalMasculinos}")
            print(f"Cantidad de ventas con importe neto entre 70 y 500: {rango70_500}")
            print(f"Cantidad de ventas de clientes femeninos con importe neto entre 140 y 1000: {femeninas_rango140_1000}")
            print(f"Acumulado del importe de ventas: ${totalVentas:.2f}")
            print(f"Acumulado del importe neto de clientes tipo 1: ${acumulado1:.2f}")
            print(f"Promedio del importe neto de clientes tipo 1: ${promedio1:.2f}")
        elif opcion == '3':
            continuar = False
        else:
            print("Opción inválida, intente de nuevo.")