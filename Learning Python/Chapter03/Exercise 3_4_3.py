def do_twice(function_in,argument_in):
    function_in(argument_in)
    function_in(argument_in)

def print_twice(text_in):
    print(text_in)
    print(text_in)

do_twice(print_twice, "Spam"*3)