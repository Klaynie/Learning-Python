def is_abecedarian(word):
    word = word.lower()
    i = 0
    while i < len(word)-1:
        if word[i] > word[i+1]:
            return False
        i = i + 1
    return True

def traverse_list():
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            
traverse_list()