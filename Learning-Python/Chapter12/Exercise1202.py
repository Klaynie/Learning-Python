import random

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    d = {}
    for length, word in t:
        d.setdefault(length, []).append(word)
    res = []
    for key in d:
        randomList =random.choices(d[key], k=len(d[key])-1)
        for word in randomList:
            res.append(word)
    return res

def generateWordList(fileName):
    t = []
    file = open(fileName)
    for line in file:
        word = line.strip()
        t.append(word)
    return t
           
wordList = generateWordList('words.txt')

print(sort_by_length(wordList))