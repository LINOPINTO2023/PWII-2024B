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

# entrada para la respuesta
while True:
    answer = input("ingresa la palabra completa: ")
    if len(answer) != len(palabra_final):
        print("Ingresa una palabra con la misma cantidad de letras")
        continue
    else:
        if answer.lower() == palabras[word_choose].lower():
            print("Felicidades ganaste!")
            print(f"La palabra era: {palabras[word_choose]}")
            break
        else:
            intentos -= 1
            print("Respuesta incorrecta.")
            if intentos == 0:
                print(f"La palabra correcta era: {palabras[word_choose]}")
                break
