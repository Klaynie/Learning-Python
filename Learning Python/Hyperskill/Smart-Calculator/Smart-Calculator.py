commands = ['/exit','/help']
user_outputs = ['Bye!','The program calculates the sum of numbers']
keep_going = True

def is_empty_line(input_):
    return input_ == ''

def is_single_number(input_):
    return ' ' not in input_

def sum_(input_):
    return sum([int(number) for number in input_.split()])

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
        print(sum_(input_))

def calculator_loop():
    global keep_going
    while keep_going:
        input_ = input()
        input_handler(input_)

calculator_loop()