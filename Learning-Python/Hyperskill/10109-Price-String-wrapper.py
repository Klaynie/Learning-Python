"""
Below, we have written the decorator price_string. The function takes another function with one parameter as its argument, converts its output to a string, and adds the pound sign to this string to represent the price of a product.

def price_string(func):
    def wrapper(quantity):
        return "£" + str(func(quantity))

    return wrapper

Your task is to:

    - write the body of the function new_price : it should take an argument and return the float value with a 10% discount
    - decorate the function with the decorator price_string

For example, for the input value 100, the decorated function should return £90.0.

You do not need to take any input, just write the body of the function and decorate it.
"""


def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper


@price_string
def new_price(float_in):
    discount = 0.1  # 10%
    return (1 - discount) * float_in
