all_word_list = input().split()
words_ending_in_s = []
for word in all_word_list:
    if word[-1].lower() == 's':
        words_ending_in_s.append(word)
print("_".join(words_ending_in_s))