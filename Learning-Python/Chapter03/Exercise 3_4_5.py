def do_twice(function_in_do_twice,argument_in_do_twice):
    function_in_do_twice(argument_in_do_twice)
    function_in_do_twice(argument_in_do_twice)

def do_four(function_in_do_four,argument_in_do_four):
    do_twice(function_in_do_four,argument_in_do_four)
    do_twice(function_in_do_four,argument_in_do_four)

def print_twice(text_in):
    print(text_in)
    print(text_in)

do_four(print_twice, 'Spam'*5)