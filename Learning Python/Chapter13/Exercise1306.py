import string

def process_file(filename):
    wordSet = set()
    fp = open(filename)
    for line in fp:
        process_line(line, wordSet)
    return wordSet

def process_line(line, wordSet):
    line = line.replace('-', ' ')
    word = ''
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        if word not in wordSet:
            wordSet.add(word)

def checkForWordsNotInList(inputSet1, inputSet2):
    outputSet3 = set()
    for item in inputSet2:
        if item not in inputSet1:
            if item not in outputSet3:
                outputSet3.add(item)
    return outputSet3

wordsInBook = process_file('emma.txt')
wordList = process_file('words.txt')

wordsNotInList = checkForWordsNotInList(wordList, wordsInBook)

print(wordsNotInList)