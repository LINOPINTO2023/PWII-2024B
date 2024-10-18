def menu():
    print("MENU DE OPCIONES")
    print("INGRESAR DATOS DE VENTAS")
    print("VER RESULTADOS DE VENTAS")
    print("SALIR")

def main():
    print("Ingrese el Tipo de cliente: ")
    cliente = int(input()) 
    print("ingrese la cantidad de pasajes: ")
    pasajes = int(input())
    print("Ingrese el genero: ")
    genero = input()
# Para controlar la parte del código a ejecutar
if __name__ == "__main__":
    main()
