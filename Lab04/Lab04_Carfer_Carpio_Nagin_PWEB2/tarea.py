menu=True
contadormascul = 0
contadorfem = 0
importeneto70500 = 0
importnetofem140 = 0
acumulimportventas = 0
importnetotipo1 = 0
importpromtipo1 = 0
# Bucle infinito para mantener el menú activo
while menu:
    print("Menú:")
    print("[1] Registrar venta de pasaje")
    print("[2] Reportar ventas")
    print("[3] Salir")
    opcion = input("Elija una opción: ")
    # Esta es la pción para registrar venta de pasajes
    if opcion == "1":
        while True:
            # Verificando que el tipo de cliente sea 1 o 2
            tipo_cliente = int(input("Ingrese el tipo de cliente (1 o 2): "))
            if tipo_cliente in [1, 2]:
                break
            else:
                print("Tipo de cliente no válido. Ingrese 1 o 2.")

        # Verificando que la cantidad de pasajes sea mayor a 0
        while True:
            cantidad_pasajes = int(input("Ingrese la cantidad de pasajes: "))
            if cantidad_pasajes > 0:
                break
            else:
                print("La cantidad de pasajes no puede ser 0 o negativa. Por favor, ingrese un número válido.")
        
        # Aqui onfirmamos el género del cliente, convertimos el caracter a mayuscula
        genero_cliente = input("Ingrese el género del cliente (M, F): ").upper()
        if genero_cliente not in ["M", "F"]:
            print("Género no válido. Ingrese M o F")
            continue
        
        # Verificando que el tipo de servicio sea 1, 2 o 3
        while True:
            tipo_servicio = int(input("Ingrese el tipo de servicio (1-Económica, 2-Ejecutiva, 3-Primera clase): "))
            if tipo_servicio in [1, 2, 3]:
                precios = [70, 140, 280]
                precio = precios[tipo_servicio - 1]
                break
            else:
                print("Tipo de servicio no válido. Ingrese 1, 2 o 3.")
        
        # Aqui calculamos los descuentos
        if cantidad_pasajes == 1:
            descuento = 0
        elif 2 <= cantidad_pasajes <= 5:
            descuento = 0.05
        elif 6 <= cantidad_pasajes <= 10:
            descuento = 0.12
        else:
            descuento = 0.15
        
        # Aqui calculamos el importe bruto, descuento y neto
        importe_bruto = cantidad_pasajes * precio
        monto_descuento = importe_bruto * descuento
        importe_neto = importe_bruto - monto_descuento

        # Aqui tenemos los contadores y acumuladores
        if genero_cliente == "M":
            contadormascul += 1
        elif genero_cliente == "F":
            contadorfem += 1
        
        if 70 <= importe_neto <= 500:
            importeneto70500 += 1
        if contadorfem == 'F' and 140 <= importe_neto <= 1000:
            importnetofem140 += 1

        acumulimportventas += importe_neto

        if tipo_cliente == 1:
            importnetotipo1 += importe_neto
            importpromtipo1 += 1
        
        # Aqui los resultados de la venta
        print(f"Importe Bruto: ${importe_bruto:.2f}")
        print(f"Monto de Descuento: ${monto_descuento:.2f}")
        print(f"Importe Neto: ${importe_neto:.2f}")
      
    elif opcion == "2":
        # Ventas

    # Opción para salir del programa
    elif opcion == "3":
        menu=False
    else:
        print("Opción no válida. Elija opcion 1, 2 o 3")
