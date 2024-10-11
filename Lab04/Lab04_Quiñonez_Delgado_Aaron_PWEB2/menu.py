opcionMenu = int(input("BIENVENIDO A LA EMPRESA ROYDAN LATAM\nSELECIONE UNA OPCIÓN:\n[1]REGISTAR VENTA DE PASAJE\n[2]REPORTAR VENTAS\n[3]SALIR\n"))
#Utilizamos condiciones para que nos asegure que el numero escrito está en el rango permitido
while True:
    if 0 < opcionMenu < 4:
        #Registrar venta de pasaje
        if opcionMenu == 1:
            tipoCliente = int(input("Tipo de cliente (1 ó 2): "))
            while True: 
                cantidadPasajes = int(input("Ingrese la cantidad de pasajes: "))
                if cantidadPasajes < 1:
                     print("Ingrese una cantidad válida")
                else:
                     break
            while True:
                generoCliente = input("Ingrese su género (M o F): ")
                if generoCliente in ['M', 'F']:
                    print("Por favor, ingrese un valor válido (M o F).")
                else:
                    break
            tipoServicio = int(input("Indique tipo de servicio:\n[1]Económica\n[2]Ejecutiva\n[3]Primera clase\n"))
            #Precio total Económico
            if tipoServicio == 1:
                    precioPasaje = cantidadPasajes*70
            #Precio total Ejecutivo
            elif tipoServicio == 2:
                    precioPasaje = cantidadPasajes*140
            #Precio total Primera clase
            elif tipoServicio == 3:
                    precioPasaje = cantidadPasajes*280
            #Aplicación de descuento
            if cantidadPasajes == 1:
                print("No aplica descuento")
            elif 1 < cantidadPasajes < 6:
                print(f"Obtiene un 5% de descuento")
                precioPasajeFinal = (precioPasaje*95)/100
            elif 6 < cantidadPasajes < 11:
                    print(f"Obtiene un 12% de descuento")
                    precioPasajeFinal = (precioPasaje*88)/100
            elif cantidadPasajes > 10:
                    print(f"Obtiene un 15% de descuento")
                    precioPasajeFinal = (precioPasaje*85)/100
            #Imprimir información de informe bruto
            importeBruto = precioPasaje
            descuento = precioPasajeFinal - precioPasaje
            importeNeto = importeBruto - descuento

        break
    else:
        print("Opción no válida, vuelva a ingresar el número")
        input