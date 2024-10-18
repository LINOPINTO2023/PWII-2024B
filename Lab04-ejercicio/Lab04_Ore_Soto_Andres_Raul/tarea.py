hombres = 0
mujeres = 0
mujeres_obj = 0
punto_obj = 0
neto_obj = 0
importe_tipo1 = 0
contador_tipo1 = 0


def registrar_datos():
    global neto_obj, importe_tipo1, contador_tipo1
    contador = 0
    dinero_bolsa = 0
    descuento = 0

    ingresos = input("¿Cuales son sus ingresos?: ")
    pasajes = input("¿Cuántos pasajes comprará?: ")

    while contador < int(pasajes):
        # Género de las personas
        genero = input("¿Cuál es su género (M/F): ")
        if genero.lower() == "m":
            global hombres
            hombres += 1
        elif genero.lower() == "f":
            global mujeres
            mujeres += 1
        else:
            print("Ingrese un género válido")
            continue

        # Datos de los tipos de boletos
        tipo_servicio = input(
            "Ingrese el tipo de servicio (1-Economica / 2-Ejecutiva / 3-Primera clase): ")
        if tipo_servicio == "1":
            dinero_bolsa += 70
            importe_tipo1 += 70
            contador_tipo1 += 1
        elif tipo_servicio == "2":
            dinero_bolsa += 140
        elif tipo_servicio == "3":
            dinero_bolsa += 280
        else:
            print("Ingrese una cantidad correcta")
            contador -= 1
            continue

        contador += 1

    # Aplica descuento según la cantidad de pasajes
    if int(pasajes) == 1:
        descuento = 1
    elif 2 <= int(pasajes) <= 5:
        descuento = 5/100
    elif 6 <= int(pasajes) <= 10:
        descuento = 12/100
    elif int(pasajes) >= 11:
        descuento = 15/100

    importe_bruto = dinero_bolsa
    descuento = importe_bruto * descuento
    neto = importe_bruto - descuento
    neto_obj += neto

    # Conteo de pasajes
    if 70 <= neto <= 500:
        global punto_obj
        punto_obj += 1
    if 140 <= neto <= 1000 and genero.lower() == "f":
        global mujeres_obj
        mujeres_obj += 1

    print(f"Tu importe bruto es: {importe_bruto}")
    print(f"El monto de descuento es: {descuento}")
    print(f"El monto total a pagar es: {neto}")


def mostrar_resultados():
    promedio_tipo1 = importe_tipo1 / contador_tipo1 if contador_tipo1 > 0 else 0
    print(f"La cantidad de varones que compraron los pasajes son: {hombres}")
    print(f"La cantidad de ventas con un importe neto entre >=70 y <=500 son: {
          punto_obj}")
    print(f"La cantidad de mujeres con importe neto entre >=140 y <=1000 son: {
          mujeres_obj}")
    print(f"El importe neto total es de: {neto_obj}")
    print(f"El acumulado del importe de ventas de clientes de tipo 1 es: {
          importe_tipo1}")
    print(f"El promedio del importe neto de clientes de tipo 1 es: {
          promedio_tipo1:.2f}")


# Lógica de las preguntas
while True:
    print("1. Continuar con el registro de ventas")
    print("2. Mostrar los resultados")
    answer = input("Ingrese la opción que desea: ")

    if answer == "1":
        registrar_datos()
        pregunta = input("¿Desea pasar a mostrar los resultados (S/N)?: ")
        if pregunta.lower() == "s":
            mostrar_resultados()
            break
    elif answer == "2":
        mostrar_resultados()
        pregunta = input("¿Desea realizar otra operación (S/N)?: ")
        if pregunta.lower() != "s":
            print("¡Hasta la próxima! :D")
            break
    else:
        print("Ingrese una opción válida")
