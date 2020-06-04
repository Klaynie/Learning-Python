import string

def process_line(line):
    hist = {}
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1
    return hist

def print_dict(dict_):
    for key, value in dict_.items():
        print(key, value)

print_dict(process_line(input()))