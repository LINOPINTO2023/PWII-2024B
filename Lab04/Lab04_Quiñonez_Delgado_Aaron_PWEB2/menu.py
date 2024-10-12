opcionMenu = int(input("BIENVENIDO A LA EMPRESA ROYDAN LATAM\nSELECIONE UNA OPCIÓN:\n[1]REGISTAR VENTA DE PASAJE\n[2]REPORTAR VENTAS\n[3]SALIR\n"))
#Creamos variables que almacenaran datos para el reporte de ventas
cantidadHombres = 0
cantidadMujeres = 0
#Creamos variable que almacenará los datos de los usuarios
usuarioID = 0
usuarios = {}
def agregarUsuario(id, tipo, pasajes, genero, servicio, impNeto):
     usuarios[id] = {
          "tipo" : tipo,
          "pasajes" : pasajes,
          "genero" : genero,
          "servicio" : servicio,
          "neto" : impNeto
     }
#Utilizamos condiciones para que nos asegure que el numero escrito está en el rango permitido
while True:
    if 0 < opcionMenu < 4:
        #Registrar venta de pasaje
        if opcionMenu == 1:
            #Tipo de cliente
            while True:
                tipoCliente = int(input("Tipo de cliente (1 ó 2): "))
                if tipoCliente != 1 and tipoCliente != 2:
                     print("Número equivocado, escoja otra vez")
                else:
                     break
            #Cantidad de pasajes
            while True: 
                cantidadPasajes = int(input("Ingrese la cantidad de pasajes: "))
                if cantidadPasajes < 1:
                     print("Ingrese una cantidad válida")
                else:
                     break
            #Género del cliente
            while True:
                generoCliente = input("Ingrese su género (M o F): ")
                if generoCliente in ["M", "F", "m", "f"]:
                     if generoCliente in ["M", "m"]:
                          cantidadHombres = cantidadHombres + 1
                     else:
                          cantidadMujeres = cantidadMujeres + 1
                     break
                else:
                    print("Por favor, ingrese un valor válido (M o F).")
            #Tipo de servicio
            while True:
                tipoServicio = int(input("Indique tipo de servicio:\n[1]Económica\n[2]Ejecutiva\n[3]Primera clase\n"))
                #Precio total Económico
                if tipoServicio == 1:
                        precioPasaje = cantidadPasajes*70
                        break
                #Precio total Ejecutivo
                elif tipoServicio == 2:
                        precioPasaje = cantidadPasajes*140
                        break
                #Precio total Primera clase
                elif tipoServicio == 3:
                        precioPasaje = cantidadPasajes*280
                        break
                else:
                     print("Número incorrecto, escoja de nuevo")
                
            #Aplicación de descuento
            if cantidadPasajes == 1:
                print("No aplica descuento")
            elif 1 < cantidadPasajes < 6:
                print(f"Obtiene un 5% de descuento")
                precioPasajeFinal = (precioPasaje*95)/100
            elif 5 < cantidadPasajes < 11:
                    print(f"Obtiene un 12% de descuento")
                    precioPasajeFinal = (precioPasaje*88)/100
            elif cantidadPasajes > 10:
                    print(f"Obtiene un 15% de descuento")
                    precioPasajeFinal = (precioPasaje*85)/100
            #Imprimir información de informe bruto
            importeBruto = precioPasaje
            descuento = precioPasajeFinal - precioPasaje
            importeNeto = importeBruto - descuento
            #Usamos la función para almacenar los datos de los usuarios
            usuarioID += 1
            agregarUsuario(usuarioID, tipoCliente, cantidadPasajes, generoCliente, tipoServicio, importeNeto)

        elif opcionMenu == 2:
             #Reporte de ventas
             
             #Cantidad de hombres

        else:
             break

        break
    else:
        print("Opción no válida, vuelva a ingresar el número")