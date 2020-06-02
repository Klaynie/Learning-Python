commands = ['/exit','/help']
user_outputs = ['Bye!','The program calculates the sum and difference of numbers', 'Unknown command', 'Invalid expression']
command_start_symbol = '/'
operator_symbols = ['+', '-']
keep_going = True

def is_empty_line(input_):
    return input_ == ''

def is_single_number(input_):
    return ' ' not in input_

def convert_numbers_and_operators(start, end, numbers, operators, output_list):
    """ Converts numbers and operators list into one list of signed numbers
    
    numbers and operators list can be of different length so operators index value has to be shifted
    """
    for list_iterator in range(start, end):
        output_list.append(numbers[list_iterator] * int(operators[list_iterator - start] + '1'))
    return output_list

def generate_output_list(numbers, operators):
    """ Combines numbers and operators list into one list

    The numbers and operators are combined intto a list of signed values
    to use the built in sum method to perfom addition and subtraction with of
    all user provided numbers.

    numbers: list containing only numbers
    operators: list containing mathematical operator symbol
    """
    output_list = []
    if len(numbers) == len(operators):
        convert_numbers_and_operators(start=0, end=len(numbers), numbers=numbers, operators=operators, output_list=output_list)
    elif len(numbers) != len(operators):
        output_list.append(numbers[0])
        convert_numbers_and_operators(start=1, end=len(numbers), numbers=numbers, operators=operators, output_list=output_list)
    return output_list

def convert_input(input_):
    """ Converts the user input to be usable for calculations
    
    The user input needs to be converted into operators and numbers
    """
    if input_.startswith('-'):
        input_ = input_.replace("-", "- ", 1)
    items = [item for item in input_.split()]
    numbers = [int(item) for item in items if item.isdigit()]
    operators = [convert_operator_string(item) for item in items if not item.isdigit()]
    return generate_output_list(numbers, operators)

def convert_operator_string(operator_string):
    """ Converts the multiple addition and subtraction sings into one sign
    
    The number of minus signs defines the algebraic sign of the number
    """
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

def command_handler(input_):
    """ Checks if the command is in the list of commands

    Returns the command description if available, otherwise will let the user know that know that command is unkown
    """
    global keep_going, commands
    if input_ not in commands:
        print(user_outputs[2])
    if input_ == commands[0]:
        print(user_outputs[0])
        keep_going = False
    elif input_ == commands[1]:
        print(user_outputs[1])

def input_guardian(input_):
    """ Checks if the input format is technically correct

    If the input starts with "/" it will be treated as a command
    If the input is only digits it will be printed as is later on
    The input cannot end with an operator symbol
    Otherwise there should be at least one of the operator symbols in the input
    """
    if input_.startswith(command_start_symbol):
        return True
    if input_.isdigit():
        return True
    if input_.endswith(operator_symbols[0]):
        return False
    if input_.endswith(operator_symbols[1]):
        return False
    if (operator_symbols[0] not in input_) and (operator_symbols[1] not in input_):
        return False
    return True

def input_handler(input_):
    """ Checks the user input and passes it to the correct function
    
    The guardian will check if the input format is
    input that starts with "/" has to go to the command function
    If there is no empty space in the input it will be printed as is, otherwise the sum of all items is calculated
    """
    global keep_going
    if input_guardian(input_):
        if input_.startswith(command_start_symbol):
            command_handler(input_)
        elif is_empty_line(input_):
            pass
        elif is_single_number(input_):
            print(input_)
        else:        
            print(sum(convert_input(input_)))
    if not input_guardian(input_):
        print(user_outputs[3])

def calculator_loop():
    global keep_going
    while keep_going:
        input_ = input()
        input_handler(input_)

calculator_loop()

#print(input_guardian('11'))
#print(input_guardian('8 + 7 - 4'))
#print(input_guardian('abc'))
#print(input_guardian('+15'))
#print(input_guardian('18 22'))
#print(input_guardian('-22'))
#print(input_guardian('22-'))
#print(input_guardian('/go'))