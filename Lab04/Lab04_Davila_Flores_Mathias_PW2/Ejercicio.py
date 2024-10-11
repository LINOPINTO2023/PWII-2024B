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
        

    elif opcion == 2:
        

    elif opcion == 3:
        verificar_menu = False

    else:
        print("ERROR: Opción no válida. Intente de nuevo.")
