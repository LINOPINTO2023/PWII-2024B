def ingresar_datos():
    tipo_cliente = int(input("Ingrese el tipo de cliente (1 o 2): "))
    cantidad_pasajes = int(input("Ingrese la cantidad de pasajes: "))
    genero = input("Ingrese el género del cliente (M/F): ").lower()
    tipo_servicio = int(input("Ingrese el tipo de servicio (1-Económica, 2-Ejecutiva, 3-Primera clase): "))
    return tipo_cliente, cantidad_pasajes, genero, tipo_servicio

def calcular_precio(cantidad_pasajes, tipo_servicio):
    if tipo_servicio == 1:
        precio_base = 70
    elif tipo_servicio == 2:
        precio_base = 140
    elif tipo_servicio == 3:
        precio_base = 280
    else:
        print("Tipo de servicio inválido.")
        return 0, 0, 0

    if cantidad_pasajes == 1:
        descuento = 0
    elif 2 <= cantidad_pasajes <= 5:
        descuento = 0.05
    elif 6 <= cantidad_pasajes <= 10:
        descuento = 0.12
    else:
        descuento = 0.15

    importe_bruto = cantidad_pasajes * precio_base
    monto_descuento = importe_bruto * descuento
    importe_neto = importe_bruto - monto_descuento

    return importe_bruto, monto_descuento, importe_neto

def main():
    total_ventas = 0
    total_clientes_masculinos = 0
    ventas_rango_70_500 = 0
    ventas_femeninas_rango_140_1000 = 0
    acumulado_tipo_1 = 0
    cantidad_tipo_1 = 0
    continuar = True

    while continuar:
        opcion = input("1. Ingresar ventas\n2. Ver total de ventas\n3. Salir\nSeleccione una opción: ")
        
        if opcion == '1':
            tipo_cliente, cantidad_pasajes, genero, tipo_servicio = ingresar_datos()
            importe_bruto, monto_descuento, importe_neto = calcular_precio(cantidad_pasajes, tipo_servicio)
            total_ventas += importe_neto

            # Contar clientes de género masculino
            if genero == 'm':
                total_clientes_masculinos += 1

            # Contar ventas en el rango 70 <= Importe Neto <= 500
            if 70 <= importe_neto <= 500:
                ventas_rango_70_500 += 1

            # Contar ventas de clientes femeninos en el rango 140 <= Importe Neto <= 1000
            if genero == 'f' and 140 <= importe_neto <= 1000:
                ventas_femeninas_rango_140_1000 += 1

            # Acumular importe neto de clientes de tipo 1
            if tipo_cliente == 1:
                acumulado_tipo_1 += importe_neto
                cantidad_tipo_1 += 1

            # Mostrar resultados por cliente
            print(f"Importe bruto: ${importe_bruto:.2f}")
            print(f"Monto de descuento: ${monto_descuento:.2f}")
            print(f"Importe neto: ${importe_neto:.2f}")
        
        elif opcion == '2':
            if cantidad_tipo_1 > 0:
                promedio_tipo_1 = acumulado_tipo_1 / cantidad_tipo_1
            else:
                promedio_tipo_1 = 0

            print(f"\n--- Resultados Totales ---")
            print(f"Cantidad de clientes de género masculino: {total_clientes_masculinos}")
            print(f"Cantidad de ventas con importe neto entre 70 y 500: {ventas_rango_70_500}")
            print(f"Cantidad de ventas de clientes femeninos con importe neto entre 140 y 1000: {ventas_femeninas_rango_140_1000}")
            print(f"Acumulado del importe de ventas: ${total_ventas:.2f}")
            print(f"Acumulado del importe neto de clientes tipo 1: ${acumulado_tipo_1:.2f}")
            print(f"Promedio del importe neto de clientes tipo 1: ${promedio_tipo_1:.2f}")
        
        elif opcion == '3':
            continuar = False
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
