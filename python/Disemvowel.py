def disemvowel(string):
    vowels = "aeiou"
    newString = ""
    for letter in string:
        if letter.lower() in vowels:
            continue
        else:
            newString += letter
    return newString
