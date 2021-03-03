"""
We have a predefined function that takes a name and prints a greeting message with this name:

def greetings(name):
    print('Hello,', name)

Now, write a decorator @morning that will print another string, saying 'Good morning' after the greeting. Below you can see the result of the function with the decorator and the input name Susie:

# Hello, Susie
# Good morning, Susie

You do not need to take any input or call a function, just write the body of the decorator.
"""


def morning(func):
    def wrapper(arg):
        func(arg)
        print('Good morning,', arg)

    return wrapper


@morning
def greetings(name):
    print('Hello,', name)


greetings("Susie")
