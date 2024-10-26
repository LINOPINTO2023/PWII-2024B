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
#Usamos join para convertir la lista en string
palabraOculta = "".join(palabraOculta)
print("La palabra oculta es:", palabraOculta)
#Creamos un contador de intentos que se mostrará al usuario, tendrá 5 intentos para completar la palabra
intentos = 5
while intentos != 0:
    #Pedimos al usuario que ingrese una letra o la palabra completa a adivinar
    usuarioInput = input("Ingrese la letra o palabra completa: ")
    #Si introduce la palabra completa
    if len(usuarioInput) > 1 and usuarioInput == palabraEscogida:
        print("Palabra correcta, ganaste")
    #Si solo introduce una letra
    elif len(usuarioInput) == 1:
        if usuarioInput in palabraEscogida:
            palabraOculta = list(palabraOculta)
            for i in range(len(palabraEscogida)):
                if palabraEscogida[i] == usuarioInput:
                    #Volvemos la palabra lista, lo reemplazamos por el input del usuario y lo volveremos string de nuevo
                    palabraOculta[i] = usuarioInput
            palabraOculta = "".join(palabraOculta)
            print(f"Palabra correcta, tiene {intentos} intentos")
        else:
            intentos-=1
            print(f"Letra incorrecta, tiene {intentos} intentos")
        print(palabraOculta)