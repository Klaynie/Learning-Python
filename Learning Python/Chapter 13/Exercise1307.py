import string
import random
import bisect

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    word = ''
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def wordList(dict):
    wordList = []
    for key, value in dict.items():
        if key not in wordList:
            wordList.append(key)
    return wordList

def cummulative_sum(dict):
    res = []
    i = 0
    for key, value in dict.items():
        i += value
        res.append(i)
    return res

def createRandomWordNumber(wordList):
    return random.randint(1, wordList[len(wordList)-1])

def findIndexOfNumber(cummulativeList, inputNumber):
    return bisect.bisect_right(cummulativeList, inputNumber)

hist = process_file('emma.txt')
wordList = wordList(hist)
cummulativeWordList = cummulative_sum(hist)
randomWordNumber = createRandomWordNumber(cummulativeWordList)
entryPoint = findIndexOfNumber(cummulativeWordList, randomWordNumber)

print(randomWordNumber, wordList[entryPoint])