input_ = input().split('_')
converted_input = []
for word in input_:
    converted_input.append(word.capitalize())

print(''.join(converted_input))