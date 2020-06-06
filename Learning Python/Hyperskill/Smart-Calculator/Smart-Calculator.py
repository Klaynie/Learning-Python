import string
from enum import IntEnum
from collections import deque

class UserOutput(IntEnum):
    BYE = 0
    EXPLAIN = 1
    UNKNOW_COMMAND = 2
    INVALID_EXPRESSION = 3
    INVALID_IDENTIFIER = 4
    UNKNOW_VARIABLE = 5
    INVALID_ASSIGNMENT = 6

class OperatorSymbol(IntEnum):
    PLUS = 0
    MINUS = 1
    TIMES = 2
    DIVISION = 3
    POWER = 4

class EqualitySymbol(IntEnum):
    EQUAL = 0

class CommandKeyword(IntEnum):
    EXIT = 0
    HELP = 1

commands = ['/exit','/help']
user_outputs = ['Bye!',
                'The program calculates the sum and difference of numbers, you can store numbers in variables', 
                'Unknown command',
                'Invalid expression',
                'Invalid identifier',
                'Unknown variable',
                'Invalid assignment']
command_start_symbol = '/'
equality_symbols = ['=']
operator_symbols = ['+', '-', '*', '/', '^']
bracket_symbols = ['(', ')']
variables_dict = {}
keep_going = True

def is_empty_line(input_):
    return input_ == ''

def is_single_number(input_):
    return ' ' not in input_

def split_input_into_assignment(input_):
    input_ = input_.replace(' ', '')
    try:
        key, value = input_.split(equality_symbols[EqualitySymbol.EQUAL])
    except ValueError:
        print(user_outputs[UserOutput.INVALID_ASSIGNMENT])
    else:
        return key, value

def variable_assignment(input_):
    global user_outputs, variables_dict
    try:
        key, value = split_input_into_assignment(input_)
    except TypeError:
        pass
    else:
        if check_assignment(key, value):
            assign_variable(key, value)

def assign_variable(key, value):
    global variables_dict
    try:
        int(convert_single_number(value))
    except ValueError:
        try:
            variables_dict[value]
        except KeyError:
            print(user_outputs[UserOutput.UNKNOW_VARIABLE])
        else:
            variables_dict[key] = variables_dict[value]
    else:
        variables_dict[key] = int(convert_single_number(value))

def check_assignment(key, value):
    """ Will check if the assignment can be performed, otherwise inform the user what went wrong.

    key, value are derived from user input via split_input_into_assignment(input_) and need to be checked for validity
    """
    result = False
    if check_assignment_validity(key, value):
        result = True
    elif not check_valid_variable_name(key):
        print(user_outputs[UserOutput.INVALID_IDENTIFIER])
        result = False
    elif not check_valid_content(key, value):
        print(user_outputs[UserOutput.INVALID_ASSIGNMENT])
        result = False
    elif value not in variables_dict.values():
        print(user_outputs[UserOutput.UNKNOW_VARIABLE])
        result = False
    else:
        print(user_outputs[UserOutput.INVALID_ASSIGNMENT])
    
    return result

def check_assignment_validity(key, value):
    return check_valid_variable_name(key) and check_valid_content(key, value)

def check_valid_variable_name(input_):
    for letter in input_:
        if letter not in string.ascii_letters:
            return False
    return True

def check_valid_content(key, value):
    global variables_dict
    result = False

    if value.isdigit():
        result = True
    elif try_conversion(value):
        result = True
    elif check_valid_variable_name(value):
        result = True

    return result

def try_conversion(value):
    for item in value:
        if item in string.ascii_letters:
            return False
    try:
        convert_single_number(value)
    except Exception:
        return False
    else:
        return True

def check_for_variables(input_):
    for letter in input_:
        if letter in string.ascii_letters:
            return True
    return False

def print_variable_content(input_):
    global variables_dict
    if input_ in variables_dict:
        print(variables_dict[input_])
    elif not check_valid_variable_name(input_):
        print(user_outputs[UserOutput.INVALID_IDENTIFIER])
    else:
        print(user_outputs[UserOutput.UNKNOW_VARIABLE])

def convert_single_number(input_):
    global operator_symbols
    operator_string = ''
    number = ''
    for item in input_:
        if item in operator_symbols:
            operator_string += item
        elif item.isdigit():
            number += item
    sign = convert_operator_string(operator_string)
    if sign == operator_symbols[OperatorSymbol.PLUS]:
        sign = ''
    return sign+number

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

def contains_plus_or_minus(string):
    return operator_symbols[OperatorSymbol.PLUS] in string or operator_symbols[OperatorSymbol.MINUS] in string

def convert_input(input_):
    global operator_symbols, variables_dict
    """ Converts the user input to be usable for calculations
    
    The user input needs to be converted into operators and numbers
    """
    if input_.startswith(operator_symbols[OperatorSymbol.PLUS]):
        input_ = input_.replace(operator_symbols[OperatorSymbol.PLUS], operator_symbols[OperatorSymbol.PLUS] + ' ', 1)
    elif input_.startswith(operator_symbols[OperatorSymbol.MINUS]):
        input_ = input_.replace(operator_symbols[OperatorSymbol.MINUS], operator_symbols[OperatorSymbol.MINUS] + ' ', 1)
    items = [item for item in input_.split()]
    numbers = []
    operators = []
    for item in items:
        if item.isdigit():
            numbers.append(int(item))
        else:
            try:
                variables_dict[item]
            except KeyError:
                if contains_plus_or_minus(item):
                    operators.append(convert_operator_string(item))
                else:
                    print(user_outputs[UserOutput.UNKNOW_VARIABLE])
            else:
                numbers.append(variables_dict[item])
    return generate_output_list(numbers, operators)

def convert_input2(input_):
    global operator_symbols, bracket_symbols
    postfix_stack = deque()
    analysis = []
    for item in input_:
        if item.isdigit():
            analysis.append('digit')
        elif item in operator_symbols:
            analysis.append('operator')
        elif item in bracket_symbols:
            analysis.append('bracket')
        elif item in string.ascii_letters:
            analysis.append('letter')
        elif item == ' ':
            analysis.append('space')
    i = 0
    while i < len(input_) - 1:
        temp_item = ''
        if analysis[i] != analysis[i + 1] and input_[i] != ' ':
            postfix_stack.append(input_[i])
        elif analysis[i] == analysis[i + 1]:
            temp_item += input_[i]
            while analysis[i] == analysis[i + 1] and i < len(input_) - 2:
                i += 1
                temp_item += input_[i]
                print(i)
            if i == len(input_) - 2:
                temp_item += input_[i + 1]
            postfix_stack.append(temp_item)
        if i == len(input_) - 2 and analysis[i] != analysis[i + 1] and input_[i] != ' ':
            postfix_stack.append(input_[i + 1])
        i += 1
    return postfix_stack

def check_postfix_stack(stack):
    pass

def convert_operator_string(operator_string):
    """ Converts the multiple addition and subtraction sings into one sign
    
    The number of minus signs defines the algebraic sign of the number
    """
    if not contains_plus_or_minus(operator_string):
        return operator_string
    elif operator_symbols[OperatorSymbol.MINUS] not in operator_string:
        return operator_symbols[OperatorSymbol.PLUS]
    else:
        count_minus_sign = 0
        for sign in operator_string:
            if sign == operator_symbols[OperatorSymbol.MINUS]:
                count_minus_sign += 1
        if count_minus_sign % 2 == 0:
            return operator_symbols[OperatorSymbol.PLUS]
        else:
            return operator_symbols[OperatorSymbol.MINUS]

def command_handler(input_):
    """ Checks if the command is in the list of commands

    Returns the command description if available, otherwise will let the user know that know that command is unkown
    """
    global keep_going, commands
    if input_ not in commands:
        print(user_outputs[UserOutput.UNKNOW_COMMAND])
    if input_ == commands[CommandKeyword.EXIT]:
        print(user_outputs[UserOutput.BYE])
        keep_going = False
    elif input_ == commands[CommandKeyword.HELP]:
        print(user_outputs[UserOutput.EXPLAIN])

def input_guardian(input_):
    """ Checks if the input format is technically correct

    If the input starts with "/" it will be treated as a command
    If the input is only digits it will be printed as is later on
    The input cannot end with an operator symbol
    Otherwise there should be at least one of the operator symbols in the input
    """
    result = True

    if input_.startswith(command_start_symbol):
        result = True
    elif input_.isdigit():
        result = True
    elif is_empty_line(input_):
        result = True
    elif input_.endswith(operator_symbols[OperatorSymbol.PLUS]):
        result = False
    elif input_.endswith(operator_symbols[OperatorSymbol.MINUS]):
        result = False

    return result

def contains_operator_symbols(input_):
    global operator_symbols
    result = False

    if operator_symbols[OperatorSymbol.PLUS] in input_:
        result = True
    elif operator_symbols[OperatorSymbol.MINUS] in input_:
        result = True
    elif operator_symbols[OperatorSymbol.TIMES] in input_:
        result = True
    elif operator_symbols[OperatorSymbol.DIVISION] in input_:
        result = True
    elif operator_symbols[OperatorSymbol.POWER] in input_:
        result = True
    
    return result

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
        elif equality_symbols[EqualitySymbol.EQUAL] in input_:
            variable_assignment(input_)
        elif check_for_variables(input_) and not contains_operator_symbols(input_):
            print_variable_content(input_)
        elif is_single_number(input_):
            print(convert_single_number(input_))
        else:        
            print(sum(convert_input(input_)))
    elif not input_guardian(input_):
        print(user_outputs[UserOutput.INVALID_EXPRESSION])

def calculator_loop():
    global keep_going
    while keep_going:
        input_ = input()
        input_handler(input_)

calculator_loop()

#print(convert_input2('888*3+-+12*(4-2)+BIG'))