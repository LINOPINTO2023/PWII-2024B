import random

words = ["Tonto", "Jordan","Desconocido"]
n = random.choice(words)
i = 5
aciertos = 0
while i >= 0:
    for _ in n:
       poculto= n.replace("-")
    print("Palabra:"," ".join(n))
    print("Intentos restantes: ", i,)
    print("-----------------------------------------")
    i = i - 1
    print(n)