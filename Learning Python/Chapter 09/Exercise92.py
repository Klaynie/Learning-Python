def has_no_e(word):
    flag = False
    for letter in word:
        if letter == 'e':
            return False
    return True

def percentage_has_no_e():
    totalCounter = 0
    hasNoECounter = 0
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        if has_no_e(word):
            print(word)
            hasNoECounter = hasNoECounter + 1
        totalCounter = totalCounter + 1
    print('Out of ' + str(totalCounter) + ' words there are ' + str(hasNoECounter) + ' words without an e which is ' + str(round(hasNoECounter/totalCounter*100,2)) +'%')
    
percentage_has_no_e()