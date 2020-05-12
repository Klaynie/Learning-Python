for number in range(1, 101):
    output_string = ''
    if number % 3 == 0:
        output_string += 'Fizz'
    if number % 5 == 0:
        output_string += 'Buzz'
    print(output_string if output_string != '' else number)