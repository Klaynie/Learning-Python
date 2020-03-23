def histogram(inputWord):
    d = {}
    for character in inputWord:
        d[character] = 1 + d.get(character, 0)
    return d

print(histogram('brontosaurus'))