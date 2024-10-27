import random

defaultWords = ["bat", "computer", "elephant", "truck", "fan", "phone"]

def hideWord(word):
    numHiddenLetters = int(len(word) * 0.6)
    hiddenIndices = random.sample(range(len(word)), numHiddenLetters)
    hiddenWordList = [letter if index not in hiddenIndices else "_" for index, letter in enumerate(word)]
    return "".join(hiddenWordList), hiddenIndices

def playWordGuessingGame():
    print("Welcome to the Word Guessing Game!")
    
    wordList = defaultWords.copy()

    chosenWord = random.choice(wordList)
    hiddenWord, hiddenIndices = hideWord(chosenWord)
    wordInProgress = list(hiddenWord)
    attempts = 5  

    print(f"You have {attempts} attempts to guess the word.")
    print("Word:", hiddenWord)

    while attempts > 0:
        guess = input("Enter a single letter or try to solve the entire word: ").strip().lower()

        if len(guess) == 1:  
            if guess in chosenWord:
                for index in hiddenIndices:
                    if chosenWord[index] == guess:
                        wordInProgress[index] = guess
                print("Correct guess!")
            else:
                attempts -= 1
                print("Incorrect letter. Attempts remaining:", attempts)

        elif len(guess) == len(chosenWord):  
            if guess == chosenWord:
                print("Congratulations! You've guessed the word:", chosenWord)
                return
            else:
                attempts -= 1
                print("Incorrect word. Attempts remaining:", attempts)
        else:
            print("Invalid input. Enter a single letter or a full word of the correct length.")

        currentProgress = "".join(wordInProgress)
        print("Word:", currentProgress)

        if currentProgress == chosenWord:
            print("Congratulations! You've completed the word:", chosenWord)
            return

    print("Game over! The word was:", chosenWord)

playWordGuessingGame()
