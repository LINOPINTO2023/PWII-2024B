#Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#• El juego comienza proponiendo una palabra aleatoria incompleta. Por ejemplo "m_ur_d_v", y el
#número de intentos que le quedan
#• El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que la palabra
#a adivinar)
#• Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta uno al número de
#intentos
#• Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno al número de
#intentos
#• Si el contador de intentos llega a 0, el jugador pierde
#• La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
#• Puedes utilizar las palabras que quieras y el número de intentos que consideres
import random

# Funcion para iniciar el juego
def iniciarJuego():
    palabra, palabraOculta = generarPalabra()
    intentos = 3
    print("ADIVINA LA PALABRA")
    print(f"Tu palabra es: {palabraOculta}")
    print(f"Tienes {intentos} intentos.")
    
    while intentos > 0:
        intento = input("Introduce una letra o una palabra: ")

        if len(intento) == 1:  
            if intento in palabra:
                palabraOculta = actualizarPalabra(palabra, palabraOculta, intento)
                print("¡Has adivinido una letra!")
            else:
                intentos -= 1
                print("Letra incorrecta.")
        elif len(intento) == len(palabra):  
            if intento == palabra:
                print ("¡Felicidades! Has adivinado la palabra.")
                return
            else:
                intentos -= 1
                print("Palabra incorrecta.")
        else:
            print("Entrada inválida. Introduce una letra o una palabra completa.")

        print(f"Tu palabra es: {palabraOculta}")
        print(f"Te quedan {intentos} intentos")

    print("¡GAME OVER! No te quedan intentos, la palabra era:", palabra)    
    
# Generamos una palabra random de una lista y se oculta no mas del 60% de la palabra    
def generarPalabra():
    palabras = ["carpintero", "factura", "rinoceronte", "camiseta", "cerradura", "plumero"]
    palabra = random.choice(palabras)
    
    palabraOculta = list(palabra)
    cantLetOcultas = random.randint(1, int(len(palabra) * 0.6))    
    letOcultas = random.sample(range(len(palabra)), cantLetOcultas)
    for i in letOcultas:
        palabraOculta[i] = "_"
    return palabra, "".join(palabraOculta)

# La funcion actualiza nuestra palabra oculta mostrando la letra adivinada
def actualizarPalabra(palabra, palabraOculta, letra):
    palabraOculta = list(palabraOculta)
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabraOculta[i] = letra
    return "".join(palabraOculta)

# Llamamos a iniciar el juego
iniciarJuego()
