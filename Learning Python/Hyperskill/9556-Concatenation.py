def concat(*words, sep=' '):
    return sep.join(words)

print(concat("turtle"))
print(concat("cat", "dog"))
print(concat("a", "b", "c", sep=":"))