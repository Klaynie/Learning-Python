phone_number = input()

number_translation = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for number in phone_number:
    print(number_translation[int(number)])