def uses_only2(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word, string):
    word = word.lower()
    lengthString = len(string)
    stringLengthCounter = 0
    for letterString in string:
        for letterWord in word:
            if letterWord == letterString:
                stringLengthCounter = stringLengthCounter + 1
                break
        if stringLengthCounter == lengthString:
           return True
    return False    
            
def traverse_list(string):
    totalCounter = 0
    hasNoLetterFromStringCounter = 0
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        if uses_all(word, string) == True:
            print(word)
            
def uses_all2(word, required):
    return uses_only2(required, word)