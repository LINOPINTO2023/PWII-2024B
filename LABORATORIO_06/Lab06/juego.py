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

#actulizar al realizar un intento (actulizar el num de intentos o actulizar la palabra oculta)
def intentos(palabra, palabra_mostrada, intentos, entrada):
    if intento(palabra, entrada):
        palabra_mostrada = actualizar(palabra, palabra_mostrada, entrada)
        print("¡Correcto!")
        print(palabra_mostrada)
    else:
        intentos -= 1
        print("Intento Incorrecto")
    return palabra_mostrada, intentos

#mostrar la palabra oculta y el numero de intentos que se tiene
def mostrar(palabra_mostrada, intentos):
    print(f"PALABRA --> {palabra_mostrada}")
    print(f"INTENTOS --> {intentos}")


def jugar():
    palabra = random.choice(PALABRAS)
    palabra_mostrada = ocultar(palabra)
    intentos = 7

    print("BIENVENIDO JUGARDO")
    print(f"TIENES {intentos} INTENTOS PARA ADIVINAR LA PALABRA")
    mostrar(palabra_mostrada, intentos)

    while intentos > 0:
        entrada = input("INGRESE UNA LETRA O PALABRA --> ").strip().lower()
        palabra_mostrada, intentos = intentos(palabra, palabra_mostrada, intentos, entrada)

        if palabra_mostrada == palabra:
            print("FELICIDADES JUGADOR ----- ADIVINASTE LA PALABRA")
        
        mostrar(palabra_mostrada, intentos)
    
    if intentos == 0:
        print("GAME OVER")
        print(f"LA PALABRA ERA ---> {palabra}")

if __name__ == "__main__":
    jugar()
