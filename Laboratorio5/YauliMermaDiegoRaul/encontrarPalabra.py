import random

# Lista de palabras disponibles
palabras = ["abandonar", "abanico", "abisal", "abominar", "abracadabra", "abril", "abrojo", "abrupto", "abulia", "academia"]

# Selección aleatoria de la palabra
palabra = random.choice(palabras).lower()  # Convertimos la palabra a minúsculas

def reemplazar(palabra):
    """Función para reemplazar aleatoriamente letras de la palabra."""
    longitud = len(palabra)
    max_reemplazos = int(longitud * 0.6)  # Máximo 60% oculto
    reemplazos = 0 
    minimo = 0.3  # Probabilidad de ocultar cada letra
    
    nueva_palabra = []
    for c in palabra:
        if random.random() < minimo and reemplazos < max_reemplazos:
            nueva_palabra.append('_')
            reemplazos += 1
        else:
            nueva_palabra.append(c)
    
    return ''.join(nueva_palabra)

def mostrar_progreso(palabra_oculta):
    """Muestra el progreso actual de la palabra."""
    print("\nPalabra actual: " + ' '.join(palabra_oculta))

def jugar(palabra, intentos=6):
    """Función principal del juego."""
    palabra_oculta = list(reemplazar(palabra))  # Convierte en lista para modificar
    letras_adivinadas = set()  # Almacena letras ya intentadas
    ganado = False  # Variable de control
    print("\n¡Bienvenido al juego de adivinar la palabra!")
    mostrar_progreso(palabra_oculta)
    while intentos > 0 and not ganado:
        entrada = input("\nIngresa una letra o una palabra completa: ").strip().lower()

        if len(entrada) == 1:  # Entrada de una letra
            letra = entrada
            if letra in letras_adivinadas:
                print(f"Ya intentaste la letra '{letra}'. Prueba con otra.")
                continue
            letras_adivinadas.add(letra)
            if letra in palabra:
                print(f"¡Bien! La letra '{letra}' está en la palabra.")
                # Actualiza todas las ocurrencias de la letra
                for i, c in enumerate(palabra):
                    if c == letra:
                        palabra_oculta[i] = letra
            else:
                print(f"La letra '{letra}' no está en la palabra.")
                intentos -= 1
        elif len(entrada) == len(palabra):  # Adivinar la palabra completa
            if entrada == palabra:
                print("\nLo lograste, ves que facil es.")
                ganado = True  # Cambia el estado a ganado
            else:
                print("Palabra incorrecta.")
                intentos -= 1
        else:
            print("Entrada inválida. Ingresa una letra o una palabra con la longitud correcta.")
        mostrar_progreso(palabra_oculta)

        # Verifica si se adivinó toda la palabra
        if ''.join(palabra_oculta) == palabra:
            print("\nLo lograste, ves que facil es.")
            ganado = True
        print(f"Intentos restantes: {intentos}")
    if not ganado:
        print(f"\nTe quedaste sin intentos. La palabra era: {palabra}")
jugar(palabra)