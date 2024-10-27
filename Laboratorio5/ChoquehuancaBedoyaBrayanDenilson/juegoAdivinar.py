import random
import math

# Palabras para ser adivinadas
palabrasDisponibles = ["INGENIERIA", "SISTEMAS", "PROGRAMACION"]

# Número máximo de intentos
intentosDisponibles = 5

# Escoger de forma aleatoria la palabra a adivinar
palabraAdivinar = random.choice(palabrasDisponibles)

# Inicializar la palabra oculta globalmente para poder actualizarla en cada intento
palabraAdivinarOculta = ""

# Quitar algunas letras de la palabra
def prepararPalabraOculta():
    global palabraAdivinarOculta

    # Ocultaremos aleatoriamente hasta un 60% de la palabra, redondeando al número mayor
    cantidadMaxOcultar = math.ceil(0.6 * len(palabraAdivinar))

    # Se crea una lista con las posiciones en la palabra que serán ocultadas
    posicionesParaOcultar = random.sample(range(len(palabraAdivinar)), cantidadMaxOcultar)

    # Crea una lista de caracteres de la palabra a adivinar
    palabraAdivinarLista = list(palabraAdivinar)

    # Convierte en "_" las posiciones a ocultar
    for pos in posicionesParaOcultar:
        palabraAdivinarLista[pos] = "_"

    # Crear un string con la lista de la palabra con "_"
    palabraAdivinarOculta = "".join(palabraAdivinarLista)

# Preparar la palabra inicial
prepararPalabraOculta()

# Bucle principal del juego
while intentosDisponibles > 0:
    print(f"\nPalabra a adivinar: {palabraAdivinarOculta}")
    print(f"Intentos restantes: {intentosDisponibles}")

    # Solicitar al usuario que introduzca una letra o la palabra completa
    intentoUsuario = input("Introduce una letra o la palabra completa: ").upper()

    # Validar si el intento es una palabra completa
    if len(intentoUsuario) == len(palabraAdivinar):
        if intentoUsuario == palabraAdivinar:
            print(f"¡Felicidades! Has adivinado la palabra: {palabraAdivinar}")
            break
        else:
            print("Palabra incorrecta.")
            intentosDisponibles -= 1

    # Si el intento es una letra única
    elif len(intentoUsuario) == 1:
        letra = intentoUsuario
        if letra in palabraAdivinar:
            # Actualizar la palabra oculta con la letra acertada
            palabraAdivinarOculta = "".join([
                letra if palabraAdivinar[i] == letra else palabraAdivinarOculta[i]
                for i in range(len(palabraAdivinar))
            ])
            print(f"¡Correcto! La letra '{letra}' está en la palabra.")
            # Si no hay más "_" en palabraAdivinarOculta, se ha ganado el juego
            if "_" not in palabraAdivinarOculta:
                print(f"¡Felicidades! Has completado la palabra: {palabraAdivinarOculta}")
                break
        else:
            print(f"La letra '{letra}' no está en la palabra.")
            intentosDisponibles -= 1

    # Si el intento no cumple con ninguna de las condiciones anteriores
    else:
        print("Entrada no válida. Debes introducir una sola letra o intentar resolver la palabra completa.")

    # Verificar si se acabaron los intentos
    if intentosDisponibles == 0:
        print(f"Te has quedado sin intentos. La palabra era: {palabraAdivinar}")
        break
