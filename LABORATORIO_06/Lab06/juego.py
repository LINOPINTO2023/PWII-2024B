import random

#PALABRAS PARA EL JUEGO 
PALABRAS = ["europa", "programacion", "arequipa", "ceviche", "computadora", "latinoamerica", "pisco"]

#Ocultar ciertas letras de una palabra
def ocultar(palabra):
    ocultas = int(len(palabra) * 0.6)
    indices = random.sample(range(len(palabra)), ocultas)
    palabra_inicial = list(palabra)

    for i in indices:
        palabra_inicial[i] = "_"
    
    
    return ''.join(palabra_inicial)

#Verificar si el intento es correcto o incorrecto
def intento(palabra, entrada):
    if(len(entrada) == 1):
        return entrada in palabra
    if(len(entrada) == len(palabra)):
        return entrada == palabra
    return False

#ejemplo
palabra_seleccionada = random.choice(PALABRAS)
palabra_oculta = ocultar(palabra_seleccionada)
    
print("Palabra oculta:", palabra_oculta)

while True:
    entrada = input("Adivina una letra o la palabra completa: ")
    
    if intento(palabra_seleccionada, entrada):
        print("¡Correcto!")
        if entrada == palabra_seleccionada:
            print("¡Has adivinado la palabra! Era:", palabra_seleccionada)
            break
    else:
        print("Incorrecto. Intenta de nuevo.")
