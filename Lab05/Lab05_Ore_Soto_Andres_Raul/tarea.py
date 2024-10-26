import random
palabras = ["Personalizado", "Jugadores", "Matematicamentu", "Teclado"]
word_choose = random.randint(0, len(palabras) - 1)

delete_word = []
for letra in range(len(palabras[word_choose])//2):
    random_number = random.randint(0, len(palabras[word_choose]) - 1)
    delete_word.append(random_number)
# Hasta aqui tengo una lista ordenada con numeros aleatorios
delete_word = sorted(delete_word)


for number in range(len(palabras[word_choose])):
    new_chain = ""
    if number in delete_word:
        un_word = palabras[word_choose].replace(
            palabras[word_choose][number], "_")
        new_chain += un_word
    else:
        new_chain += palabras[word_choose][number]

print(new_chain)
