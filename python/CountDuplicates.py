# count number of letters with duplicates
# my code
def duplicate_count(text):
    dupCount = 0
    dupArr = []
    text = text.lower()
    for letter in text:
        if text.count(letter) > 1 and letter not in dupArr:
            dupCount += 1
            dupArr.append(letter)
    return dupCount

# optimal, not mine
def optimatl_duplicate_count(text):
    return len([letter for letter in set(text.lower()) if text.lower().count(letter) > 1])