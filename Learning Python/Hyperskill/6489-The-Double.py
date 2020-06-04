import string

double_alphabet = {}

for letter in string.ascii_lowercase:
    double_alphabet[letter] = letter * 2

print(double_alphabet)