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

# Run the game
playWordGuessingGame()
