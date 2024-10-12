preciosPasajes = [70.00, 140.00, 280.00]
clientes = [[None for _ in range(5)] for _ in range(100)]  # Lista de clientes con espacio para 100 clientes
numeroCliente = 0

while True:
    op = input("Seleccione una opción: \n"
               "Elija 1 si desea ingresar datos. \n"
               "Ingrese 2 si desea visualizar los resultados de las ventas \n"
               "Escriba 'salir' para salir: ")

    if op == "1":
        while True:
            tipoCliente = int(input("¿Es cliente de tipo 1 o 2? "))
            clientes[numeroCliente][0] = tipoCliente

            cantidadPasajes = int(input("¿Cuántos pasajes desea comprar? "))
            if cantidadPasajes < 2:
                descuento = 0
            elif cantidadPasajes < 6:
                descuento = 5
            elif cantidadPasajes < 11:
                descuento = 12
            else:
                descuento = 15
            clientes[numeroCliente][1] = cantidadPasajes

            generoCliente = input("¿Cuál es su género? M o F: ").upper()
            if generoCliente == 'M':
                generoCliente = 1
            else:
                generoCliente = 2
            clientes[numeroCliente][2] = generoCliente

            tipoServicio = int(input("¿Cuál es el tipo de servicio al que desea acceder? \n"
                                     "1-Económica 2-Ejecutiva 3-Primera Clase: "))
            clientes[numeroCliente][3] = tipoServicio

            costoTotal = cantidadPasajes * preciosPasajes[tipoServicio - 1]
            costoNeto = costoTotal - (descuento * costoTotal / 100)

            print(f"El costo total de sus pasajes es: {costoTotal}")
            print(f"El descuento es: {descuento}%")
            print(f"El costo a pagar es de: {costoNeto}")
            clientes[numeroCliente][4] = costoNeto

            nuevoRegistro = int(input("¿Desea realizar otro registro de ventas? \n"
                                      "Ingrese 1 para otro registro o 2 para salir: "))
            if nuevoRegistro == 2:
                break
            else:
                numeroCliente += 1

    elif op == "2":
        cont = 0
        for cliente in clientes:
            if cliente[2] == 1:  # Género masculino
                cont += 1
        print(f"Hay {cont} clientes masculinos")

        cont = 0
        for cliente in clientes:
            if cliente[4] is not None and 70 <= cliente[4] <= 500:
                cont += 1
        print(f"Hay {cont} ventas mayores a 70 y menores a 500")

        cont = 0
        for cliente in clientes:
            if cliente[4] is not None and 140 <= cliente[4] <= 1000 and cliente[2] == 2:  # Género femenino
                cont += 1
        print(f"Hay {cont} clientes de género femenino cuyo Importe Neto es >= 140 y <= 1000")

        totalVentas = sum(cliente[4] for cliente in clientes if cliente[4] is not None)
        print(f"El importe total de ventas es: {totalVentas}")

        cont = 0
        totalImporteTipo1 = 0
        iter = 0
        for cliente in clientes:
            if cliente[0] == 1:  # Cliente de tipo 1
                totalImporteTipo1 += cliente[4]
                cont += 1
        if cont > 0:
            print(f"El acumulado del Importe Neto de clientes de tipo 1 es: {totalImporteTipo1}")
            print(f"El promedio de Importe Neto de clientes de tipo 1 es: {totalImporteTipo1 / cont}")
        else:
            print("No hay clientes de tipo 1 registrados.")

    elif op.lower() == "salir":
        break

