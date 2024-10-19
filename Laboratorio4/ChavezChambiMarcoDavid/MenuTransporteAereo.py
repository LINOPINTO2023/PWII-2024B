cliMasc = 0
totalImporteVentas = 0
totalImporteClientesTipo1 = 0
cantClientesTipo1 = 0
cantVentasA = 0
cantVentasB = 0

while True:
    # Menu Empresa Transporte Aereo
    print("MENU DE OPCIONES")
    print("1. Registrar venta de pasaje")
    print("2. Reportar ventas")
    print("3. Salir\n")
    tipOpcion = int(input("Ingrese su opción: "))
    
    # OPCION 1
    if tipOpcion == 1:
        while True:
            tipCliente = int(input("Ingrese tipo de cliente (1 o 2): "))
            if tipCliente == 1 or tipCliente == 2:
                break
            else:
                print("Tipo de cliente no válido. Debe ser 1 o 2.")

        while True:
            cantPasajes = int(input("Ingrese la cantidad de pasajes a comprar: "))
            if cantPasajes > 0:
                break
            else:
                print("La cantidad de pasajes debe ser mayor a 0.")
        
        while True:
            genCliente = input("Ingrese su género (M o F): ").upper()
            if genCliente == 'M' or genCliente == 'F':
                break
            else:
                print("Género no válido. Debe ser M o F.")
        
        while True:
            tipServicio = int(input("Ingrese el tipo de servicio (1-Economica / 2-Ejecutiva / 3-Primera): "))
            if tipServicio == 1 or tipServicio == 2 or tipServicio == 3:
                break
            else:
                print("Tipo de servicio no válido. Debe ser 1, 2 o 3.")      

        # precios
        if tipServicio == 1:
            precio = 70
        elif tipServicio == 2:
            precio = 140
        else:
            precio = 280
            
        # descuentos
        if cantPasajes == 1:
            descuento = 0
        elif 2 <= cantPasajes <= 5:
            descuento = 5
        elif 6 <= cantPasajes <= 10:
            descuento = 12
        else:
            descuento = 15

        #Importe Bruto = cantidad pasajes * precio.
        impBruto = precio * cantPasajes
        #Monto de Descuento = Importe a Pagar * Porcentaje de Descuento
        montDescuento =  impBruto * descuento / 100
        #Importe Neto = Importe Bruto – Monto de Descuento
        impNeto = impBruto - montDescuento
        
        totalImporteVentas = totalImporteVentas + impBruto
        
        if tipCliente == 1:
            totalImporteClientesTipo1 = totalImporteClientesTipo1 + impNeto
            cantClientesTipo1 = cantClientesTipo1 + 1
        if genCliente == 'M':
            cliMasc = cliMasc + 1
        if 70 <= impNeto <= 500:
            cantVentasA = cantVentasA + 1
        if genCliente == 'F' and 140 <= impNeto <= 1000:
            cantVentasB = cantVentasA + 1            
        
    #OPCION 2    
    elif tipOpcion == 2:
        if cantClientesTipo1 > 0:
            promImpNetoCliTip1 = totalImporteClientesTipo1 / cantClientesTipo1
        else:
            promImpNetoCliTip1 = 0 
        #●	Cantidad de clientes de género masculino.
        print(f"Cantidad de clientes de género masculino: {cliMasc} ")
        #●	Cantidad de ventas cuyo Importe Neto sea >=70 y <=500
        print(f"Cantidad de ventas cuyo Importe Neto sea >=70 y <=500:  {cantVentasA}")
        #●	Cantidad de ventas de clientes de género femenino cuyo Importe Neto sea >=140 y <=1000
        print(f"Cantidad de ventas de clientes de género femenino cuyo Importe Neto sea >=140 y <=1000:  {cantVentasB}")
        #●	El acumulado del Importe de Ventas.
        print(f"El acumulado del Importe de Ventas:  {totalImporteVentas}")
        #●	El acumulado del Importe Neto de clientes, de tipo 1.
        print(f"El acumulado del Importe Neto de clientes, de tipo 1:  {cantClientesTipo1}")
        #●	Promedio de Importe Neto, de clientes, de tipo 1.
        print(f"Promedio de Importe Neto, de clientes, de tipo 1:  {promImpNetoCliTip1}")
    
    #OPCION 3
    else:
        print("Usted salio del programa")
        break
        
        
