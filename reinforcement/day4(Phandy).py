# Exercise One==================
def getCharAtIndex(word):
    character = ""
    for char in range(len(word)):
        if char == indexInput:
            character = word[char]
    return character
word = input()
again = True
while again:
    indexInput = int(input())
    result = getCharAtIndex(word)
    if indexInput > len(word):
        result = "Index out of range input again"
        again = True
    else:
        again = False
    print(result)

# Exercise Two==================

def convertCamelToSnake(word):
    isSmall = False
    newWord = ""
    for char in range(len(word)):
        if word[char] == word[char].upper() and word[char].isalpha():
            newWord += "_" + word[char].lower()
            isSmall = True
        else:
            newWord += word[char]
    if not isSmall:
            newWord = "None"
    return newWord
word = input()
print(convertCamelToSnake(word))


# Exercise Three================
amountOfFruits = int(input())
arrayOfDictionary = []
sumOfPrice = 0
for num in range(amountOfFruits):
    dictionary = {}
    fruit = input()
    dictionary["name"] = fruit
    priceOfFruit = int(input())
    dictionary["price"] = priceOfFruit
    sumOfPrice += priceOfFruit
    arrayOfDictionary.append(dictionary)
print(arrayOfDictionary)
if sumOfPrice > 40 :
    result = "Error you don't have enough money"
print(result)

