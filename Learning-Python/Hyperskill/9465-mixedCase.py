word_list = input().split()

new_word_list = [word_list[0].lower()]
for number in range(1, len(word_list)):
    new_word_list.append(word_list[number].capitalize())

print("".join(new_word_list))