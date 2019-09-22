def is_abecedarian(word):
    word = word.lower()
    i = 0
    j = 1
    while i < len(word)-1:
        if word[i]>word[j]:
            return False
        i = i + 1
        j = j + 1
    return True

def traverse_list():
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            
traverse_list()