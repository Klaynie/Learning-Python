import string

def generateWordDictionairy(fileName):
    d = {}
    file = open(fileName)
    for line in file:
        line = line.lower()
        line = line.translate({ord(i): ' ' for i in string.punctuation})
        lineLength = len(line)
        letterCounter = 0
        word = ''
        while letterCounter < lineLength:
            if line[letterCounter] == ' ':
                word = word.strip()
                if len(word) != 0:
                    d[word] = 1 + d.get(word, 0)
                word = ''
            if line[letterCounter].isalpha():
                word += line[letterCounter]
            letterCounter += 1          
    return d

def generateWordListDictionary():    
    d = {}
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        d[word] = ''
    return d

def generateWordNotInDictionary(d1, d2):
    for key, value in d1.items():
        if key not in d2:
            print(key)


d1 = generateWordDictionairy('English.txt')
d2 = generateWordListDictionary()

generateWordNotInDictionary(d1, d2)