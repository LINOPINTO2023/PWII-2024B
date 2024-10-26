import random

palabras = [
    "elefante",
    "murcielago",
    "aeropuerto",
    "estudiante",
    "mariposa",
    "guitarra",
    "ventilador",
    "computadora",
    "jardineria",
    "caminante",
    "abrelatas",
    "biblioteca",
    "universidad",
    "constructor",
    "calendario"
]
#Escogemos de manera aleatoria una palabra del array
numRand = random.randint(0, len(palabras)-1)
palabraEscogida = palabras[numRand]
#Hacemos una lista que almacena la palabra escogida
palabraOculta = list(palabraEscogida)
#Escogemos de manera aleatorias las letras que ocultaremos
longMitadPalabra = len(palabraEscogida)//2
#Hacemos un bucle for que nos almacenará todas las posiciones de letras a ocultar
posLetras = []
for i in range(longMitadPalabra):
    numRand = random.randint(0, len(palabraEscogida) - 1)
    while True:
        if numRand not in posLetras:
            posLetras.append(numRand)
            break
        else:
            numRand = random.randint(0, len(palabraEscogida) - 1)
#Hacemos un bucle for que reemplazará cada caracter por "_"
for i in posLetras:
    palabraOculta[i] = "_"
palabraOculta = "".join(palabraOculta)
print(palabraOculta)
#Pedimos al usuario que ingrese una letra o la palabra completa a adivinar
usuarioInput = input("Ingrese la letra o palabra completa: ")
#Si introduce la palabra completa
if len(usuarioInput) > 1 and usuarioInput == palabraEscogida:
    print("Palabra correcta, ganaste")
#Si solo introduce una letra
elif len(usuarioInput) == 1:
    for i in palabraEscogida:
        if i == usuarioInput:
            #Volvemos la palabra lista y después lo volveremos string
            
contador = 0