def generateWordList():    
    t = []
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        t.append(word)
    return t

def interlock(wordList, word):
    """Checks whether a word can be split into two interlocked words.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return (evens in wordList) and (odds in wordList)

def interlock_general(wordList, word, n):
    """Checks whether a word can be split into n interlocked words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if (inter in wordList) == False:
            return False  
    return True

def interlock_general_word(word, n):
    """Checks whether a word can be split into n interlocked words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        print(inter)
                    
def traverseListForInterlock():
    t = generateWordList()
    for word in t:
        if interlock(t, word):
            print(word, word[::2], word[1::2])
            
def traverseListForInterlock_general(n):
    t = generateWordList()
    for word in t:
        if interlock_general(t, word, n):
            print(word)            

#traverseListForInterlock()
           
traverseListForInterlock_general(3)

#interlock_general_word('agonised', 3)