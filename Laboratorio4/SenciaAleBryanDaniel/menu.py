
#CONTADORESPARA LA OPCION 2 DE LOS DATOS DE OPCION 1
hombreOne = 0
mujerOne = 0
hombreTwo = 0
mujerTwo = 0
ventasNeto = 0
ventasMujeres = 0
venTotales = 0
impClientOne = 0
promClientOne = 0


#MENU 
while True:
    print("---------------------------")
    print("MENU DE OPCIONES")
    print("[1] REGISTRAR VENTA DE PASAJE")
    print("[2] REPORTAR VENTAS")
    print("[3] SALIR")
    operacion = input("QUE OPERACION DESEA REALIZAR =>")
    
#TIPO DE OPERACION-1
    if operacion == '1':

    #SELECCION DEL TIPO DE CLIENTE
        while True:
            print("---------------------------")
            print("### REGISTRAR VENTA DE PASAJE ###")
            print("--SELECCIONE EL TIPO DE CLIENTE--")
            print("[1] => TIPO 1")
            print("[2] => TIPO 2")
            print("[3] => VOLVER AL MENU")
            tipClient = input("SELECCIONE LA OPCION: ")

        #CLIENTE TIPO-1
            if tipClient == '1':
                print("---------------------------")
                print("CLIENTE TIPO [1]")
                print("#############")
                print("CANTIDAD DE PASAJES:]")
                pasajes = input("SELECCIONE: [1,2,3,4,5,6,7,8,9,10,...] => ")
                while not pasajes.isdigit() or int(pasajes) < 1:
                    print("INGRESE UNA CANTIDAD DE PASAJES VALIDA")
                    pasajes = input("SELECCIONE: [1,2,3,4,5,6,7,8,9,10,...] => ")
                
                print("#############")
                print("MASCULINO => [M]")
                print("FEMENINO => [F]")
                genero = input("INGRESE SU GENERO: ").upper()
                while genero != "M" and genero != "F":
                    print("INGRESE UN GENERO VALIDO")
                    genero = input("INGRESE SU GENERO (M/F): ").upper()
                if genero == "M":
                    hombreOne += 1
                elif genero == "F":
                    mujerOne += 1
                
                print("#############")
                print("[1] => ECONOMICA")
                print("[2] => EJECUTIVA")
                print("[3] => PRIMERA CLASE")
                servicioMax = 3
                tipoServicio = input("SELECCIONE EL TIPO DE SERVICIO: ")
                while not tipoServicio.isdigit() or int(tipoServicio) < 1 or int(tipoServicio) > servicioMax:
                    print("INGRESE UN TIPOS DE SERVICIO VALIDO")
                    print("[1] => ECONOMICA")
                    print("[2] => EJECUTIVA")
                    print("[3] => PRIMERA CLASE")
                    tipoServicio = input("SELECCIONE EL TIPO DE SERVICIO: ")

                print("#############")
                print("DATOS CALCULADOS DEL CLIENTE CON RESPECTO AL SEVICIO")

            #CALCULO DE LOS DATOS A MOSTRAR CLIENTE TIPO-1
                if pasajes == '1':
                    descPasaje = 0
                elif '2' <= pasajes <= '5':
                    descPasaje = 0.05  
                elif '6' <= pasajes <= '10':
                    descPasaje = 0.12  
                else:
                    descPasaje = 0.15  

                if tipoServicio == '1':
                    costServicio = 70
                elif tipoServicio == '2':
                    costServicio = 140
                else:
                    costServicio = 280
                
                impBruto = int(pasajes)*costServicio
                montDesc = impBruto*descPasaje
                impNeto = impBruto - montDesc

                #INFO PARA EL REPORTE
                if impNeto>=70 and impNeto<=500:
                    ventasNeto = ventasNeto+1
                
                if genero == 'F' and (impNeto>=140 and impNeto<=1000):
                    ventasMujeres = ventasMujeres+1
                
                venTotales = venTotales + impNeto

                impClientOne = impClientOne+ impNeto

                print(f"IMPORTE BRUTO: {impBruto}")
                print(f"MONTO DE DESCUENTO: {montDesc}")
                print(f"IMPORTE NETO: {impNeto}")
                
                '''
                if tipoServicio == '1' and pasajes == '1':
                    impBruto = 1*70
                    montDesc = impBruto*0
                    impNeto = impBruto - montDesc
                elif tipoServicio == '1' and (int(pasajes)>2 and int(pasajes)<5 ):
                    impBruto = 1*70
                    montDesc = impBruto*0.05
                    impNeto = impBruto - montDesc
                '''

        #CLIENTE TIPO-2
            elif tipClient == '2':
                print("---------------------------")
                print("CLIENTE TIPO [2]")

                print("#############")
                print("CANTIDAD DE PASAJES:]")
                pasajes = input("SELECCIONE: [1,2,3,4,5,6,7,8,9,10,...] => ")
                while not pasajes.isdigit() or int(pasajes) < 1:
                    print("INGRESE UNA CANTIDAD DE PASAJES VALIDA")
                    pasajes = input("SELECCIONE: [1,2,3,4,5,6,7,8,9,10,...] => ")
                
                print("#############")
                print("MASCULINO => [M]")
                print("FEMENINO => [F]")
                genero = input("INGRESE SU GENERO: ").upper()
                while genero != "M" and genero != "F":
                    print("INGRESE UN GENERO VALIDO")
                    genero = input("INGRESE SU GENERO (M/F): ").upper()
                if genero == "M":
                    hombreTwo += 1
                elif genero == "F":
                    mujerTwo += 1
                
                print("#############")
                print("[1] => ECONOMICA")
                print("[2] => EJECUTIVA")
                print("[3] => PRIMERA CLASE")
                servicioMax = 3
                tipoServicio = input("SELECCIONE EL TIPO DE SERVICIO: ")
                while not tipoServicio.isdigit() or int(tipoServicio) < 1 or int(tipoServicio) > servicioMax:
                    print("INGRESE UN TIPOS DE SERVICIO VALIDO")
                    print("[1] => ECONOMICA")
                    print("[2] => EJECUTIVA")
                    print("[3] => PRIMERA CLASE")
                    tipoServicio = input("SELECCIONE EL TIPO DE SERVICIO: ")

                print("#############")
                print("DATOS CALCULADOS DEL CLIENTE CON RESPECTO AL SEVICIO")
        
            #CALCULO DE LOS DATOS A MOSTRAR CLIENTE TIPO-2
                if pasajes == '1':
                    descPasaje = 0
                elif '2' <= pasajes <= '5':
                    descPasaje = 0.05  
                elif '6' <= pasajes <= '10':
                    descPasaje = 0.12  
                else:
                    descPasaje = 0.15  

                if tipoServicio == '1':
                    costServicio = 70
                elif tipoServicio == '2':
                    costServicio = 140
                else:
                    costServicio = 280
                
                impBruto = int(pasajes)*costServicio
                montDesc = impBruto*descPasaje
                impNeto = impBruto - montDesc

                #INFO PARA EL REPORTE
                if impNeto>=70 and impNeto<=500:
                    ventasNeto = ventasNeto+1
                
                if genero == 'F' and (impNeto>=140 and impNeto<=1000):
                    ventasMujeres = ventasMujeres+1
                
                venTotales = venTotales + impNeto

                print(f"IMPORTE BRUTO: {impBruto}")
                print(f"MONTO DE DESCUENTO: {montDesc}")
                print(f"IMPORTE NETO: {impNeto}")

            elif tipClient == '3':
                break
            else:
                print("INGRESE UN TIPO DE CLIENTE VALIDO")


#TIPO DE OPERACION-2
    if operacion == '2':

    #RESULTADOS OBTENIDOS
        while True:
            print("---------------------------")
            print("### REPORTAR VENTAS ###")
            print("[1] INFORMACION RECOLECTADA")
            print("[2] VOLVER AL MENU")
            tipVentas = input("SELECCIONE LA OPCION:")

            if tipVentas == '1':
                #REPORTE DE LAS VENTAS
                hombresTotal = hombreOne +  hombreTwo
                promClientOne = impNeto/(hombreOne+mujerOne)
                print(f"TOTAL DE CLIENTES DE GENERO MASCULINO =>[{hombresTotal}]")
                print(f"CANTIDAD DE VENTAS MAYORES A 70 PERO MENORES A 500 =>[{ventasNeto}]")
                print(f"VENTAS DEL GENERO  FEMENINO MAYORES A 140 PERO MENORS A 1000 =>[{ventasMujeres}]")
                print(f"IMPORTE DE VENTAS TOTALES =>[{venTotales}]")
                print(f"IMPORTE TOTAL NETO DE CLIENTES TIPO [1] =>[{impClientOne}]")
                print(f"PROMEDIO DEL IMPORTE NETO DE CLIENTES TIPO [1] =>[{promClientOne}]")
            elif tipVentas == '2':
                break
            else:
                print("INGRESE UN TIPO DE CLIENTE VALIDO")


    elif operacion == '3':
        print("OPERACIONES TERMINADAS.")
        break  
    else:
        print("OPCION INVALIDA INGRESE UNA OPERACION A REALIZAR")
 