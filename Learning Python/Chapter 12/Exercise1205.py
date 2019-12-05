import datetime

def generateWordList():
    wordList = []
    wordListFile = open('words.txt')
    for line in wordListFile:
        word = line.strip()
        wordList.append(word)
    return wordList

def buildLetterDictionary(wordList):
    letterDictionary = {}
    for word in wordList:
        temporaryWordList = []
        for letter in word:
            temporaryWordList.append(letter)
        temporaryWordList.sort()
        temporaryTuple = tuple(temporaryWordList)
        if temporaryTuple not in letterDictionary:
            letterDictionary[temporaryTuple] = [word]
        else:
            letterDictionary[temporaryTuple].append(word)
    return letterDictionary

def findMetathesisPair(letterDictionary):
    metathesisWordList = []
    for letterTuple, wordList in letterDictionary.items():
        lengthWordList = len(wordList)
        if lengthWordList > 1:
            i = 1
            while i <= lengthWordList-1:
                if howManyLettersAreDifferent(wordList[0],wordList[i]) <= 2:
                    metathesisWordTuple = wordList[0],wordList[i]
                    metathesisWordList.append(metathesisWordTuple)
                i += 1
    return metathesisWordList

def howManyLettersAreDifferent(word1, word2):
    '''
    This function assumes that the words are of the same length
    '''
    i = 0
    differentLetterCounter = 0
    while i <= len(word1)-1:
        if not (word1[i] == word2[i]):
            differentLetterCounter += 1
        i += 1
    return differentLetterCounter

wordList = generateWordList()
d = buildLetterDictionary(wordList)
print(findMetathesisPair(d))