def generateWordDictionary():    
    d = {}
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        d[word] = ''
    return d

def rotate_word(word, amount):
    startLowerCase = ord('a')
    endLowerCase   = ord('z')
    newWord = ''
    for letter in word:
        if (ord(letter)+amount <= endLowerCase and ord(letter)+amount >= startLowerCase):
            newLetter = chr(ord(letter)+amount)
        if ord(letter)+amount > endLowerCase:
            newLetter = chr(startLowerCase+ord(letter)+amount-endLowerCase-1)
        if ord(letter)+amount < startLowerCase:
            additionalOrd = startLowerCase-(ord(letter)+amount)-1
            newLetter = chr(endLowerCase-additionalOrd)
        newWord = newWord + newLetter
    return newWord

def findRotatePairs():
    d = generateWordDictionary()
    results = {}
    for word in d:
        i = 1
        while i <= 25:
            rotatedWord = rotate_word(word, i)
            if rotatedWord in d:
                results[word, rotatedWord] = i
            i += 1
    return results
            
print(findRotatePairs())           