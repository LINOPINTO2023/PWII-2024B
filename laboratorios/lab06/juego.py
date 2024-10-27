import random

def ocultar_palabra(palabra):
    # Oculta de forma aleatoria algunas letras de la palabra, sin ocultar la primera letra
    palabra_oculta = [letra if i == 0 else "_" for i, letra in enumerate(palabra)]
    indices = [i for i in range(1, len(palabra)) if palabra_oculta[i] == "_"]
    letras_a_ocultar = random.sample(indices, k=len(indices)//2)  # Oculta la mitad de las letras
    
    for i in letras_a_ocultar:
        palabra_oculta[i] = palabra[i]
    
    return ''.join(palabra_oculta)

def juego_adivina_palabra():
    palabras = ["papaya", "fresa", "sandia", "durazno", "mandarina","pera"]#podemos cambiar las palabras que deseamos
    palabra = random.choice(palabras)
    palabra_oculta = ocultar_palabra(palabra)
    intentos = 5

    print("¡Bienvenido al juego de adivinar la palabra!")
    print(f"Tienes {intentos} intentos para adivinar la palabra.")
    print(f"Palabra a adivinar: {palabra_oculta}")

    while intentos > 0:
        intento = input("Introduce una letra o intenta adivinar la palabra: ").lower()

        if len(intento) == 1:  # Intento con una letra
            if intento in palabra:
                palabra_oculta = "".join([intento if palabra[i] == intento else palabra_oculta[i] for i in range(len(palabra))])
                print(f"¡Acertaste una letra! {palabra_oculta}")
            else:
                intentos -= 1
                print(f"Letra incorrecta. Te quedan {intentos} intentos.")
        elif len(intento) == len(palabra):  # Intento de resolver la palabra
            if intento == palabra:
                print("¡Felicidades! Adivinaste la palabra correctamente.")
                return
            else:
                intentos -= 1
                print(f"Palabra incorrecta. Te quedan {intentos} intentos.")
        else:
            print("Entrada no válida. Debe ser una letra o una palabra completa.")

        if "_" not in palabra_oculta:
            print("¡Felicidades! Completaste la palabra correctamente.")
            return

    print(f"Lo siento, te has quedado sin intentos. La palabra era '{palabra}'.")

# Ejecuta el juego
juego_adivina_palabra()
