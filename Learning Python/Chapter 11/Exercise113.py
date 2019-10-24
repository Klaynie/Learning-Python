def histogram(inputWord):
    d = {}
    for character in inputWord:
        d[character] = 1 + d.get(character, 0)
    return d

def print_hist(h):
    t = list(h.keys())
    t.sort()
    for c in t:
        print(c, h[c])
        
h = histogram('zzzaaavvvfgggg')
print_hist(h)