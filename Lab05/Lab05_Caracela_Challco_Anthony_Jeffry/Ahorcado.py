import random

# Lista de palabras para el juego
palabras = ["murcielago", "elefante", "computadora", "desarrollo", "programacion"]

# Selección de una palabra aleatoria y configuración de la palabra incompleta
def crear_palabra_incompleta(palabra):
    letras_ocultas = random.sample(range(len(palabra)), k=int(len(palabra) * 0.4))  # Máximo 40% de letras ocultas
    incompleta = ''.join('_' if i in letras_ocultas else letra for i, letra in enumerate(palabra))
    return incompleta

# Juego principal
def juego_adivinanza():
    palabra = random.choice(palabras)
    palabra_incompleta = crear_palabra_incompleta(palabra)
    intentos = 6  # Número de intentos

    print("¡Bienvenido al juego de adivinar palabras!")
    print(f"Adivina la palabra: {palabra_incompleta}")
    print(f"Tienes {intentos} intentos.")

    while intentos > 0:
        entrada = input("Ingresa una letra o la palabra completa: ").lower()

        if len(entrada) == 1:  # Si es una letra
            if entrada in palabra:
                palabra_incompleta = ''.join(entrada if palabra[i] == entrada else palabra_incompleta[i] for i in range(len(palabra)))
                print(f"¡Bien hecho! La palabra ahora es: {palabra_incompleta}")
            else:
                intentos -= 1
                print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        elif len(entrada) == len(palabra):  # Si intenta adivinar la palabra completa
            if entrada == palabra:
                print("¡Felicidades, has adivinado la palabra!")
                return
            else:
                intentos -= 1
                print(f"Palabra incorrecta. Te quedan {intentos} intentos.")
        
        else:
            print("Entrada no válida. Ingresa una letra o una palabra del tamaño correcto.")

        # Verificar si la palabra está completa
        if palabra_incompleta == palabra:
            print("¡Felicidades, has completado la palabra!")
            return

    print(f"Lo siento, te has quedado sin intentos. La palabra era: {palabra}")

# Ejecutar el juego
juego_adivinanza()

