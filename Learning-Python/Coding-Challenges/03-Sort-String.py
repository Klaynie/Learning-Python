def sort_words(string):
    word_list = string.split()
    word_mapping = dict()
    temp_list = list()
    result = list()
    for word in word_list:
        lower_word = word.lower()
        word_mapping[lower_word] = word
        temp_list.append(lower_word)
    temp_list.sort()
    for word in temp_list:
        result.append(word_mapping[word])
    return ' '.join(result)


def sort_words2(string):
    words = string.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w) // 2:] for w in words]
    return ' '.join(words)


string = 'banana ORANGE apple'
# string = 'string of words'

print(sort_words2(string))