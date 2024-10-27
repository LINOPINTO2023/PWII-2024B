import random

palabras = ["encapsulation", "polymorphism", "asynchronous", "inheritance", "abstraction", "multithreading", "serialization"]


def ocultar_palabra(palabra):
    num_letras_a_ocultar = int(len(palabra) * 0.6)
    letras_a_ocultar = random.sample(range(len(palabra)), num_letras_a_ocultar)
    palabra_oculta = ''.join('_' if i in letras_a_ocultar else letra for i, letra in enumerate(palabra))
    return palabra_oculta

def jugar_adivinar_palabra():
    palabra_original = random.choice(palabras)
    palabra_actual = ocultar_palabra(palabra_original)
    intentos = 5  

    print("Bienvenido a este juego en el debes de adivinar palabras.")
    print("Palabra por adivinar:")
    print(f"Palabra: {palabra_actual}")
    print(f"Tienes {intentos} intentos.")

    while intentos > 0:
        intento = input("Introduce una letra o intenta adivinar la palabra: ")

        # Si el jugador introduce una palabra completa
        if len(intento) == len(palabra_original):
            if intento == palabra_original:
                print("¡BIEN HECHO! Adivinaste la palabra.")
                return
            else:
                intentos -= 1
                print("UPS, no es la palabra. Inténtalo de nuevo.")
