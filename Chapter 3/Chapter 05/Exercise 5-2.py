def print_arg(arg):
    print(arg)

def do_n(f, arg, n):
    if n <= 0:
       return
    f(arg)
    do_n(f, arg, n-1)
        
do_n(print_arg, 'Hello World', 5)