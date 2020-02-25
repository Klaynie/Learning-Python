import string
import random
wordCounterDict = 0

def process_file_markov(filename, prefixLength):
    '''
    This function will take a text file and perform a Markov analysis. It will take prefixLength words as the key for a dictionairy and will populate all unique words
    that follow after this key word tuple via a list
    
    filename: Name of the file
    prefixLength: Number of words to be used as key tuple
    '''
    global wordCounterDict
    positionDictionariy = dict()
    markovDictionariy = dict()
    fp = open(filename)
    i = 1
    for line in fp:
        process_line(line, positionDictionariy)
    while i < wordCounterDict-1:
        prefixList = []
        prefixTuple = tuple()
        j = 0
        while j < prefixLength:
            prefixList.append(positionDictionariy.get(i+j))
            j += 1
        prefixTuple = tuple(prefixList)
        if prefixTuple not in markovDictionariy:
            markovDictionariy[prefixTuple] = [positionDictionariy.get(i+j)]
        else:
            if positionDictionariy.get(i+j) not in markovDictionariy[prefixTuple]:
                markovDictionariy[prefixTuple].append(positionDictionariy.get(i+j))
        i += 1
    return markovDictionariy

def process_line(line, positionDictionariy):
    global wordCounterDict
    line = line.replace('-', ' ')
    word = ''
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        positionDictionariy[wordCounterDict] = word
        wordCounterDict += 1

def combineTwoDictionaries(dict1, dict2):
    outputdict = dict()
    for key, value in dict1.items():
        if key not in dict2:
            outputdict[key] = value
        else:
            combinedList = value[:]
            if key in dict2:
                for item in dict2[key]:
                    if item not in combinedList:
                        combinedList.append(item)
            outputdict[key] = combinedList
    for key, value in dict2.items():
        if key not in dict1:
            outputdict[key] = value
    return outputdict

def createRandomSenctenceFromMarkovDictionariy(markovDictionariy, numberOfWords):
    sentence = ''
    prefixList = []
    prefixTuple = tuple()
    # Seed the sentence with the a first randomly selected Markov Pair
    i = 0
    randomKey = random.choice(list(markovDictionariy.keys()))
    randomWord = random.choice(markovDictionariy[randomKey])
    for word in randomKey:
        sentence += word + ' '
        '''
        Taking all words after the first for the 2nd Key
        '''
        if i > 0:
            prefixList.append(word)
        i += 1
    sentence += randomWord + ' '
    prefixList.append(randomWord) # Randomly selected word from the list forms the last part of the 2nd Key 
    prefixTuple = tuple(prefixList)
    i += 1
    '''
    Create the rest of the sentence by using the a combination of the first Markov Pair with the randomly selected partner
    '''
    while i < numberOfWords:
        randomWord = random.choice(markovDictionariy[prefixTuple])
        sentence += randomWord + ' '
        '''
        Prepare the next key
        '''
        del prefixList[0]
        prefixTuple = tuple()
        prefixList.append(randomWord)
        prefixTuple = tuple(prefixList)
        i += 1
    print(sentence)

hist1 = process_file_markov('emma.txt', 2)
hist2 = process_file_markov('English.txt', 2)
hist = combineTwoDictionaries(hist1,hist2)
'''
test code
testtuple = tuple()
testwords = ['and','his']
testtuple = tuple(testwords)
print(1)
print(hist1[testtuple])
print(2)
print(hist2[testtuple])
print('combined')
print(hist[testtuple])
'''
createRandomSenctenceFromMarkovDictionariy(hist,30)