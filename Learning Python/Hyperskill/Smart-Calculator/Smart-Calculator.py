keep_going = True
while keep_going:
    input_ = input()
    if input_ == '/exit':
        keep_going = False
    elif input_ == '':
        pass
    elif ' ' not in input_:
        print(input_)
    else:
        input_list = input_.split()
        number_list = [int(number) for number in input_list]
        print(number_list[0] + number_list[1])