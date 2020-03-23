import random

def histogram(inputWord):
    d = {}
    for character in inputWord:
        d[character] = 1 + d.get(character, 0)
    return d

def chooseFromHist(inputDictionary):
    '''
    We want to return each letter with its weighted probability, for this we can build up a cumulative sum of the letters and a list of the letter values
    We can create a new dictionary that has the letter values and select the index with its weight
    '''
    sumOfHist = 0
    histRanges = []
    probabilityDictionary = {}
    for key, value in inputDictionary.items():
        sumOfHist += value
        histRanges.append(sumOfHist)
        probabilityDictionary[sumOfHist] = key
    returnKey = random.choices(histRanges, cum_weights = histRanges)
    return probabilityDictionary[returnKey[0]]

d = histogram('abbbbbbbbb')    
print(chooseFromHist(d))
'''
Quick Check Code
i = 0
counterA = 0
counterS = 0
while i < 100:
    letter = chooseFromHist(d)
    if letter == 'a':
        counterA += 1
    if letter == 'b':
        counterS += 1
    i += 1
print(counterA, counterS)
'''