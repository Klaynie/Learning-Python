# 1. Functions are objects
def add_five(num):
    print(num +5)

# print(add_five)

# 2. Functions within functions
def add_five(num):
    def add_two(num):
        return num + 2
    
    num_plus_two = add_two(num)
    print(num_plus_two + 3)

# add_two(7)
# add_five(10)

# 3. Returning functions from fuctions
def get_math_function(operation):
    def add(num1, num2):
        return num1 + num2
    
    def sub(num1, num2):
        return num1 - num2
    
    if operation == '+':
        return add
    elif operation == '-':
        return sub

# add_function = get_math_function('+')
# sub_function = get_math_function('-')
# print(add_function(4, 6))
# print(sub_function(4, 6))

# 4. Decorating a function
def title_decorator(print_name_function):
    def wrapper():
        print('Sir')
        print_name_function()
    return wrapper

def print_my_name():
    print('Earl')

def print_joes_name():
    print('Joe')

# decorated_function1 = title_decorator(print_my_name)
# decorated_function1()

# decorated_function2 = title_decorator(print_joes_name)
# decorated_function2()

# 5. Decorators
def title_decorator(print_name_function):
    def wrapper():
        print('Sir')
        print_name_function()
    return wrapper

@title_decorator
def print_my_name():
    print('Earl')

@title_decorator
def print_joes_name():
    print('Joe')

# print_my_name()

# 6. Decorators w/ Parameters
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print('Sir')
        print_name_function(*args, **kwargs)
    return wrapper

@title_decorator
def print_name(name, age):
    print(f"{name} you are {age}")

print_name('Shelby', 50)