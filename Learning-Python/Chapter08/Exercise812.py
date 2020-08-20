def rotate_word(word, amount):
    startUpperCase = ord('A')
    endUpperCase   = ord('Z')
    startLowerCase = ord('a')
    endLowerCase   = ord('z')
    newWord = ''
    for letter in word:
        if letter.isnumeric():
            newLetter = letter
        if letter.islower():
            if (ord(letter)+amount <= endLowerCase and ord(letter)+amount >= startLowerCase):
                newLetter = chr(ord(letter)+amount)
            if ord(letter)+amount > endLowerCase:
                newLetter = chr(startLowerCase+ord(letter)+amount-endLowerCase-1)
            if ord(letter)+amount < startLowerCase:
                additionalOrd = startLowerCase-(ord(letter)+amount)-1
                newLetter = chr(endLowerCase-additionalOrd)
        if letter.isupper():
            if (ord(letter)+amount <= endUpperCase and ord(letter)+amount >= startUpperCase):
                newLetter = chr(ord(letter)+amount)
            if ord(letter)+amount < startUpperCase:
                newLetter = chr(startUpperCase+ord(letter)+amount-endUpperCase-1)
            if ord(letter)+amount < startUpperCase:
                additionalOrd = startUpperCase-(ord(letter)+amount)-1
                newLetter = chr(endUpperCase-additionalOrd)
        newWord = newWord + newLetter
    return newWord
        
print(rotate_word('MELON',-10))