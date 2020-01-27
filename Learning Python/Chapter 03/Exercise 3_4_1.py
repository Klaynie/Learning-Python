def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
do_twice(print_spam)
input("Press a key to exit")