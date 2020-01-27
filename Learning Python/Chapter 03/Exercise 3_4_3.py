def do_twice(function_in_do_twice,argument_in_do_twice):
    function_in_do_twice(argument_in_do_twice)
    function_in_do_twice(argument_in_do_twice)
def do_four(function_in_do_four,argument_in_do_four):
    do_twice(function_in_do_four,argument_in_do_four)
    do_twice(function_in_do_four,argument_in_do_four)
def print_tx(text_in):
    print(text_in)
do_four(print_tx, 'Show me what you got')
input("Press a key to exit")