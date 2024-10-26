import random

# lista de palabras para el juego
palabras = ["Personalizado", "Jugadores", "Paramiticuanquitaro", "Teclado"]

continuar_jugando = True

while continuar_jugando:
    word_choose = random.randint(0, len(palabras) - 1)

    delete_word = []
    for letra in range(len(palabras[word_choose]) // 2 - 1):
        random_number = random.randint(0, len(palabras[word_choose]) - 1)
        if random_number not in delete_word:
            delete_word.append(random_number)

    delete_word = sorted(delete_word)

    new_chain = list(palabras[word_choose])
    for index in delete_word:
        new_chain[index] = "_"

    palabra_final = "".join(new_chain)

    intentos = random.randint(2, len(palabra_final) - 1)

    print(palabra_final)

    while intentos > 0:
        answer = input("Ingresa la palabra completa: ")

        if len(answer) != len(palabra_final):
            print("Ingresa una palabra con la misma cantidad de letras")
            continue

        if answer.lower() == palabras[word_choose].lower():
            print("-----------------------------------------\n")
            print("¡Felicidades ganaste!")
            print(f"La palabra era: {palabras[word_choose]}\n")
            break
        else:
            intentos -= 1
            print("Respuesta incorrecta")
            print(f"Te quedan {intentos} intentos")
            if intentos == 0:
                print(f"La palabra correcta era: {palabras[word_choose]}")
                break

    print("================================================")
    answer2 = input("¿Deseas continuar jugando? (s/n): ").lower()
    if answer2.lower() == "s":
        continuar_jugando = True
    else:
        continuar_jugando = False
        print("Gracias por jugar!")
