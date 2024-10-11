#Contador de la cantidad de pasajes
contador = 0
#Contador masculino y femenino
contadorm = 0
contadorf = 0
#Ventas con rango uno general y otro para clientes femeninos
ventas_rango_general = 0
ventas_rango_femenino = 0
#importe bruto e importe neto
acumulado_importe_bruto = 0
acumulado_importe_neto = 0
#tipo1
acumulado_importe_tipo1 = 0
contador_tipo1 = 0
do = True
while do: 
    print("Empresa de Transporte aéreo")
    print("[1]Registrar venta de pasaje")
    print("[2]Reportar ventas")
    print("[3]Salir")
    opcion = int(input("¿Qué opción vas a elegir?"))
    match opcion:
        case 1:
            while True:
                tipoc = int(input("¿Cuál tipo de cliente eres? 1 o 2: "))
                cantidadp = int(input("¿Cantidad de pasajes? "))
                Genero = input("¿Eres Masculino(m) o Femenino(f)? ").lower()
                serviciot = int(input("¿Tipo de servicio? ([1]-Económica / [2]-Ejecutiva / [3]-Primera clase): "))
                list1 = [tipoc, cantidadp, Genero, serviciot]
                print(list1)
                
                if list1[1] <= 0:
                    print("La cantidad de pasajes no puede ser 0.")
                    continue
                
                if list1[2] != "m" and list1[2] != "f":
                    print("Solo puede ser Masculino (m) o Femenino (f).")
                    continue
                

                if list1[3] != 1 and list1[3] != 2 and list1[3] != 3:
                    print("Solo puede elegir entre las tres opciones del [1, 3].")
                    continue
                else:
                    break
         
            if list1[2] == "m":
                contadorm += 1  
            elif list1[2] == "f":
                contadorf += 1  
            
            contador += cantidadp
    
            if list1[3] == 1:
                economico = 70
                importe_Bruto = cantidadp * economico
            elif list1[3] == 2:
                ejecutivo = 140
                importe_Bruto = cantidadp * ejecutivo
            elif list1[3] == 3:
                primera_Clase = 280
                importe_Bruto = cantidadp * primera_Clase
            
            acumulado_importe_bruto += importe_Bruto
         
            if 2 <= list1[1] <= 5:
                desc = importe_Bruto * 0.05
            elif 6 <= list1[1] <= 10:
                desc = importe_Bruto * 0.12
            elif list1[1] >= 11:
                desc = importe_Bruto * 0.15
            else:
                desc = 0

            importe_neto = importe_Bruto - desc
            acumulado_importe_neto += importe_neto
            
            if 70 <= importe_neto <= 500:
                ventas_rango_general += 1
            if list1[2] == "f" and 140 <= importe_neto <= 1000:
                ventas_rango_femenino += 1

            if list1[0] == 1:
                acumulado_importe_tipo1 += importe_neto
                contador_tipo1 += 1  


            print("El importe bruto es: " + str(importe_Bruto))
            print("El monto de descuento es: " +  str(desc))
            print("El importe neto es: " + str(importe_neto))   

        case 2:
            # Opción 2
            print("Ventas registradas:")
            print("- Cantidad de clientes masculinos: " + str(contadorm))
            print("- Ventas cuyo Importe Neto sea >=70 y <=500: " + str(ventas_rango_general) )
            print("- Ventas de clientes femeninos cuyo Importe Neto sea >=140 y <=1000: " + str(ventas_rango_femenino))
            print("- Acumulado del Importe de Ventas (Bruto): " +  str(acumulado_importe_bruto))
            print("- Acumulado del Importe Neto de clientes de tipo 1: " + str(acumulado_importe_tipo1) )  
            promedio_tipo1 = acumulado_importe_tipo1 / contador_tipo1
            print("- Promedio de Importe Neto de clientes de tipo 1:" + str(promedio_tipo1))
        case 3:
            do = False