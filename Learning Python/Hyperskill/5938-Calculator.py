# put your python code here
addition_operator = '+'
subtraction_operator = '-'
multiplication_operator = '*'
power_operator = 'pow'
division_operator = '/'
floor_division_operator = 'div'
modulo_operator = 'mod'

operators_to_check = [division_operator, modulo_operator, floor_division_operator]

first_number = float(input())
second_number = float(input())
operator = input()

if second_number == 0 and operator in operators_to_check:
    print("Division by 0!")
elif operator == addition_operator:
    print(first_number + second_number)
elif operator == subtraction_operator:
    print(first_number - second_number)
elif operator == multiplication_operator:
    print(first_number * second_number)
elif operator == power_operator:
    print(first_number ** second_number)
elif operator == division_operator:
    print(first_number / second_number)
elif operator == floor_division_operator:
    print(first_number // second_number)
elif operator == modulo_operator:
    print(first_number % second_number)
else:
    print("No valid operator provided")