def uses_only(word, string):
    word = word.lower()
    for letterWord in word:
        for letterString in string:
            checkLetterWordEqualLetterStringFlag = letterWord == letterString
            if checkLetterWordEqualLetterStringFlag == True:
                break
        if checkLetterWordEqualLetterStringFlag == False:
            return False
    return True    

def uses_only2(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True
            
def traverse_list(string):
    totalCounter = 0
    hasNoLetterFromStringCounter = 0
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        if uses_only(word, string) == True:
            print(word)
            
traverse_list('acefhlo')

'''
hello fella feel each local leaf
'''