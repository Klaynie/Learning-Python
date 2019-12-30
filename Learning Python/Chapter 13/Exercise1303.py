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

def invertDict(d):
	inverse = {}
	for key, val in d.items():
	    inverse.setdefault(val, []).append(key)
	return inverse

def findTopWords(d):
    order = []
    topWords = []
    for key, val in d.items():
        order.append(key)
    order.sort(reverse=True)
    while len(topWords) < 20:
        topWords.append(d[order[len(topWords)]])
    print(topWords)

d = invertDict(generateWordDictionairy('English.txt'))

findTopWords(d)