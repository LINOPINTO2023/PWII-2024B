import random
words = ["meow", "cats", "claudita", "aea"]
word = random.choice(words)
guessed_letters = []
while True:
    letter = input("Ingrese su letra correspondiente: ")
    guessed_letters.append(letter)
    hidden_letter = ''
    for c in word:
        if c in guessed_letters:
            hidden_letter += c
        else:
            hidden_letter += "_"
    print(hidden_letter)
    if "_" not in hidden_letter:
        print("¡Ganaste el juego!")
        break
attempts = 5

while attempts > 0:
    hidden_letter = ''.join([c if c in guessed_letters else '_' for c in word])
    print("Palabra:", hidden_letter)
    print("Intentos restantes:", attempts)
    
    letter = input("Ingrese su letra correspondiente: ").lower()
    guessed_letters.append(letter)
    if letter not in word:
        attempts -= 1
    
    if "_" not in hidden_letter:
        print("¡Ganaste el juego!")
        break

if attempts == 0:
    print("La palabra era:", word)
while attempts > 0:
    hidden_letter = ''.join([c if c in guessed_letters else '_' for c in word])
    print("Palabra:", hidden_letter)
    print("Intentos restantes:", attempts)

    letter = input("Ingrese una letra o la palabra completa: ").lower()
    
    if len(letter) == 1:
        guessed_letters.append(letter)
        if letter not in word:
            attempts -= 1
    elif len(letter) == len(word):
        if letter == word:
            print("Adivinaste la palabra:", word)
            break
        else:
            attempts -= 1
            print("La palabra no es correcta.")
    
    if '_' not in hidden_letter:
        print("Adivinaste la palabra:", word)
        break

if attempts == 0:
    print("La palabra era:", word)
