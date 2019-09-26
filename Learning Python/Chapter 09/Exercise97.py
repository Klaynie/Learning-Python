def has_three_double_letters(word):
    word = word.lower()
    if len(word) < 6:
       return False
    i = 0
    while i < len(word)-5:
        if word[i] == word[i+1]:
            if word[i+2] == word[i+3]:
                if word[i+4] == word[i+5]:
                    return True
        i = i + 1
    return False

def traverse_list():
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        if has_three_double_letters(word):
            print(word)
            
            
traverse_list()