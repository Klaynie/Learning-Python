"""
Preprocess an input text:

    delete punctuation symbols (commas, periods, exclamation and question marks ,.!?),
    convert all symbols to lowercase.

Then print your text.

Punctuation marks appear not only at the end of the input string, so you have to figure out how to get rid of all of them.
"""
string = input()

punctionation_marks = ',.!?'

for item in punctionation_marks:
    string = string.replace(item, '')

print(string.lower())