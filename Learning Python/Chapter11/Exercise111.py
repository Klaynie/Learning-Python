def generateWordDictionary():    
    d = {}
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        d[word] = ''
    return d
    
print(generateWordDictionary())