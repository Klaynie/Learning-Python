def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

print(multiply(5))

print(multiply(5, 10))