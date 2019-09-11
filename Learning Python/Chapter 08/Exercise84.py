def find(word, letter, index):
    index = index + 1
    if index > len(word):
        return 'Please provide an index between 0 and ' + str(len(word))
    else:
        while index < len(word):
            if word[index] == letter:
               return index
            index = index + 1
        return -1
    
print(find('counterintuitive', 'e', 1))