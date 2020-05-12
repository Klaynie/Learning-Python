input_string = input()

output_string = ''
for letter in input_string:
    if letter.islower():
        output_string += letter
    else:
        output_string += '_' + letter.lower()
print(output_string)