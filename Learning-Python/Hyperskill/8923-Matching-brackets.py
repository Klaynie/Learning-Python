def check_for_matching_brackets(input_string):
    stack = []
    bracket_symbols = ['(', ')']
    for letter in input_string:
        if letter == bracket_symbols[0]:
            stack.append(letter)
        if letter == bracket_symbols[1]:
            try:
                stack.pop()
            except IndexError:
                return 'ERROR'
    if len(stack) == 0:
        return 'OK'
    return 'ERROR'

print(check_for_matching_brackets(input()))