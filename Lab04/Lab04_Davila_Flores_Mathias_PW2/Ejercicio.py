verificar_menu = True
genero_m = 0  # Cantidad de clientes masculinos
importe_bruto = 0
importe_neto = 0
monto_descuento = 0
tipo_cliente_1 = 0  # Contador de clientes de tipo 1
acumulado_importe_neto_tipo_1 = 0
acumulado_importe_ventas = 0  # Total de ventas
ventas_femeninas = 0  # Ventas de clientes femeninos con importes entre 140 y 1000
ventas_rango = 0  # Ventas con importes entre 70 y 500
tipo_cliente = 0
while verificar_menu:
    print("\nMENU DE OPCIONES\n[1] REGISTRAR VENTA DE PASAJE\n[2] REPORTAR VENTAS\n[3] SALIR")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        while True:
            # Validar tipo de cliente
            tipo_cliente = int(input("Ingrese tipo de cliente (1 o 2): "))
            while tipo_cliente != 1 and tipo_cliente != 2:
                print("Error. Ingrese una opcion valida")
                tipo_cliente = int(input("Ingrese tipo de cliente (1 o 2): "))

            # Validar cantidad de pasajes
            numero_pasajes = int(input("Ingrese cantidad de pasajes: "))
            while numero_pasajes <= 0:
                print("Error. Ingrese una opcion valida")
                numero_pasajes = int(input("Ingrese cantidad de pasajes: "))
            
            # Validar género del cliente
            genero_cliente = input("Ingrese género del cliente (M/F): ").upper()
            while genero_cliente != 'M' and genero_cliente != 'F':
                print("Error. Ingrese una opcion valida")
                genero_cliente = input("Ingrese género del cliente (M/F): ").upper()
            
            # Validar tipo de servicio
            tipo_servicio = int(input("Ingrese tipo de servicio (1: Económico, 2: Ejecutivo, 3: Primera Clase): "))
            while tipo_servicio != 1 and tipo_servicio != 2 and tipo_servicio != 3:
                print("Error. Ingrese una opcion valida")
                tipo_servicio = int(input("Ingrese tipo de servicio (1: Económico, 2: Ejecutivo, 3: Primera Clase): "))
            
            # Precios
            if tipo_servicio == 1:
                precio = 70.00
            elif tipo_servicio == 2:
                precio = 140.00
            elif tipo_servicio == 3:
                precio = 280.00

            # Descuentos segun el  numero de pasajes
            if numero_pasajes == 1:
                desc = 0.00
            elif 2 <= numero_pasajes <= 5:
                desc = 0.05
            elif 6 <= numero_pasajes <= 10:
                desc = 0.12
            else:
                desc = 0.15
            
            # Cálculos de importes
            importe_bruto = numero_pasajes * precio
            monto_descuento = importe_bruto * desc
            importe_neto = importe_bruto - monto_descuento

            # Actualización de datos
            acumulado_importe_ventas += importe_neto

            if genero_cliente == 'M':
                genero_m += 1
            if genero_cliente == 'F' and 140 <= importe_neto <= 1000:
                ventas_femeninas += 1
            if 70 <= importe_neto <= 500:
                ventas_rango += 1
            if tipo_cliente == 1:
                tipo_cliente_1 += 1
                acumulado_importe_neto_tipo_1 += importe_neto
            
            # Mostrar resultados de la venta
            print("\nResumen de la venta:")
            print(f"Importe Bruto: ${importe_bruto:.2f}")
            print(f"Descuento aplicado: ${monto_descuento:.2f}")
            print(f"Importe Neto: ${importe_neto:.2f}\n")
            
            # Menu para ver si desea realizar otro movimiento o salir de la opcion 1 (registrar pasaje de venta)
            print("\nMENU DE OPCIONES\n[1] REGISTRAR OTRA VENTA\n[2] SALIR")
            otra_opcion = int(input("Seleccione una opción: "))
            if otra_opcion == 2:
                break  # Salir al menú principal

    elif opcion == 2:
        # Mostrar reporte de ventas
        print("\nReporte de Ventas:")
        print(f"Cantidad de clientes de género masculino: {genero_m}")
        print(f"Cantidad de ventas con Importe Neto entre $70 y $500: {ventas_rango}")
        print(f"Cantidad de ventas de clientes femeninos con Importe Neto entre $140 y $1000: {ventas_femeninas}")
        print(f"Acumulado total de Importe de Ventas: ${acumulado_importe_ventas:.2f}")
        print(f"Acumulado de Importe Neto de clientes de tipo 1: ${acumulado_importe_neto_tipo_1:.2f}")
    
        # Calcular promedio de Importe Neto de clientes tipo 1
        if tipo_cliente_1 > 0:
            promedio_importe_neto_tipo_1 = acumulado_importe_neto_tipo_1 / tipo_cliente_1
        else:
            promedio_importe_neto_tipo_1 = 0
        print(f"Promedio de Importe Neto de clientes de tipo 1: ${promedio_importe_neto_tipo_1:.2f}")

    elif opcion == 3:
        verificar_menu = False

    else:
        print("ERROR: Opción no válida. Intente de nuevo.")
