"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

def read_dictionary(filename='c06d'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron
    return d

def generateWordDictionary():    
    d = {}
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        d[word] = ''
    return d

def checkHomophone(d, word1, word2):
    if (word1 in d and word2 in d):
        if d[word1] == d[word2]:
            return True
    else:
        return False

def traverseAllWords():
    wordDictionary = generateWordDictionary()
    pronunciationDictionary = read_dictionary(filename='c06d')
    for word in wordDictionary:
        word1 = word[1:]
        word2 = word[:1] + word[2:]
        if (word1 in wordDictionary and word2 in wordDictionary and checkHomophone(pronunciationDictionary, word1, word2)):
            print(word, word1, word2)
            
traverseAllWords()