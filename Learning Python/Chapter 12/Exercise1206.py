flagForWordRemoval = False

def generateWordDictionary():    
    d = {}
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        d[word] = ''
    return d

def createWordListWithOneLetterRemoved(word):
    i = 0
    newWordList = []
    if len(word) == 1:
        return newWordList
    while i <= len(word)-1:
        newWord = ''
        j = 0
        while j <= len(word)-1:
            for letter in word:
                if j != i:
                    newWord += letter
                j += 1
        newWordList.append(newWord)
        i +=1
    return newWordList

def checkIfWordCanBeReduced(word, wordDictionary):
    global flagForWordRemoval
    flagForWordRemoval = False
    wordList = createWordListWithOneLetterRemoved(word)
    if wordList == []:
        flagForWordRemoval = True
    if len(wordList) > 0:
        for word in wordList:
            if word in wordDictionary:
                checkIfWordCanBeReduced(word, wordDictionary)
    return flagForWordRemoval

def createDictionaryWithPossibleWords(wordDictionary):
    wordLengthDictionary = {}
    for word in wordDictionary:
        if checkIfWordCanBeReduced(word, wordDictionary) == True:
            if len(word) not in wordLengthDictionary:
                    wordLengthDictionary[len(word)] = [word]
            else:
                wordLengthDictionary[len(word)].append(word)
    return wordLengthDictionary

def printAllSubWords(word, wordDictionary):
    wordList = createWordListWithOneLetterRemoved(word)
    if wordList == []:
        return
    if len(wordList) > 0:
        for word in wordList:
            if word in wordDictionary:
                print(word)
                printAllSubWords(word, wordDictionary)

wordDictionary = generateWordDictionary()
possibleWordDictionary = createDictionaryWithPossibleWords(wordDictionary)

print(possibleWordDictionary[10]) #['insolating', 'restarting', 'staunchest', 'twitchiest']

for word in possibleWordDictionary[10]:
    printAllSubWords(word, wordDictionary)