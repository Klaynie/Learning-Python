import string

def generateWordDictionairy(fileName):
    d = {}
    wordCounter = 0
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
                    wordCounter += 1
                word = ''
            if line[letterCounter].isalpha():
                word += line[letterCounter]
            letterCounter += 1
    print(wordCounter)            
    return d

print(len(generateWordDictionairy('English.txt')))