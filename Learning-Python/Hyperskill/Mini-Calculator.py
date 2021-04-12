from enum import IntEnum

class OperatorSymbol(IntEnum):
    PLUS = 0
    MINUS = 1
    TIMES = 2

operator_symbols = ['+', '-', '*']

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def perform_calculation(equation_list):
    result = 0
    num1 = float(equation_list[0])
    num2 = float(equation_list[2])
    calculation_symbol = equation_list[1]
    if calculation_symbol == operator_symbols[OperatorSymbol.PLUS]:
        result = add(num1, num2)
    elif calculation_symbol == operator_symbols[OperatorSymbol.MINUS]:
        result = subtract(num1, num2)
    elif calculation_symbol == operator_symbols[OperatorSymbol.TIMES]:
        result = multiply(num1, num2)
    return int(result)

def main():
    equation = input()
    equation_list = equation.split(' ')
    result = perform_calculation(equation_list)
    print(result)

main()
