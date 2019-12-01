import datetime
def generateWordList():    
    t = []
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        t.append(word)
    return t

def buildLetterDictionary(wordList):
    d = {}
    for word in wordList:
        t = []
        for letter in word:
            t.append(letter)
        t.sort()
        tup = tuple(t)
        if tup not in d:
            d[tup] = [word]
        else:
            d[tup].append(word)
    return d

def findAnagrams(d):
    timestamp = datetime.datetime.utcnow()
    timestampString = str(timestamp.strftime("%Y")) + '-' + str(timestamp.strftime("%m")) + '-' + str(timestamp.strftime("%d")) + '_' + str(timestamp.strftime("%H")) + str(timestamp.strftime("%M")) + str(timestamp.strftime("%S"))
    outputFilename = 'Exercise1204-Anagram-List-' + timestampString + '.txt'
    file = open(outputFilename ,'w')
    for key, value in d.items():
        if len(value) > 1:
            t = value
            s = []
            for item in t:
                length =len(item)
                if length not in s:
                    s.append(length)
            for length in s:
                u = []
                for item in t:
                  if length == len(item):
                      u.append(item)
                if len(u) > 1:
                    p = '['
                    for item in u:
                        p += item
                        p += ','
                    p = p[:-1]
                    p += ']'
                    file.write(p + '\n')
    
wordList = generateWordList()
d = buildLetterDictionary(wordList)

findAnagrams(d)