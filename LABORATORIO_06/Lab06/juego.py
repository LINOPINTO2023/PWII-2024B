import random

#PALABRAS PARA EL JUEGO 
PALABRAS = {"europa", "programacion", "arequipa", "ceviche", "computadora", "latinoamerica", "pisco"}

def ocultar(palabra):
    ocultas = int(len(palabra) * 0.6)
    indices = random.sample(range(len(palabra)), ocultas)
    palabra_inicial = list(palabra)

    for i in indices:
        palabra_inicial[i] = "_"
    
    return ''.join(palabra_inicial)

# Ejemplo de uso
palabra_seleccionada = random.choice(PALABRAS)
resultado = ocultar(palabra_seleccionada)
print("Palabra oculta:", resultado)