contador = 0
contadorm = 0
contadorf = 0
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
         
         
            if list1[0] == 1:
                contador += cantidadp  
            else:
                if list1[2] == "m":
                    contadorm += cantidadp
                elif list1[2] == "f":
                    contadorf += cantidadp

    
            if list1[3] == 1:
                economico = 70
                importe_Bruto = cantidadp * economico
            elif list1[3] == 2:
                ejecutivo = 140
                importe_Bruto = cantidadp * ejecutivo
            elif list1[3] == 3:
                primera_Clase = 280
                importe_Bruto = cantidadp * primera_Clase

         
            if 2 <= list1[1] <= 5:
                desc = importe_Bruto * 0.05
            elif 6 <= list1[1] <= 10:
                desc = importe_Bruto * 0.12
            elif list1[1] >= 11:
                desc = importe_Bruto * 0.15
            else:
                desc = 0

            importe_neto = importe_Bruto - desc

            print(f"El importe bruto es: {importe_Bruto}")
            print(f"El monto de descuento es: {desc}")
            print(f"El importe neto es: {importe_neto}")

        case 2:
            # Opción 2
            print(f"Ventas registradas:\n- Pasajes masculinos: {contadorm}\n- Pasajes femeninos: {contadorf}")
        case 3:
            do = False