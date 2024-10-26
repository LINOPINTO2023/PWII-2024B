import random

# Lista de palabras 
palabras = ["algoritmo", "codigo", "programa", "hardware", "software", "redes", "base", "datos", "bug", "compilador"]

#Funcion para ocultar las letras 
def ocultar_letras(palabra):
    num_letras = len(palabra)
    max_ocultas = int(num_letras * 0.6)  # Máximo 60% de letras ocultas
    indices_ocultos = random.sample(range(num_letras), max_ocultas)  # Elegimos qué letras ocultar
    
    # Ocultar las letras seleccionadas
    palabra_oculta = ""
    for i, letra in enumerate(palabra):
        if i in indices_ocultos:
            palabra_oculta += "_"
        else:
            palabra_oculta += letra
    return palabra_oculta

def juego():
    palabra_original = random.choice(palabras)  # Elegir una palabra al azar
    palabra_actual = ocultar_letras(palabra_original)  # Ocultamos letras
    
    intentos = 5  # Número de intentos
    print(f"Palabra a adivinar: {palabra_actual}")
    
    while intentos > 0 and "_" in palabra_actual:
        intento = input(f"Tienes {intentos} intentos. Introduce una letra o la palabra completa: ").lower()

        # Verificar que la longitud sea válida 
        if len(intento) == 1 or len(intento) == len(palabra_original):
            # Si adivina la palabra completa
            if intento == palabra_original:  
                print(f"¡Felicidades! Adivinaste la palabra: {palabra_original}")
                return
            
            # Si introduce una letra correcta
            elif len(intento) == 1 and intento in palabra_original:  
                nueva_palabra = ""  
                for i in range(len(palabra_original)):
                    if palabra_original[i] == intento:
                        nueva_palabra += intento  # Agregar la letra correcta
                    else:
                        nueva_palabra += palabra_actual[i]  # Mantener la letra oculta o ya revelada
                palabra_actual = nueva_palabra  
                print(f"¡Acertaste! Palabra actual: {palabra_actual}")

            # Si la letra es incorrecta o adivina mal la palabra
            else:  
                intentos -= 1
                print(f"Intento incorrecto. Te quedan {intentos} intentos.")
        else:
            print(f"Entrada inválida. Debes introducir una letra o una palabra de {len(palabra_original)} letras.")
    
    print(f"{'¡Ganaste!' if '_' not in palabra_actual else 'Perdiste.'} La palabra era: {palabra_original}")

# Inicializacion del juego
juego()
