def generateWordList(fileName):
    d = {}
    t = []
    countLetter = 0
    file = open(fileName)
    for line in file:
        word = line.strip()
        for letter in word.lower():
            if letter.isalpha():
                d[letter] = 1 + d.get(letter, 0)
                countLetter += 1
    for key in d:
        d[key] /=  countLetter
        t.append((key, d[key]))
        t.sort()
    return t

print(generateWordList('Deutsch.txt'))
print(generateWordList('English.txt'))
print(generateWordList('French.txt'))