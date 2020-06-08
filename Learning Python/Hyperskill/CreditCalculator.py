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

def convert_user_input_principal(user_input):
    try:
        float(user_input)
    except Exception:
        result = 1000000
    else:
        result = float(user_input)
    return result

def convert_user_input_monthly_payment(user_input):
    try:
        float(user_input)
    except Exception:
        result = 15000
    else:
        result = float(user_input)
    return result

def convert_user_input_interest(user_input):
    try:
        float(user_input)
    except Exception:
        result = 10
    else:
        result = float(user_input) / 100
    return result

def convert_user_input_months(user_input):
    try:
        int(user_input)
    except Exception:
        result = 12
    else:
        result = int(user_input)
    return result

def calculate_paydown_time(principal, monthly_payment, interest):
    return 1

def convert_paydowm_time_input(principal, monthly_payment, interest):
    converted_principal = convert_user_input_principal(principal)
    converted_monthly_payment = convert_user_input_monthly_payment(monthly_payment)
    converted_interest = convert_user_input_interest(interest)
    return converted_principal, converted_monthly_payment, converted_interest

def get_paydowm_time_input():
    principal = get_value(user_prompts[UserPrompt.PRINCIPAL])
    monthly_payment = get_value(user_prompts[UserPrompt.MONTHLY_PAYMENT])
    interest = get_value(user_prompts[UserPrompt.INTEREST])
    return principal, monthly_payment, interest

def paydown_time_calculator():
    principal, monthly_payment, interest = get_paydowm_time_input()
    converted_principal, converted_monthly_payment, converted_interest = convert_paydowm_time_input(principal, monthly_payment, interest)
    result = calculate_paydown_time(converted_principal, converted_monthly_payment, converted_interest)
    return result

def calculate_principal(monthly_payment, months, interest):
    return 1

def convert_principal_input(monthly_payment, months, interest):
    converted_monthly_payment = convert_user_input_monthly_payment(monthly_payment)
    converted_months = convert_user_input_months(months)
    converted_interest = convert_user_input_interest(interest)
    return converted_monthly_payment, converted_months, converted_interest

def get_principal_input():
    monthly_payment = get_value(user_prompts[UserPrompt.MONTHLY_PAYMENT])
    months = get_value(user_prompts[UserPrompt.MONTHS])
    interest = get_value(user_prompts[UserPrompt.INTEREST])
    return monthly_payment, months, interest

def principal_calculator():
    monthly_payment, months, interest = get_principal_input()
    converted_monthly_payment, converted_months, converted_interest = convert_principal_input(monthly_payment, months, interest)
    result = calculate_principal(converted_monthly_payment, converted_months, converted_interest)
    return result

def calculate_monthly_payment(principal, months, interest):
    monthly_payment = 1
    return monthly_payment

def convert_monthly_payment_input(principal, months, interest):
    converted_principal = convert_user_input_principal(principal)
    converted_months = convert_user_input_months(months)
    converted_interest = convert_user_input_interest(interest)
    return converted_principal, converted_months, converted_interest

def get_monthly_payment_input():
    principal = get_value(user_prompts[UserPrompt.PRINCIPAL])
    months = get_value(user_prompts[UserPrompt.MONTHS])
    interest = get_value(user_prompts[UserPrompt.INTEREST])
    return principal, months, interest

def monthly_payment_calculator():
    principal, months, interest = get_monthly_payment_input()
    converted_principal, converted_months, converted_interest = convert_monthly_payment_input(principal, months, interest)
    result = calculate_monthly_payment(converted_principal, converted_months, converted_interest)
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