import os


def contains_letters(word, optional_letters, must_have_letter):
    result = True
    for letter in word:
        if letter not in optional_letters:
            if letter != must_have_letter:
                result = False
    return result


def create_word_list(file_name):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file_name)
    result = open(abs_file_path)
    return result


def main(minimum_length, must_have_letter, optional_letters, file_name='words.txt'):
    result = []
    word_list = create_word_list(file_name)
    for line in word_list:
        word = line.strip()
        if len(word) >= minimum_length:
            if must_have_letter in word:
                if contains_letters(word, optional_letters, must_have_letter):
                    result.append(word)
    return result


minimum_length = 4
must_have_letter = 'p'
optional_letters = ['a', 'b', 'm', 'e', 'l', 'i']
print(main(minimum_length, must_have_letter, optional_letters))
