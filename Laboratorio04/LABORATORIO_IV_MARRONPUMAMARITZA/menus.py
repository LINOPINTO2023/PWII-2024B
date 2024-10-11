
ventas=[]
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    opcion = input('Opción: ')
    while opcion not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
        opcion = input('Opción: ')
    return opcion

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones,opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()
    

def menu_principal():
    opciones = {
        '1': ('Registrar venta de pasaje', accion1),
        '2': ('Reportar ventas', accion2),
        '3': ('Salir',salir),
    }
    generar_menu(opciones,'3')
    
def accion1():
    print('Has elegido la opción 2')
    tipocliente = 0
    while tipocliente not in [1,2]:
        print("Tipo de cliente:")
        print("1")
        print("2")
        tipocliente = int(input("Ingrese el tipo de cliente (1 o 2): "))
        
    cantpasajes = 0
    while cantpasajes <= 0:
        cantpasajes = int(input("Ingrese la cantidad de pasajes: "))
    
    genero = ''
    while genero not in ['M' , 'F']:
        genero = input("Ingrese el genero del cliente(M  o F)").upper()
        
    tiposervice = 0
    while tiposervice not in [1,2,3,]:
        print("Tipo de servicio: ")
        print("1 - Economica")
        print("2 - Ejecutiva")
        print("3 - Primera clase")
        tiposervice = int(input("Ingrese el tipo de servicio (1,2,3): "))
    if tiposervice ==1:
        preciopasaje = 70.00
    elif tiposervice ==2:
        preciopasaje = 140.00
    elif tiposervice ==3:
        preciopasaje = 280.00
        
    if cantpasajes ==1:
        descuento = 0
    elif 2 <= cantpasajes <=5:
        descuento =  0.05
    elif 6 <= cantpasajes <=10:
        descuento = 0.12
    else:
        descuento = 0.15
    
    importbruto = cantpasajes*preciopasaje
    montodescuento = importbruto* descuento
    importeNeto = importbruto - montodescuento
    
    venta = {
        'tipocliente': tipocliente,
        'genero':genero,
        'importeNeto': importeNeto,
        'tiposervicio': tiposervice
    }
    ventas.append(venta)
    print(f"\n=========----------------------------------------Resumen del proceso---------------------------------================")
    print(f"Tipo de cliente: {'Regular' if tipocliente == 1 else 'Frecuente'} ")   
    print(f"Cantidad de pasajes: {cantpasajes}")
    print(f"Genero del cliente: {'Masculino' if genero =='M' else 'Femenino'}")  
    print(f"Tipo de servicio: {'Economico' if tiposervice == 1 else 'Ejecutivo' if tiposervice == 2 else 'Primera clase'}")
    print(f"El importe Bruto es: S/{importbruto:.2f})")
    print(f"El monto de descuento es: S/{montodescuento:.2f}({descuento * 100}% de descuento)")
    print(f"Importe Neto: S/{importeNeto:.2f}")
     
def accion2():
    print('Has elegido la opción 2')
    cantidadMasculino=0
    ventasImporteRango=0
    ventasFemeninoImporteRango =0
    acumuladoImporteVentas =0
    acumuladoImporteNetoTipo1 = 0
    cantidadTipo1 = 0
    for venta in ventas:
        if venta['genero'] == 'M':
            cantidadMasculino +=1
            
        if 70 <= venta['importeNeto'] <=500:
            ventasImporteRango +=1
        
        if venta['genero']=='F' and 140 <= venta ['importeNeto'] <=1000:
            ventasFemeninoImporteRango +=1
        acumuladoImporteVentas += venta['importeNeto']
        if venta['tipocliente']==1:
            acumuladoImporteNetoTipo1 += venta['importeNeto']
            cantidadTipo1 += 1
    if cantidadTipo1 > 0 :
        promedioImporteNetoTipo1 = acumuladoImporteNetoTipo1 / cantidadTipo1
    else:
        promedioImporteNetoTipo1 = 0
    print("\nReporte de ventas")
    print(f"Clientes masculinos: {cantidadMasculino}")
    print(f"Ventas entre S/ 70 y S/ 500: {ventasImporteRango}")
    print(f"Ventas femeninas entre S/140 y S/1000:{ventasFemeninoImporteRango}")
    print(f"Importe total de ventas: S/{acumuladoImporteVentas:.2f}")
    print(f"Importe Neto total de clientes tipo 1: S/{acumuladoImporteNetoTipo1:.2f}")
    print(f"Promedio de Importe Neto de clientes tipo 1: S/{promedioImporteNetoTipo1:.2f}")

    

def salir():
    print('Saliendo...')


if __name__ == '__main__':
    menu_principal()