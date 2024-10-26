# -*- coding: utf-8 -*-
import random
#Las palabras que se adivinaran
listapalabras = ['elefante', 'lapicero', 'hormiga', 'gallina', 'ave', 'antro', 'azul', 'piña',
           'caracol', 'raton', 'gorila', 'peaton', 'tenedor', 'pintura', 'blanco',
           'iguana', 'leon', 'gato', 'gallo', 'comida', 'televisor', 'papel', 'lonchera']
def generadorLetrasVisibles(palabra):
    # Aqui calculamos cuántas letras se deben mostrar, no más del 40%
    letrasTotal = len(palabra)
    maximoVisible = int(letrasTotal * 0.4)
    cantidadMostrar = random.randint(1, maximoVisible)
    
    # Seleccionamos posiciones aleatorias para mostrar
    posiciones = random.sample(range(letrasTotal), cantidadMostrar)
    # Construye la palabra oculta
    palabraOculta = list('_' * letrasTotal)
    for posicion in posiciones:
        palabraOculta[posicion] = palabra[posicion]
    
    return ''.join(palabraOculta)

def iniciarJuego():
    # Se selecciona una palabra aleatoria
    palabraSeleccionada = listapalabras[random.randint(0, len(listapalabras) - 1)]
    intentosMaximos = 7
    intentosRestantes = intentosMaximos
    
    # Se genera la palabra parcialmente oculta
    palabraOculta = generadorLetrasVisibles(palabraSeleccionada)
    letrasVisibles = list(palabraOculta)
    
    mostrarIntroduccion()
    print(f"\nTe quedan {intentosRestantes} intentos")
    print(f"Palabra a adivinar: {palabraOculta}")
    
    while intentosRestantes > 0:
        intento = input('Ingresa una letra o intenta adivinar la palabra completa: ').lower()
        
        # Aqui verificamos si es una letra única o una palabra completa
        if len(intento) == 1:  # Es una letra
            if intento in palabraSeleccionada:
                # Aqui actualiza todas las ocurrencias de la letra
                letraAcertada = False
                for i in range(len(palabraSeleccionada)):
                    if palabraSeleccionada[i] == intento and letrasVisibles[i] == '_':
                        letrasVisibles[i] = intento
                        letraAcertada = True
                
                if not letraAcertada:
                    print("Esa letra ya estaba descubierta!")
                    intentosRestantes -= 1
            else:
                print("Letra incorrecta!")
                intentosRestantes -= 1
                
        else:  #  si es un intento de palabra completa
            if intento == palabraSeleccionada:
                mostrarFelicitacion(palabraSeleccionada)
                return
            else:
                print("Palabra incorrecta!")
                intentosRestantes -= 1
        
        # Muestra el estado actual
        print(f"\nTe quedan {intentosRestantes} intentos")
        dibujarMuñeco(intentosMaximos - intentosRestantes - 1)
        print(''.join(letrasVisibles))
        
        # Verifica si ganó
        if '_' not in letrasVisibles:
            mostrarFelicitacion(palabraSeleccionada)
            return
    
    # Si llega aquí perdió
    print(f"\n¡Juego Terminado! La palabra era: {palabraSeleccionada}")


def mostrarIntroduccion():
    print("----------AHORCADO----------")

def mostrarFelicitacion(palabra):
    print("*****FELICIDADES*****")
    print(f"¡Tu palabra es: {palabra}!")

def dibujarMuñeco(posicion):
    partesCuerpo = [
        '0',
        '/', '|', '\\',
             '|',
        '/', '\\'
    ]
    secciones = [
        '\n\t+--------+\n\t|\t |\n',
        '\n=========\n'
    ]
    cuerpo = ''
    for i in range(len(partesCuerpo)):
        if i <= posicion and posicion >= 0:
            if i == 0:
                cuerpo = '\t|\t ' + partesCuerpo[i]
            elif i > 0 and i < 4:
                if i == 1:
                    cuerpo = cuerpo + "\n\t|\t"
                cuerpo = cuerpo + partesCuerpo[i]
            elif i == 4:
                cuerpo = cuerpo + '|\t ' + partesCuerpo[i] + '\n\t|\t'
            elif i > 4:
                cuerpo = cuerpo + partesCuerpo[i] + " "

            if i > 2 and i < 4:
                cuerpo = cuerpo + '\n\t'
        else:
            if i > 0:
                cuerpo += "\n"
            cuerpo = cuerpo + '\t|\t'
    cuerpo = secciones[0] + cuerpo + secciones[1]
    print(cuerpo)

if __name__ == "__main__":
    iniciarJuego()
