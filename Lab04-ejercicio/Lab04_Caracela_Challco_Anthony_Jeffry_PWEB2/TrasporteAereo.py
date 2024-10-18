# Definir la clase Cliente
class Cliente:
    def __init__(self, nombre, tipo_cliente, cantidad_pasajes, genero, tipo_servicio):
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente
        self.cantidad_pasajes = cantidad_pasajes
        self.genero = genero
        self.tipo_servicio = tipo_servicio
    
    def obtener_precio(self):
        # Precios según el tipo de servicio
        if self.tipo_servicio == 1:
            return 70.0  # Económica
        elif self.tipo_servicio == 2:
            return 140.0  # Ejecutiva
        elif self.tipo_servicio == 3:
            return 280.0  # Primera clase
        return 0.0

    def obtener_descuento(self):
        # Descuento según la cantidad de pasajes
        if self.cantidad_pasajes == 1:
            return 0.0
        elif 2 <= self.cantidad_pasajes <= 5:
            return 0.05  # 5%
        elif 6 <= self.cantidad_pasajes <= 10:
            return 0.12  # 12%
        elif self.cantidad_pasajes >= 11:
            return 0.15  # 15%
        return 0.0

    def calcular_importe_bruto(self):
        return self.cantidad_pasajes * self.obtener_precio()

    def calcular_monto_descuento(self):
        return self.calcular_importe_bruto() * self.obtener_descuento()

    def calcular_importe_neto(self):
        return self.calcular_importe_bruto() - self.calcular_monto_descuento()

# Lista para almacenar clientes
clientes = []

# Función para ingresar datos
def ingresar_datos():
    while True:
        nombre = input("Ingrese el nombre del titular: ")
        tipo_cliente = int(input("Ingrese el tipo de cliente (1 o 2): "))
        cantidad_pasajes = int(input("Ingrese la cantidad de pasajes: "))
        genero = input("Ingrese el género del cliente (M/F): ").upper()
        tipo_servicio = int(input("Ingrese el tipo de servicio (1-Económica, 2-Ejecutiva, 3-Primera clase): "))
        
        # Crear un nuevo objeto Cliente
        cliente = Cliente(nombre, tipo_cliente, cantidad_pasajes, genero, tipo_servicio)
        clientes.append(cliente)
        
        # Mostrar los resultados para el cliente
        print(f"Importe Bruto: {cliente.calcular_importe_bruto():.2f}")
        print(f"Monto de Descuento: {cliente.calcular_monto_descuento():.2f}")
        print(f"Importe Neto: {cliente.calcular_importe_neto():.2f}")
        
        # Preguntar si el usuario desea agregar otro cliente
        continuar = input("¿Desea agregar otro cliente? (s/n): ").lower()
        if continuar != 's':
            break

# Función para mostrar los resultados de ventas
def mostrar_resultados():
    total_ventas = 0
    total_clientes_masculinos = 0
    total_clientes_femeninos = 0
    ventas_rango_70_500 = 0
    ventas_femeninas_rango_140_1000 = 0
    acumulado_tipo_1 = 0
    total_importe_neto_tipo_1 = 0
    cantidad_tipo_1 = 0

    for cliente in clientes:
        importe_neto = cliente.calcular_importe_neto()
        total_ventas += importe_neto
        
        if cliente.genero == 'M':
            total_clientes_masculinos += 1
        
        if cliente.genero == 'F':
            total_clientes_femeninos += 1

        if 70 <= importe_neto <= 500:
            ventas_rango_70_500 += 1
        
        if cliente.genero == 'F' and 140 <= importe_neto <= 1000:
            ventas_femeninas_rango_140_1000 += 1
        
        if cliente.tipo_cliente == 1:
            acumulado_tipo_1 += importe_neto
            total_importe_neto_tipo_1 += 1
            cantidad_tipo_1 += 1

    print(f"Total de ventas: {total_ventas:.2f}")
    print(f"Cantidad de clientes masculinos: {total_clientes_masculinos}")
    print(f"Cantidad de clientes masculinos: {total_clientes_femeninos}") 
    print(f"Cantidad de ventas con importe neto entre 70 y 500: {ventas_rango_70_500}")
    print(f"Cantidad de ventas femeninas con importe neto entre 140 y 1000: {ventas_femeninas_rango_140_1000}")
    print(f"Acumulado de importe neto de clientes de tipo 1: {acumulado_tipo_1:.2f}")
    
    if cantidad_tipo_1 > 0:
        promedio_tipo_1 = acumulado_tipo_1 / cantidad_tipo_1
        print(f"Promedio de importe neto de clientes de tipo 1: {promedio_tipo_1:.2f}")
    else:
        print("No hay clientes de tipo 1.")

# Menú principal
print("Bienvenido al registro de Transporte Aéreo\nMENÚ DE OPCIONES")
while True:
    print("\n[1] Ingresar datos")
    print("[2] Ver resultados de ventas")
    print("[3] Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        ingresar_datos()
    elif opcion == '2':
        mostrar_resultados()
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
