commands = ['/exit','/help']
user_outputs = ['Bye!','The program calculates the sum of numbers']

def input_handler(input_):
    return sum([int(number) for number in input_.split()])

keep_going = True
while keep_going:
    input_ = input()
    if input_ == commands[0]:
        print(user_outputs[0])
        keep_going = False
    elif input_ == commands[1]:
        print(user_outputs[1])
    elif input_ == '':
        pass
    elif ' ' not in input_:
        print(input_)
    else:
        print(input_handler(input_))        