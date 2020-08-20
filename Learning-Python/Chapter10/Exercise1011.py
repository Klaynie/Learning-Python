import math

def bisect(inputWord, inputList):
    global t
    middle = findmiddle(len(inputList)-1)
    if middle == 0:
        return None
    if inputWord > inputList[middle]:
        return bisect(inputWord, inputList[middle:])
    if inputWord < inputList[middle]:
        return bisect(inputWord, inputList[:middle])
    if inputWord == inputList[middle]:
        return t.index(inputWord)
    
def findmiddle(number):
    return math.ceil(number/2)

def generateWordList():    
    t = []
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        t.append(word)
    return t

t = generateWordList()
counter = 0
    
print(bisect('alien', t))