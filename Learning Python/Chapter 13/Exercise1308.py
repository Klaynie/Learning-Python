import string
import random
wordCounterDict = 0

def process_file_markov(filename, prefixLength):
    '''
    This function will take a text file and markov analysis. It will take prefixLength words as the key for a dictionairy and will populate all unique words
    that follow after this key word tuple via a list
    
    filename: Name of the file
    prefixLength: Number of words to be used as key tuple
    '''
    global wordCounterDict
    positionDictionariy = dict()
    markovDictionariy = dict()
    fp = open(filename)
    i = 0
    for line in fp:
        process_line(line, positionDictionariy)
    while i < wordCounterDict:
        prefixList = []
        prefixTuple = tuple()
        for j in range(prefixLength):
            prefixList.append(positionDictionariy.get(i+j+1))
        prefixTuple = tuple(prefixList)
        if prefixTuple not in markovDictionariy:
            markovDictionariy[prefixTuple] = [positionDictionariy.get(i+j+2)]
        else:
            if positionDictionariy.get(i+j+2) not in markovDictionariy[prefixTuple]:
                markovDictionariy[prefixTuple].append(positionDictionariy.get(i+j+2))
        i += j+2
    return markovDictionariy

def process_line(line, positionDictionariy):
    global wordCounterDict
    line = line.replace('-', ' ')
    word = ''
    for word in line.split():
        #word = word.strip(string.punctuation + string.whitespace)
        #word = word.lower()
        positionDictionariy[wordCounterDict] = word
        wordCounterDict += 1

def createRandomSenctenceFromMarkovDictionariy(markovDictionariy, numberOfWords):
    sentence = ''
    i = 0
    while i < numberOfWords:
        randomKey = random.choice(list(markovDictionariy.keys()))
        randomWord = random.choice(markovDictionariy[randomKey])
        for word in randomKey:
            sentence += word + ' '
            i += 1
        sentence += randomWord + ' '
        i += 1
    print(sentence)

hist = process_file_markov('emma.txt', 3)
createRandomSenctenceFromMarkovDictionariy(hist,30)
#print(hist)