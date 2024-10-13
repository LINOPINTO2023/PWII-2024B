from boleta import Boleta
from registro_ventas import RegistroVentas

# Función principal
def empresa_transporte():
    registro_ventas = RegistroVentas()
    while True:
        print("Seleccione una opción: ")
        print("1. Registrar venta de pasajes")
        print("2. Mostrar resultados")
        print("3. Salir")
        opcion = int(input())

        if opcion == 1:
            # Ingreso y validación de datos
            tipo_cliente = int(input("Ingrese el tipo de cliente (1 o 2): "))
            while tipo_cliente not in [1, 2]:
                tipo_cliente = int(input("Tipo de cliente inválido. Ingrese el tipo de cliente (1 o 2): "))

            cantidad_pasajes = int(input("Ingrese la cantidad de pasajes: "))
            while cantidad_pasajes <= 0:
                cantidad_pasajes = int(input("Cantidad de pasajes inválida. Ingrese la cantidad de pasajes: "))

            genero_cliente = input("Ingrese el género del cliente (M/m/F/f): ").lower()
            while genero_cliente not in ['m', 'f']:
                genero_cliente = input("Género inválido. Ingrese el género del cliente (M/m/F/f): ").lower()

            tipo_servicio = int(input("Ingrese el tipo de servicio (1-Económica, 2-Ejecutiva, 3-Primera clase): "))
            while tipo_servicio not in [1, 2, 3]:
                tipo_servicio = int(input("Tipo de servicio inválido. Ingrese el tipo de servicio (1-Económica, 2-Ejecutiva, 3-Primera clase): "))

            # Crear boleta y añadir al registro
            boleta = Boleta(tipo_cliente, cantidad_pasajes, genero_cliente, tipo_servicio)
            registro_ventas.registrar_boleta(boleta)

            # Mostrar la boleta del cliente
            boleta.mostrar_boleta()

        elif opcion == 2:
            # Mostrar resultados
            registro_ventas.mostrar_resultados()

        elif opcion == 3:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    empresa_transporte()

