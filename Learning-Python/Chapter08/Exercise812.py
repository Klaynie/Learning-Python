def rotate_word(word, amount):
    start_upper_case = ord('A')
    end_upper_case   = ord('Z')
    start_lower_case = ord('a')
    end_lower_case   = ord('z')
    newWord = ''
    for letter in word:
        if letter.isnumeric():
            newLetter = letter
        elif letter.islower():
            new_letter = find_new_letter(letter, amount, start_lower_case, end_lower_case)
        elif letter.isupper():
            new_letter = find_new_letter(letter, amount, start_upper_case, end_upper_case)
        newWord = newWord + new_letter
    return newWord

def find_new_letter(letter, amount, start, end):
    if (ord(letter) + amount <= end and ord(letter) + amount >= start):
        new_letter = chr(ord(letter) + amount)
    elif ord(letter) + amount > end:
        new_letter = chr(start + ord(letter) + amount - end - 1)
    elif ord(letter) + amount < start:
        additional_ord = start-(ord(letter) + amount) - 1
        new_letter = chr(end - additional_ord)
    return new_letter

print(rotate_word('cheer', 7))
print(rotate_word('melon', -10))
print(rotate_word('IBM', -1))