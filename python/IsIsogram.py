# check for isogram
# my code
def is_isogram(word):
    cleanWord = word.lower()
    letterArr = []
    for letter in cleanWord:
        if letter.isalpha():
            if letter in letterArr:
                return False
            letterArr.append(letter)
    return True

# optimal code found (not mine)
def is_isogram_optimal(word):
    return len(string) == len(set(word.lower()))