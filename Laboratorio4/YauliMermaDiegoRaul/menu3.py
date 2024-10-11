# Función para obtener el precio según el tipo de servicio
def precio_serv(ts):
    if ts == 1:
        return 70.00  # Económica
    elif ts == 2:
        return 140.00  # Ejecutiva
    elif ts == 3:
        return 280.00  # Primera clase
    return 0

# Función para calcular el descuento según la cantidad de pasajes
def desc(cp):
    if cp == 1:
        return 0
    elif 2 <= cp <= 5:
        return 0.05
    elif 6 <= cp <= 10:
        return 0.12
    elif cp >= 11:
        return 0.15

# Función para registrar una venta
def reg_venta(v):
    # Validar tipo de cliente
    while True:
        try:
            tc = int(input("Ingrese tipo de cliente (1 o 2): "))
            if tc in [1, 2]:
                break
        except ValueError:
            print("Dato inválido. Intente de nuevo.")

    # Validar cantidad de pasajes
    while True:
        try:
            cp = int(input("Ingrese cantidad de pasajes: "))
            if cp > 0:
                break
        except ValueError:
            print("Dato inválido. Intente de nuevo.")
    
    # Validar género
    while True:
        gen = input("Ingrese género del cliente (M/F): ").upper()
        if gen in ['M', 'F']:
            break
    
    # Validar tipo de servicio
    while True:
        try:
            ts = int(input("Ingrese tipo de servicio (1-Económica, 2-Ejecutiva, 3-Primera clase): "))
            if ts in [1, 2, 3]:
                break
        except ValueError:
            print("Dato inválido. Intente de nuevo.")

    # Cálculo de precios
    p = precio_serv(ts)
    imp_b = cp * p
    d = desc(cp)
    m_d = imp_b * d
    imp_n = imp_b - m_d

    # Mostrar resultados
    print(f"Importe Bruto: ${imp_b:.2f}")
    print(f"Monto de Descuento: ${m_d:.2f}")
    print(f"Importe Neto a pagar: ${imp_n:.2f}")

    # Guardar venta
    v.append({
        'tc': tc,
        'cp': cp,
        'gen': gen,
        'ts': ts,
        'imp_n': imp_n
    })

# Función para generar el reporte de ventas
def reporte(v):
    cant_m = 0
    vent_70_500 = 0
    vent_f_140_1000 = 0
    total_v = 0
    total_neto_t1 = 0
    cant_t1 = 0

    for venta in v:
        total_v += venta['imp_n']
        
        if venta['gen'] == 'M':
            cant_m += 1
        
        if 70 <= venta['imp_n'] <= 500:
            vent_70_500 += 1
        
        if venta['gen'] == 'F' and 140 <= venta['imp_n'] <= 1000:
            vent_f_140_1000 += 1

        if venta['tc'] == 1:
            total_neto_t1 += venta['imp_n']
            cant_t1 += 1

    # Mostrar reporte
    print(f"\nCantidad de clientes masculinos: {cant_m}")
    print(f"Ventas entre $70 y $500: {vent_70_500}")
    print(f"Ventas femeninas entre $140 y $1000: {vent_f_140_1000}")
    print(f"Total de ventas: ${total_v:.2f}")
    print(f"Total de ventas de clientes tipo 1: ${total_neto_t1:.2f}")

    if cant_t1 > 0:
        prom_t1 = total_neto_t1 / cant_t1
        print(f"Promedio ventas tipo 1: ${prom_t1:.2f}")
    else:
        print("No hay ventas de clientes tipo 1.")

# Función principal
def main():
    v = []
    while True:
        print("----------------------------------------------")
        print("               MENÚ DE OPCIONES               ")
        print('[1]. Registrar venta.')
        print('[2]. Reportar ventas.')
        print('[3]. Salir.')
        print("----------------------------------------------")
        op = input("Elija una opción: ")

        if op == '1':
            reg_venta(v)
        elif op == '2':
            reporte(v)
        elif op == '3':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Llamada a la función principal
main()