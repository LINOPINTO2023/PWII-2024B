import random
palabras = ["Personalizado", "Jugadores", "Paramiticuanquitaro", "Teclado"]
word_choose = random.randint(0, len(palabras) - 1)

delete_word = []
for letra in range(len(palabras[word_choose])//2):
    random_number = random.randint(0, len(palabras[word_choose]) - 1)
    if random_number not in delete_word:
        delete_word.append(random_number)
# Hasta aqui tengo una lista ordenada con numeros aleatorios
delete_word = sorted(delete_word)


new_chain = list(palabras[word_choose])

for index in delete_word:
    new_chain[index] = "_"

palabra_final = "".join(new_chain)

# Generar un numero aleatorio de intentos
intentos = random.randint(2, len(palabra_final) - 1)

print(palabra_final)
print(f"Tienes {intentos} intentos para adivinar la palabra.")
