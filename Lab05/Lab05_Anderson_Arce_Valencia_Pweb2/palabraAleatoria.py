import random

words = ["Tonto", "Jordan", "Desconocido"]
n = random.choice(words)
num_letras = len(n)
max_ocultas = int(num_letras * 0.6)  # Máximo 60% de letras ocultas
indices_ocultos = random.sample(range(num_letras), max_ocultas)  # Elegimos qué letras ocultar
print(max_ocultas)
print(indices_ocultos)
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
    print("Intentos restantes: ", intentos,)
    print("-----------------------------------------")
    acertar = input("Introduce una letra o la palabra completa: " ).lower()
    intentos = intentos - 1  