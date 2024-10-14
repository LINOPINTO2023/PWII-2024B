def calcular_descuento(cantidad):
    if cantidad == 1:
        return 0
    elif 2 <= cantidad <= 5:
        return 0.05
    elif 6 <= cantidad <= 10:
        return 0.12
    else:
        return 0.15

def precio_por_servicio(tipo_servicio):
    precios = {1: 70.00, 2: 140.00, 3: 280.00}
    return precios.get(tipo_servicio, 0)

def opcion1():
    while True:
        tipo_cliente = int(input("Ingrese el tipo de cliente (1 o 2): "))
        if tipo_cliente not in [1, 2]:
            print("Tipo de cliente inválido. Debe ser 1 o 2.")
            continue
 
        cantidad_pasajes = int(input("Ingrese la cantidad de pasajes: "))
        if cantidad_pasajes < 1:
            print("Cantidad de pasajes debe ser mayor a 0.")
   
        genero = input("Ingrese el género del cliente (M/F): ").upper()
        if genero not in ['M', 'F']:
            print("Género inválido. Debe ser M o F.")
            continue

        tipo_servicio = int(input("Ingrese el tipo de servicio (1-Económica, 2-Ejecutiva, 3-Primera clase): "))
        if tipo_servicio not in [1, 2, 3]:
            print("Tipo de servicio inválido.")
            continue

        precio = precio_por_servicio(tipo_servicio)
        importe_bruto = cantidad_pasajes * precio

        descuento = calcular_descuento(cantidad_pasajes)
        monto_descuento = importe_bruto * descuento

        importe_neto = importe_bruto - monto_descuento

        print(f"Importe Bruto: ${importe_bruto:.2f}")
        print(f"Descuento: {descuento*100}%")
        print(f"Monto de Descuento: ${monto_descuento:.2f}")
        print(f"Importe Neto: ${importe_neto:.2f}")

        ventas.append({
            'tipo_cliente': tipo_cliente,
            'genero': genero,
            'importe_neto': importe_neto
        })

        continuar = input("¿Desea continuar registrando ventas? (s/n): ").lower()
        if continuar != 's':
            break

def opcion2():
    total_clientes_masculinos = sum(1 for v in ventas if v['genero'] == 'M')
    ventas_rango_70_500 = sum(1 for v in ventas if 70 <= v['importe_neto'] <= 500)
    ventas_femeninas_140_1000 = sum(1 for v in ventas if v['genero'] == 'F' and 140 <= v['importe_neto'] <= 1000)
    total_importe_ventas = sum(v['importe_neto'] for v in ventas)
    total_importe_clientes_tipo1 = sum(v['importe_neto'] for v in ventas if v['tipo_cliente'] == 1)
    promedio_tipo1 = total_importe_clientes_tipo1 / max(1, sum(1 for v in ventas if v['tipo_cliente'] == 1))

    print(f"Cantidad de clientes de género masculino: {total_clientes_masculinos}")
    print(f"Cantidad de ventas con Importe Neto entre $70 y $500: {ventas_rango_70_500}")
    print(f"Cantidad de ventas de clientes femeninos con Importe Neto entre $140 y $1000: {ventas_femeninas_140_1000}")
    print(f"Acumulado del Importe de Ventas: ${total_importe_ventas:.2f}")
    print(f"Acumulado del Importe Neto de clientes tipo 1: ${total_importe_clientes_tipo1:.2f}")
    print(f"Promedio de Importe Neto de clientes tipo 1: ${promedio_tipo1:.2f}")

ventas = []
while True:
    print("\nMenú:")
    print("1. Registrar ventas")
    print("2. Ver resultados de las ventas")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        opcion1()
    elif opcion == 2:
        opcion2()
    elif opcion == 3:
        break
    else:
        print("Opción inválida. Intente nuevamente.")
