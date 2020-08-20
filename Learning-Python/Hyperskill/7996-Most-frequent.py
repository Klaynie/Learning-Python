from collections import Counter

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

text_list = text.split()

freq_counter = Counter(text_list)

n = int(input())

for i in range(n):
    print(freq_counter.most_common(n)[i][0], freq_counter.most_common(n)[i][1])