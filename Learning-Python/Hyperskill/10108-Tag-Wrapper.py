"""
Here we have a predefined function that receives some user input and removes, if necessary, all extra spaces at the beginning and at the end of a line using the built-in function strip().

def from_input(inp):
    string = inp.strip()
    return string

Create the body of a @tagged decorator that will return the string wrapped in the <title></title> HTML tag. For example, for the word Test it should output <title>Test</title>. You do not need to take any input or call a function, just write the body of the decorator.
"""


def tagged(func):
    def wrapper(arg):
        return "<title>" + str(func(arg)) + "</title>"

    return wrapper


@tagged
def from_input(inp):
    string = inp.strip()
    return string


inp = "Test"

print(from_input(inp))
