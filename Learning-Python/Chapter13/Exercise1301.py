import string

def generateWordDictionairy(fileName):
    d = {}
    file = open(fileName)
    for line in file:
        line = line.lower()
        line = line.translate({ord(i): ' ' for i in string.punctuation})
        lineLength = len(line)
        counter = 0
        word = ''
        while counter < lineLength:
            if line[counter] == ' ':
                word = word.strip()
                if len(word) != 0:
                    d[word] = 1 + d.get(word, 0)
                word = ''
            if line[counter].isalpha():
                word += line[counter]
            counter += 1
    return d

print(generateWordDictionairy('English.txt'))