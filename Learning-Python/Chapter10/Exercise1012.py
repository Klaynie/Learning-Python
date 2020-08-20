'''
Exercise 10.12. Two words are a "reverse pair" if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list. Solution: http://thinkpython.com/code/
reverse_pair.py.
'''

def generateWordList():    
    t = []
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        t.append(word)
    return t

def generateReverseWordList():    
    t = []
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        reverseWord = word[::-1]
        t.append(reverseWord)
    return t

def findReverseWordInList():
    reverseList = generateReverseWordList()
    normalList = generateWordList()
    for word in reverseList:
        if word in normalList:
            print(word, word[::-1])
             
findReverseWordInList()