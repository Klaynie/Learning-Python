def remove_punctuation(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    for char in string:
        if char not in punctuations:
            result += char
    return result


def remove_whitespaces(string):
    return ''.join(string.split())


def convert_to_lowercase(string):
    return string.lower()


def is_palindrome(string):
    string = convert_to_lowercase(string)
    string = remove_whitespaces(string)
    string = remove_punctuation(string)
    return string == string[::-1]


string = input("Enter a string: ")
print(is_palindrome(string))
