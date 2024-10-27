import random

defaultWords = ["bat", "computer", "elephant", "truck", "fan", "phone"]

def hideWord(word):
    numHiddenLetters = int(len(word) * 0.6)
    hiddenIndices = random.sample(range(len(word)), numHiddenLetters)
    hiddenWordList = [letter if index not in hiddenIndices else "_" for index, letter in enumerate(word)]
    return "".join(hiddenWordList), hiddenIndices

def playWordGuessingGame():
    print("\n" + "="*30)
    print("🎉 Welcome to the Word Guessing Game! 🎉")
    print("="*30)
    
    addWords = input("\nDo you want to add new words to the game? (yes/no): ").strip().lower()
    wordList = defaultWords.copy()

    if addWords == "yes":
        while True:
            newWord = input("Enter a new word (or type 'done' to finish): ").strip().lower()
            if newWord == "done":
                break
            elif newWord.isalpha(): 
                wordList.append(newWord)
            else:
                print("⚠️ Please enter a valid word with only letters.")

    chosenWord = random.choice(wordList)
    hiddenWord, hiddenIndices = hideWord(chosenWord)
    wordInProgress = list(hiddenWord)
    attempts = 5
    score = 0 

    print("\n" + "-"*30)
    print(f"You have {attempts} attempts to guess the word.")
    print("Word to guess:", hiddenWord)
    print("-"*30)

    while attempts > 0:
        guess = input("\nEnter a single letter or try to solve the entire word: ").strip().lower()

        if len(guess) == 1: 
            if guess in chosenWord:
                for index in hiddenIndices:
                    if chosenWord[index] == guess:
                        wordInProgress[index] = guess
                print("✅ Correct guess!")
            else:
                attempts -= 1
                print(f"❌ Incorrect letter. Attempts remaining: {attempts}")

        elif len(guess) == len(chosenWord):
            if guess == chosenWord:
                score += attempts * 10 
                print("\n" + "-"*30)
                print(f"🎉 Congratulations! You've guessed the word: {chosenWord}")
                print(f"🏆 Your score: {score}")
                print("-"*30)
                return
            else:
                attempts -= 1
                print(f"❌ Incorrect word. Attempts remaining: {attempts}")
        else:
            print("⚠️ Invalid input. Enter a single letter or a full word of the correct length.")

        currentProgress = "".join(wordInProgress)
        print("\nCurrent progress:", currentProgress)

        if currentProgress == chosenWord:
            score += attempts * 10
            print("\n" + "-"*30)
            print(f"🎉 Congratulations! You've completed the word: {chosenWord}")
            print(f"🏆 Your score: {score}")
            print("-"*30)
            return

    print("\n" + "-"*30)
    print(f"Game over! The word was: {chosenWord}")
    print(f"Your score: {score}")
    print("-"*30)

playWordGuessingGame()
