def do_twice(function_in,argument_in):
    function_in(argument_in)
    function_in(argument_in)

def print_tx(text_in):
    print(text_in)

do_twice(print_tx, "Spam"*3)