def searchList():
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        wordLength = len(word)
        if wordLength > 20:
           print(word)

searchList()