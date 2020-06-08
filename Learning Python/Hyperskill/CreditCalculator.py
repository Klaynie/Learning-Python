from enum import IntEnum
import math

class UserPrompt(IntEnum):
    KEYWORD = 0
    PRINCIPAL = 1
    MONTHLY_PAYMENT = 2
    MONTHS = 3
    INTEREST = 4

class Keyword(IntEnum):
    MONTHS = 0
    PAYMENT = 1
    PRINCIPAL = 2

keywords = ['m', 'a', 'p']
user_prompts = [f'What do you want to calculate?\n\
type "{keywords[Keyword.MONTHS]}" - for count of months,\n\
type "{keywords[Keyword.PAYMENT]}" - for monthly payment:\n\
type  "{keywords[Keyword.PRINCIPAL]}" - for credit principal:',
'Enter the credit principal:',\
'Enter monthly payment:',\
'Enter count of periods:',\
'Enter credit interest:'
]

def get_value(prompt):
    return input(prompt + '\n')

def generate_message(number, variable):
    result = ''
    messages = [f'You need {variable} to repay this credit!',\
                f'Your annuity payment = {variable}!',\
                f'Your credit principal = {variable}!'
    ]
    result = messages[number]
    return result

def calculate_paydown_time(principal, monthly_payment, interest):
    return 1

def paydown_time_calculator(principal, monthly_payment, interest):
    principal = get_value(user_prompts[UserPrompt.PRINCIPAL])
    monthly_payment = get_value(user_prompts[UserPrompt.MONTHLY_PAYMENT])
    interest = get_value(user_prompts[UserPrompt.INTEREST])
    result = calculate_paydown_time(principal, monthly_payment, interest)
    return result

def calculate_principal(monthly_payment, months, interest):
    return 1

def principal_calculator():
    monthly_payment = get_value(user_prompts[UserPrompt.MONTHLY_PAYMENT])
    months = get_value(user_prompts[UserPrompt.MONTHS])
    interest = get_value(user_prompts[UserPrompt.INTEREST])
    result = calculate_principal(monthly_payment, months, interest)
    return result

def calculate_monthly_payment(principal, months, interest):
    monthly_payment = 1
    return monthly_payment

def monthly_payment_calculator():
    principal = get_value(user_prompts[UserPrompt.PRINCIPAL])
    months = get_value(user_prompts[UserPrompt.MONTHS])
    interest = get_value(user_prompts[UserPrompt.INTEREST])
    result = calculate_monthly_payment(principal, months, interest)
    return result

def get_output_value(keyword):
    result = 0
    if keyword == keywords[Keyword.MONTHS]:
        result = paydown_time_calculator()
    elif keyword == keywords[Keyword.PAYMENT]:
        result = monthly_payment_calculator()
    elif keyword == keywords[Keyword.PRINCIPAL]:
        result = principal_calculator()
    return result

def get_number(keyword):
    if keyword == keywords[Keyword.MONTHS]:
        result = Keyword.MONTHS
    elif keyword == keywords[Keyword.PAYMENT]:
        result = Keyword.PAYMENT
    elif keyword == keywords[Keyword.PRINCIPAL]:
        result = Keyword.PRINCIPAL
    return result

def print_result(result):
    print('\n')
    print(result)

def calculator_loop():
    global keywords, user_prompts
    keep_going = True
    while keep_going:
        keyword = get_value(user_prompts[UserPrompt.KEYWORD])
        number = get_number(keyword)
        variable = get_output_value(keyword)
        result = generate_message(number, variable)
        print_result(result)
        keep_going = False

if __name__ == "__main__":
    calculator_loop()