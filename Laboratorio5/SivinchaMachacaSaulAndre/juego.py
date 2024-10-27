import random

defaultWords = ["bat", "computer", "elephant", "truck", "fan", "phone"]

def hideWord(word):
    numHiddenLetters = int(len(word) * 0.6)
    hiddenIndices = random.sample(range(len(word)), numHiddenLetters)
    hiddenWordList = [letter if index not in hiddenIndices else "_" for index, letter in enumerate(word)]
    return "".join(hiddenWordList), hiddenIndices
