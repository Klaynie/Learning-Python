def histogram(inputWord):
    d = {}
    for character in inputWord:
        d[character] = 1 + d.get(character, 0)
    return d

def invert_dict(d):
	inverse = {}
	for key, val in d.items():
	    inverse.setdefault(val, []).append(key)
	return inverse

d = histogram('parrot')

inverse = invert_dict(d)

print(inverse)