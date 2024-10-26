import random

#PALABRAS PARA EL JUEGO 
PALABRAS = ["europa", "programacion", "arequipa", "ceviche", "computadora", "latinoamerica", "pisco"]

#Ocultar ciertas letras de una palabra
def ocultar(palabra):
    ocultas = int(len(palabra) * 0.6)
    indices = random.sample(range(len(palabra)), ocultas)
    palabra_mostrada = list(palabra)

    for i in indices:
        palabra_mostrada[i] = "_"
    
    
    return ''.join(palabra_mostrada)

#Verificar si el intento es correcto o incorrecto
def intento(palabra, entrada):
    if(len(entrada) == 1):
        return entrada in palabra
    if(len(entrada) == len(palabra)):
        return entrada == palabra
    return False

#Actualizar la palabra mostrada con la letra ingresada
def actualizar(palabra, palabra_mostrada, entrada):
    nueva_palabraM = ''
    for letra in palabra:
        if letra == entrada or letra in palabra_mostrada:
            nueva_palabraM += letra
        else:
            nueva_palabraM += '_'
    return nueva_palabraM


#ejemplo
palabra_seleccionada = random.choice(PALABRAS)
palabra_oculta = ocultar(palabra_seleccionada)
    
print("Palabra oculta:", palabra_oculta)

while True:
    entrada = input("Adivina una letra o la palabra completa: ")
    
    if intento(palabra_seleccionada, entrada):
        print("¡Correcto!")
        palabra_oculta = actualizar(palabra_seleccionada, palabra_oculta, entrada)
        print(palabra_oculta)
        if entrada == palabra_seleccionada:
            print("¡Has adivinado la palabra! Era:", palabra_seleccionada)
            break
    else:
        print("Incorrecto. Intenta de nuevo.")
