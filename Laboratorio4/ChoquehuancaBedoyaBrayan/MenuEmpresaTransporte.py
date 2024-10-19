# Diccionario de ventas
ventas = []

# mostrar el menú principal
def mostrar_menu():
    print("--------MENU DE OPCIONES--------")
    print("[1]. REGISTRAR VENTA DE PASAJES")
    print("[2]. REPORTAR VENTAS")
    print("[3]. SALIR")
    print("--------------------------------")

# Opción 1: Registrar venta de pasajes
def opcion_1():
    while True:
        try:
            # Valida tipo de cliente (1 o 2)
            tipo_cliente = int(input("Ingrese el tipo de cliente (1-2): "))
            if tipo_cliente < 1 or tipo_cliente > 2:
                print("El tipo de cliente debe ser un número entre 1 y 2.")
                continue  # Volver a pedir el dato si no es válido
            
            # Valida cantidad de pasajes (debe ser entero positivo)
            cantidad_pasajes = int(input("Ingrese la cantidad de pasajes: "))
            if cantidad_pasajes <= 0:
                print("La cantidad de pasajes debe ser mayor a 0.")
                continue
            
            # Valida género (M o F)
            genero = input("Ingrese su género (M o F): ").upper()
            if genero not in ['M', 'F']:
                print("El género debe ser 'M' o 'F'.")
                continue
            
            # Valida tipo de servicio (1-Económica, 2-Ejecutiva, 3-Primera Clase)
            tipo_servicio = int(input("Ingrese el tipo de servicio (1-Economica / 2-Ejecutiva / 3-Primera clase): "))
            if tipo_servicio < 1 or tipo_servicio > 3:
                print("El tipo de servicio debe ser un número entre 1 y 3.")
                continue

            # Precios según el tipo de servicio
            precios = {1: 70.00, 2: 140.00, 3: 280.00}
            precio = precios[tipo_servicio]

            # Calcula el importe bruto
            importe_bruto = cantidad_pasajes * precio

            # Calcula porcentaje de descuento según la cantidad de pasajes
            if cantidad_pasajes == 1:
                descuento = 0
            elif 2 <= cantidad_pasajes <= 5:
                descuento = 0.05
            elif 6 <= cantidad_pasajes <= 10:
                descuento = 0.12
            else:
                descuento = 0.15

            # Calcula el monto de descuento y el importe neto
            monto_descuento = importe_bruto * descuento
            importe_neto = importe_bruto - monto_descuento

            # Muestra los resultados
            print(f"Importe Bruto: ${importe_bruto:.2f}")
            print(f"Descuento Aplicado: {descuento * 100}%")
            print(f"Monto de Descuento: ${monto_descuento:.2f}")
            print(f"Importe Neto a Pagar: ${importe_neto:.2f}")

            # Guarda la venta en la lista
            ventas.append({
                "tipo_cliente": tipo_cliente,
                "cantidad_pasajes": cantidad_pasajes,
                "genero": genero,
                "tipo_servicio": tipo_servicio,
                "importe_neto": importe_neto
            })

            break  # Salir del bucle cuando los datos son válidos
        except ValueError:
            print("Por favor, ingrese un valor válido.")

# Opción 2: Reportar ventas
def opcion_2():
    # Inicializar variables para el reporte
    total_ventas_masculino = 0
    total_ventas_netos = 0
    ventas_monto_rango_70_500 = 0
    ventas_femenino_rango_140_1000 = 0
    acumulado_importe_tipo1 = 0
    clientes_tipo1 = 0

    for venta in ventas:
        total_ventas_netos += venta["importe_neto"]

        # Contar clientes masculinos
        if venta["genero"] == 'M':
            total_ventas_masculino += 1

        # Contar ventas con importe neto en el rango de 70 a 500
        if 70 <= venta["importe_neto"] <= 500:
            ventas_monto_rango_70_500 += 1

        # Contar ventas de mujeres con importe neto en el rango de 140 a 1000
        if venta["genero"] == 'F' and 140 <= venta["importe_neto"] <= 1000:
            ventas_femenino_rango_140_1000 += 1

        # Acumular importe neto de clientes de tipo 1
        if venta["tipo_cliente"] == 1:
            acumulado_importe_tipo1 += venta["importe_neto"]
            clientes_tipo1 += 1

    # Calcular promedio de importe neto de clientes de tipo 1
    promedio_importe_tipo1 = acumulado_importe_tipo1 / clientes_tipo1 if clientes_tipo1 > 0 else 0

    # Mostrar el reporte
    print("\n--------REPORTE DE VENTAS--------")
    print(f"Cantidad de clientes de género masculino: {total_ventas_masculino}")
    print(f"Cantidad de ventas con importe neto entre $70 y $500: {ventas_monto_rango_70_500}")
    print(f"Ventas de clientes femeninos con importe neto entre $140 y $1000: {ventas_femenino_rango_140_1000}")
    print(f"Acumulado del importe total de ventas: ${total_ventas_netos:.2f}")
    print(f"Acumulado del importe neto de clientes tipo 1: ${acumulado_importe_tipo1:.2f}")
    print(f"Promedio de importe neto de clientes tipo 1: ${promedio_importe_tipo1:.2f}")

# Función para ejecutar la opción seleccionada
def ejecutar_opcion(opcion):
    match opcion:
        case '1':
            opcion_1()
        case '2':
            if ventas:
                opcion_2()
            else:
                print("No se han registrado ventas aún.")
        case '3':
            print("Saliendo ...")
        case _:
            print("Opción no válida. Escoge una opción (1-3).")

# Bucle principal del menú y las opciones
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-3): ")
    print()
    if opcion == '3':
        break
    ejecutar_opcion(opcion)
