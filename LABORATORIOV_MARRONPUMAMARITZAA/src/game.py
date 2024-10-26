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
