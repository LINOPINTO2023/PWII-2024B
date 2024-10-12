# Funciones para validaciones
def obtener_entero(mensaje, min_val=None, max_val=None):
    while True:
        try:
            valor = int(input(mensaje))
            if (min_val is not None and valor < min_val) or (max_val is not None and valor > max_val):
                print(f"Error: El valor debe estar entre {min_val} y {max_val}.")
            else:
                return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def obtener_genero(mensaje):
    while True:
        genero = input(mensaje).upper()
        if genero in ['M', 'F']:
            return genero
        else:
            print("Error: Ingrese 'M' para masculino o 'F' para femenino.")

# Función para calcular el precio según el tipo de servicio
def calcular_precio_servicio(tipo_servicio):
    precios = {1: 70.00, 2: 140.00, 3: 280.00}
    return precios.get(tipo_servicio, 0)

# Función para calcular el descuento según la cantidad de pasajes
def calcular_descuento(cantidad_pasajes):
    if cantidad_pasajes == 1:
        return 0.00
    elif 2 <= cantidad_pasajes <= 5:
        return 0.05
    elif 6 <= cantidad_pasajes <= 10:
        return 0.12
    else:
        return 0.15

# Función para procesar una venta
def registrar_venta():
    global genero_m, ventas_femeninas, ventas_rango, acumulado_importe_ventas, tipo_cliente_1, acumulado_importe_neto_tipo_1
    
    tipo_cliente = obtener_entero("Ingrese tipo de cliente (1 o 2): ", 1, 2)
    cantidad_pasajes = obtener_entero("Ingrese cantidad de pasajes: ", 1)
    genero_cliente = obtener_genero("Ingrese género del cliente (M/F): ")
    tipo_servicio = obtener_entero("Ingrese tipo de servicio (1: Económico, 2: Ejecutivo, 3: Primera Clase): ", 1, 3)
    
    # Cálculos
    precio = calcular_precio_servicio(tipo_servicio)
    descuento = calcular_descuento(cantidad_pasajes)
    importe_bruto = cantidad_pasajes * precio
    monto_descuento = importe_bruto * descuento
    importe_neto = importe_bruto - monto_descuento

    # Mostrar resultados de la venta
    print(f"\nImporte Bruto: ${importe_bruto:.2f}")
    print(f"Descuento aplicado: ${monto_descuento:.2f}")
    print(f"Importe Neto: ${importe_neto:.2f}\n")

    # Actualización de estadísticas
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

# Función para mostrar el reporte de ventas
def mostrar_reporte():
    print("\nReporte de Ventas:")
    print(f"Cantidad de clientes de género masculino: {genero_m}")
    print(f"Cantidad de ventas con Importe Neto entre $70 y $500: {ventas_rango}")
    print(f"Cantidad de ventas de clientes femeninos con Importe Neto entre $140 y $1000: {ventas_femeninas}")
    print(f"Acumulado total de Importe de Ventas: ${acumulado_importe_ventas:.2f}")
    
    if tipo_cliente_1 > 0:
        promedio_importe_neto_tipo_1 = acumulado_importe_neto_tipo_1 / tipo_cliente_1
        print(f"Acumulado de Importe Neto de clientes de tipo 1: ${acumulado_importe_neto_tipo_1:.2f}")
        print(f"Promedio de Importe Neto de clientes de tipo 1: ${promedio_importe_neto_tipo_1:.2f}")
    else:
        print("No se han registrado clientes de tipo 1.")

# Variables acumulativas globales
genero_m = 0
ventas_rango = 0
ventas_femeninas = 0
acumulado_importe_ventas = 0
tipo_cliente_1 = 0
acumulado_importe_neto_tipo_1 = 0

# Bucle principal
verificar_menu = True
while verificar_menu:
    print("BIENVENIDO A MI PROGRAMA DE EMPRESA DE TRANSPORTES INTERPROVINCIAL\n\n\n")
    print("\nMENU DE OPCIONES\n[1] REGISTRAR VENTA DE PASAJE\n[2] REPORTAR VENTAS\n[3] SALIR")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        continue

    if opcion == 1:
        registrar_venta()
        # Opción para seguir registrando ventas o volver al menú principal
        while True:
            otra_opcion = input("\n¿Desea registrar otra venta? (S/N): ").upper()
            if otra_opcion == 'S':
                registrar_venta()
            elif otra_opcion == 'N':
                break
            else:
                print("Opción no válida. Ingrese 'S' o 'N'.")
                
    elif opcion == 2:
        mostrar_reporte()
        
    elif opcion == 3:
        verificar_menu = False
        print("Saliendo del programa...")

    else:
        print("Error: Opción no válida. Intente de nuevo.")
