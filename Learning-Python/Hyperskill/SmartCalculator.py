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

class BracketSymbol(IntEnum):
    OPEN = 0
    CLOSE = 1

commands = ['/exit','/help']
user_outputs = ['Bye!',
                'The program calculates the result of your expression, use "+", "-", "*", "/" or "^", you can store numbers in variables', 
                'Unknown command',
                'Invalid expression',
                'Invalid identifier',
                'Unknown variable',
                'Invalid assignment']
all_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
command_start_symbol = '/'
equality_symbols = ['=']
operator_symbols = ['+', '-', '*', '/', '^']
bracket_symbols = ['(', ')']
variables_dict = {}
keep_going = True

def is_empty_line(input_):
    return input_ == ''

def is_single_number(input_):
    result = True
    input_list = convert_input_to_list(analyse_input(input_), input_)
    if len(input_list) == 1:
        if not input_list[0].isdigit():
            result = False
    elif len(input_list) == 2:
        if not input_list[1].isdigit():
            result = False
        elif not contains_plus_or_minus(input_list[0]):
            result = False
    elif len(input_list) > 2:
        result = False
    return result

def split_input_into_assignment(input_):
    input_ = input_.replace(' ', '')
    try:
        key, value = input_.split(equality_symbols[EqualitySymbol.EQUAL])
    except ValueError:
        print(user_outputs[UserOutput.INVALID_ASSIGNMENT])
    else:
        return key, value

def variable_assignment(input_):
    try:
        key, value = split_input_into_assignment(input_)
    except TypeError:
        pass
    else:
        if check_assignment(key, value):
            assign_variable(key, value)

def assign_variable(key, value):
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
    result = True
    for letter in input_:
        if letter not in all_letters:
            result = False
    return result

def check_valid_content(key, value):
    result = False
    if value.isdigit():
        result = True
    elif try_conversion(value):
        result = True
    elif check_valid_variable_name(value):
        result = True
    return result

def try_conversion(value):
    result = True
    for item in value:
        if item in all_letters:
            result = False
    try:
        convert_single_number(value)
    except Exception:
        result = False
    else:
        result = True
    return result

def check_for_variables(input_):
    result = False
    for letter in input_:
        if letter in all_letters:
            result = True
    return result

def print_variable_content(input_):
    if input_ in variables_dict:
        print(variables_dict[input_])
    elif not check_valid_variable_name(input_):
        print(user_outputs[UserOutput.INVALID_IDENTIFIER])
    else:
        print(user_outputs[UserOutput.UNKNOW_VARIABLE])

def convert_single_number(input_):
    """ Prepare single numbers for printing
    
    Single input numbers can contain multiple operator plus or minus signs in front of them
    """
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
    result = sign+number
    return result

def analyse_input(input_):
    """ Dividing user input into categories for later usage
    
    numerical values: 'digit'
    operators: 'operator'
    brackets: 'bracket'
    ASCII-letters: 'letter'
    Whitespace: 'space'
    """
    result = []
    for item in input_:
        if item.isdigit():
            result.append('digit')
        elif item in operator_symbols:
            result.append('operator')
        elif item in bracket_symbols:
            result.append('bracket')
        elif item in all_letters:
            result.append('letter')
        elif item == ' ':
            result.append('space')
    return result

def convert_input_to_list(analysis, input_):
    result = []
    i = 0
    if len(input_) == 1:
        result.append(input_[i])
    elif len(input_) > 1:
        while i < len(input_) - 1:
            temp_item = ''
            if analysis[i] != analysis[i + 1] and input_[i] != ' ' or analysis[i] == 'bracket':
                result.append(input_[i])
            elif analysis[i] == analysis[i + 1] and analysis[i] != 'bracket':
                temp_item += input_[i]
                while analysis[i] == analysis[i + 1] and analysis[i] != 'bracket' and i < len(input_) - 2:
                    i += 1
                    temp_item += input_[i]
                if i == len(input_) - 2:
                    temp_item += input_[i + 1]
                result.append(temp_item)
            i += 1
            if i == len(input_) - 1 and analysis[i - 1] != analysis[i] and input_[i] != ' ':
                result.append(input_[i])
    return result

def compare_operator_precedence(item1, item2):
    return set_priority(item1) > set_priority(item2)

def set_priority(operator):
    result = 0
    if contains_plus_or_minus(operator):
        result = 1
    elif contains_multiplication_or_division(operator):
        result = 2
    elif operator == operator_symbols[OperatorSymbol.POWER]:
        result = 3
    return result

def convert_input(input_):
    """ Converts the input into Postfix Notation via the following algorithm
    
    1) Add operands (numbers and variables) to the result (postfix notation) as they arrive.
    2) If the stack is empty or contains a left parenthesis on top, push the incoming operator on the stack.
    3) If the incoming operator has higher precedence than the top of the stack, push it on the stack.
    4) If the incoming operator has lower or equal precedence than or to the top of the stack, pop the stack and
       add operators to the result until you see an operator that has a smaller precedence or a left parenthesis 
       on the top of the stack; then add the incoming operator to the stack.
    5) If the incoming element is a left parenthesis, push it on the stack.
    6) If the incoming element is a right parenthesis, pop the stack and add operators to the result until you 
       see a left parenthesis. Discard the pair of parentheses.
    7) At the end of the expression, pop the stack and add all operators to the result.
    """
    # Find Algorithm to solve issue with expressions that start with '-'
    # User enumerate in for loops for i, item in enumerate(list)
    global operator_symbols, bracket_symbols
    postfix_stack = deque()
    operators_stack = deque()
    input_list = convert_input_to_list(analyse_input(input_), input_)
    for item in input_list:
        if not contains_brackets(item) and not contains_operator_symbols(item):
            postfix_stack.append(item)
        elif contains_operator_symbols(item):
            if contains_plus_or_minus(item):
                item = convert_operator_string(item)
            if len(operators_stack) == 0 or operators_stack[-1] == bracket_symbols[BracketSymbol.OPEN]:
                operators_stack.append(item)
            elif compare_operator_precedence(item, operators_stack[-1]):
                operators_stack.append(item)
            elif not compare_operator_precedence(item, operators_stack[-1]):
                postfix_stack.append(operators_stack.pop())
                operators_stack.append(item)
        elif item == bracket_symbols[BracketSymbol.OPEN]:
            operators_stack.append(item)
        elif item == bracket_symbols[BracketSymbol.CLOSE]:
            while operators_stack[-1] != bracket_symbols[BracketSymbol.OPEN]:
                postfix_stack.append(operators_stack.pop())
            operators_stack.pop()
    for _ in range(len(operators_stack)):
        postfix_stack.append(operators_stack.pop())
    return postfix_stack

def convert_operator_string(operator_string):
    """ Converts the multiple addition and subtraction sings into one sign
    
    The number of minus signs defines the algebraic sign of the number
    """
    result = ''
    if not contains_plus_or_minus(operator_string):
        result = operator_string
    elif operator_symbols[OperatorSymbol.MINUS] not in operator_string:
        result = operator_symbols[OperatorSymbol.PLUS]
    else:
        count_minus_sign = 0
        for sign in operator_string:
            if sign == operator_symbols[OperatorSymbol.MINUS]:
                count_minus_sign += 1
        if count_minus_sign % 2 == 0:
            result = operator_symbols[OperatorSymbol.PLUS]
        else:
            result = operator_symbols[OperatorSymbol.MINUS]
    return result

def postfix_calculation(postfix_stack):
    """ Performs mathematical calculation with the postfix notation algorithm
    
    1) If the incoming element is a number, push it into the stack (the whole number, not a single digit!).
    2) If the incoming element is the name of a variable, push its value into the stack.
    3) If the incoming element is an operator, then pop twice to get two numbers and perform the operation; push the result on the stack.
    4) When the expression ends, the number on the top of the stack is a final result.
    """
    # ToDo: Bugfixing for expressions that start with '-' Try to convert numbers to int
    calculation_stack = deque()
    postfix_stack = convert_postfix_stack_for_calculation(postfix_stack)
    for item in postfix_stack:
        if type(item) == int:
            calculation_stack.append(item)
        else:
            calculation_second_number = calculation_stack.pop() # Number on top of the stack is the second number for calculation
            calculation_first_number = calculation_stack.pop() # Second number in the stack is the first number for calculation
            calculation_stack.append(perform_postfix_calculation(calculation_first_number, item, calculation_second_number))
    result = calculation_stack.pop()
    return result

def convert_postfix_stack_for_calculation(postfix_stack):
    converted_postfix_stack = deque()
    for item in postfix_stack:
        if not contains_operator_symbols(item):
            if item.isdigit():
                converted_postfix_stack.append(int(item))
            else:
                converted_postfix_stack.append(get_variable_value(item))
        else:
            converted_postfix_stack.append(item)
    return converted_postfix_stack

def perform_postfix_calculation(first_number, operator, second_number):
    """ Decodes the operator string and performs the required calculation

    first_number: integer
    operator: string
    second_number: integer
    """
    result = 0
    if operator == operator_symbols[OperatorSymbol.PLUS]:
       result = first_number + second_number
    elif operator == operator_symbols[OperatorSymbol.MINUS]:
        result = first_number - second_number
    elif operator == operator_symbols[OperatorSymbol.TIMES]:
        result = first_number * second_number
    elif operator == operator_symbols[OperatorSymbol.POWER]:
        result = first_number ** second_number
    elif operator == operator_symbols[OperatorSymbol.DIVISION]:
        try:
            first_number / second_number
        except ZeroDivisionError:
            result = 'NaN'
        else:
            result = first_number / second_number
    return result

def get_variable_value(variable):
    return variables_dict[variable]

def command_handler(input_):
    """ Checks if the command is in the list of commands

    Returns the command description if available, otherwise will let the user know that know that command is unkown
    """
    global keep_going
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
    elif input_.endswith(operator_symbols[OperatorSymbol.TIMES]):
        result = False
    elif input_.endswith(operator_symbols[OperatorSymbol.POWER]):
        result = False
    elif input_.endswith(operator_symbols[OperatorSymbol.DIVISION]):
        result = False
    elif input_.endswith(bracket_symbols[BracketSymbol.OPEN]):
        result = False
    elif input_.startswith(operator_symbols[OperatorSymbol.TIMES]):
        result = False
    elif input_.startswith(operator_symbols[OperatorSymbol.POWER]):
        result = False
    elif input_.startswith(bracket_symbols[BracketSymbol.CLOSE]):
        result = False
    elif contains_operator_symbols(input_) or contains_brackets(input_):
        if not check_for_valid_math(input_):
            result = False
        elif not check_all_variables_declared(input_):
            result = False
    return result

def check_all_variables_declared(input_):
    result = True
    input_list = convert_input_to_list(analyse_input(input_), input_)
    for item in input_list:
        if is_variable(item):
            try:
                variables_dict[item]
            except KeyError:
                result = False
    return result

def check_for_valid_math(input_):
    result = True
    try:
        input_list = convert_input_to_list(analyse_input(input_), input_)
    except Exception:
        result = False
    else:
        if contains_brackets(input_):
            if not check_for_matching_brackets(input_):
                result = False
        for item in input_list:
            if contains_plus_or_minus(item) and contains_multiplication_or_division(item):
                result = False
            elif contains_multiplication_or_division(item) and len(item) > 1:
                result = False
    return result

def check_for_matching_brackets(input_):
    """ The number of opening brackets should match the number of closing brackets

    If there is a closing bracket before an opening bracket the function should return False
    """
    result = False
    stack = []
    error_counter = 0
    for symbol in input_:
        if symbol == bracket_symbols[BracketSymbol.OPEN]:
            stack.append(symbol)
        if symbol == bracket_symbols[BracketSymbol.CLOSE]:
            try:
                stack.pop()
            except IndexError:
                error_counter += 1
    if len(stack) == 0 and error_counter == 0:
        result = True
    return result

def contains_brackets(input_):
    return bracket_symbols[BracketSymbol.OPEN] in input_ or bracket_symbols[BracketSymbol.CLOSE] in input_

def contains_plus_or_minus(input_):
    return operator_symbols[OperatorSymbol.PLUS] in input_ or operator_symbols[OperatorSymbol.MINUS] in input_

def contains_multiplication_or_division(input_):
    return operator_symbols[OperatorSymbol.TIMES] in input_ or operator_symbols[OperatorSymbol.DIVISION] in input_

def contains_operator_symbols(input_):
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

def is_variable(input_):
    result = True
    for letter in input_:
        if letter not in all_letters:
            result = False
    return result

def input_handler(input_):
    """ Checks the user input and passes it to the correct function
    
    The guardian will check if the input format is technically correct and contains no undeclared variables
    input that starts with "/" has to go to the command function
    input lines only containing the variable name should print the variable content
    input lines only containing a single number should print that number
    other input will be calculated
    """
    if input_guardian(input_):
        if input_.startswith(command_start_symbol):
            command_handler(input_)
        elif is_empty_line(input_):
            pass
        elif equality_symbols[EqualitySymbol.EQUAL] not in input_ and is_single_number(input_):
            print(convert_single_number(input_))
        elif equality_symbols[EqualitySymbol.EQUAL] in input_:
            variable_assignment(input_)
        elif check_for_variables(input_) and not contains_operator_symbols(input_):
            print_variable_content(input_)
        else:        
            print(postfix_calculation(convert_input(input_)))
    elif not input_guardian(input_):
        if not check_all_variables_declared(input_):
            print(user_outputs[UserOutput.UNKNOW_VARIABLE])
        else:
            print(user_outputs[UserOutput.INVALID_EXPRESSION])

def calculator_loop():
    global keep_going, operator_symbols, commands, user_outputs, variables_dict, all_letters
    while keep_going:
        input_ = input()
        input_handler(input_)

if __name__ == "__main__":
    calculator_loop()
    #print(postfix_calculation(convert_input('-(2+3)')))
    #print(postfix_calculation(convert_input('-2+3')))