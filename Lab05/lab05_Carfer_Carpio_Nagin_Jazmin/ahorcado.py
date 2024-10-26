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
