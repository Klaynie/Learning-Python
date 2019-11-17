def histogram(inputWord):
    d = {}
    for character in inputWord:
        d[character] = 1 + d.get(character, 0)
    return d

def reverse_lookup(d, v):
    t = []
    for k in d:
        if d[k] == v:
            t.append(k)
    return t

d = histogram('zavvvfgggg')

print(reverse_lookup(d, 5))