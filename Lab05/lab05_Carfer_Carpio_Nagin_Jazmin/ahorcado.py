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
