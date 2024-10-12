#Creamos variables que almacenaran datos para el reporte de ventas
cantidadHombres = 0
cantidadMujeres = 0
#Creamos variable que almacenará los datos de los usuarios
usuarios = []
registro = {}
def agregarUsuario(tipo, pasajes, genero, servicio, impNeto, impBruto):
     registro = {
          "tipo" : tipo,
          "pasajes" : pasajes,
          "genero" : genero,
          "servicio" : servicio,
          "neto" : impNeto,
          "bruto" : impBruto
     }
     usuarios.append(registro)
#Utilizamos condiciones para que nos asegure que el numero escrito está en el rango permitido
while True:
    opcionMenu = int(input("BIENVENIDO A LA EMPRESA ROYDAN LATAM\nSELECIONE UNA OPCIÓN:\n[1]REGISTAR VENTA DE PASAJE\n[2]REPORTAR VENTAS\n[3]SALIR\n"))
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
                          cantidadHombres += 1
                     else:
                          cantidadMujeres += 1
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
            #Imprimir información
            importeBruto = precioPasaje
            print(f"Importe Bruto: {importeBruto}")
            descuento = precioPasaje - precioPasajeFinal 
            print(f"Descuento: {descuento:.2f}")
            importeNeto = importeBruto - descuento
            print(f"Importe neto: {importeNeto}")
            #Usamos la función para almacenar los datos de los usuarios
            agregarUsuario(tipoCliente, cantidadPasajes, generoCliente, tipoServicio, importeNeto, importeBruto)
        #Reporte de ventas
        elif opcionMenu == 2:
             #Cantidad de hombres
             print(f"Cantidad de clientes masculinos: {cantidadHombres}")
             #Cantidad de ventas cuyo importe neto sea >=70 y <=500
             impNetoComparacion = sum(1 for usuario in usuarios if 70 <= usuario["neto"] <= 500)
             print(f"Cantidad de ventas cuyo importe neto sea entre 70 y 500 {impNetoComparacion}")
             #Clientes de género femenino cuyo importe neto sea >=140 y <=1000
             cantidadMujeresImpNeto = sum(1 for usuario in usuarios if 140 <= usuario["neto"] <= 1000 and (usuario["genero"] == "f" or usuario["genero"] == "F"))
             print(f"Clientes femeninas cuyo importe neto sea entre 140 y 1000: {cantidadMujeresImpNeto}")
             #Acumulado de importe de ventas
             totalImpVentas = sum(usuario["bruto"] for usuario in usuarios)
             print(f"Acumulado de importe de ventas: {totalImpVentas}")
             #Acumulado del Importe Neto de clientes, de tipo 1
             totalImpNeto = sum(usuario["neto"] for usuario in usuarios if usuario["tipo"] == 1)
             print(f"Acumulado de importe neto de clientes, de tipo 1: {totalImpNeto}")
             #Promedio de Importe Neto, de clientes, de tipo 1
             cantidadTipo1 = sum(1 for usuario in usuarios if usuario["tipo"] == 1)
             promedio = totalImpNeto/cantidadTipo1 
             print(f"Promedio de importe neto de clientes, de tipo 1: {promedio}")
        else:
             break
    else:
        print("Opción no válida, vuelva a ingresar el número")