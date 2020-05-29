commands = ['/exit','/help']
user_outputs = ['Bye!','The program calculates the sum and difference of numbers']
keep_going = True

def is_empty_line(input_):
    return input_ == ''

def is_single_number(input_):
    return ' ' not in input_

def convert_numbers_and_operators(start, end, numbers, operators, output_list):
    for list_iterator in range(start, end):
        output_list.append(numbers[list_iterator] * int(operators[list_iterator - start] + '1'))
    return output_list

def generate_output_list(numbers, operators):
    output_list = []
    if len(numbers) == len(operators):
        convert_numbers_and_operators(start=0, end=len(numbers), numbers=numbers, operators=operators, output_list=output_list)
    elif len(numbers) != len(operators):
        output_list.append(numbers[0])
        convert_numbers_and_operators(start=1, end=len(numbers), numbers=numbers, operators=operators, output_list=output_list)
    return output_list

def convert_input(input_):
    if input_.startswith('-'):
        input_ = input_.replace("-", "- ", 1)
    items = [item for item in input_.split()]
    numbers = [int(item) for item in items if item.isdigit()]
    operators = [convert_operator_string(item) for item in items if not item.isdigit()]
    return generate_output_list(numbers, operators)

def convert_operator_string(operator_string):
    if '-' not in operator_string:
        return '+'
    else:
        count_minus_sign = 0
        for sign in operator_string:
            if sign == '-':
                count_minus_sign += 1
        if count_minus_sign % 2 == 0:
            return '+'
        else:
            return '-'

def input_handler(input_):
    global keep_going
    if input_ == commands[0]:
        print(user_outputs[0])
        keep_going = False
    elif input_ == commands[1]:
        print(user_outputs[1])
    elif is_empty_line(input_):
        pass
    elif is_single_number(input_):
        print(input_)
    else:        
        print(sum(convert_input(input_)))

def calculator_loop():
    global keep_going
    while keep_going:
        input_ = input()
        input_handler(input_)

calculator_loop()