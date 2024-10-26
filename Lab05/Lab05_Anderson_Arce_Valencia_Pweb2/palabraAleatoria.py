import random

words = ["Tonto", "Jordan","Desconocido"]
n = random.choice(words)
i = 1
while i < 4:
    print("Palabra:","".join(n))
    i= i + 1