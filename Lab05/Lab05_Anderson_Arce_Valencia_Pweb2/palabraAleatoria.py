import random
#Ocultar la palñabra
words = ["Tonto", "Jordan", "Desconocido"]
n = random.choice(words).lower()
num_letras = len(n)
max_ocultas = int(num_letras * 0.6)  # Máximo 60% de letras ocultas
indices_ocultos = random.sample(range(num_letras), max_ocultas)  # Elegimos qué letras ocultar

palabra_oculta = ""

for i, letra in enumerate(n):
    if i in indices_ocultos:
        palabra_oculta += "_"
    else:
        palabra_oculta += letra


#juegp:
intentos = 5
while intentos > 0 and "_" in palabra_oculta:
    print("Palabra:"," ".join(palabra_oculta))
    acertar = input(f"Introduce una letra o la palabra completa: ""\n------------------------------------------: " ).lower()
    #Primero un condicional para determinar si gano introducciendo la palabra completa
    if len(acertar) == 1 or len(acertar) == len(n):
        if acertar == n:
            print(f"Felicidades usted ha adivinado la palabra")
            palabra_oculta = n
            break
    
    #Segundo, si introduce una sola Letra
        elif len(acertar) == 1 and acertar in n:
                palabran = ""
                for i in range(len(n)):
                    if n[i] == acertar:
                        palabran += acertar
                    else:
                        palabran += palabra_oculta[i]
                palabra_oculta = palabran
                print("Encontraste una letra")
                print("-----------------------------------------")
        else:
            intentos -= 1
            print(f"Intento incorrecto. Te quedan {intentos} intentos.")
    else:
        print("Entrada invalida, debes introduccir una letra o palabra de " , len(n), "letras")

if '_' not in palabra_oculta:
    print(f"Ganaste!!!!!!!!\nLa palabra era:{n}")
else:
    print("Perdiste :p")