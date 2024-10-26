import random

# Lista de palabras 
palabras = ["algoritmo", "codigo", "programa", "hardware", "software", "redes", "base", "datos", "bug", "compilador"]

#Funcion para ocultar las letras 
def ocultar_letras(palabra):
    num_letras = len(palabra)
    max_ocultas = int(num_letras * 0.6)  # Máximo 60% de letras ocultas
    indices_ocultos = random.sample(range(num_letras), max_ocultas)  # Elegimos qué letras ocultar