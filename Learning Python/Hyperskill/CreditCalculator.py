from enum import IntEnum
import math

class UserPrompt(IntEnum):
    KEYWORD = 0
    PRINCIPAL = 1
    MONTHLY_PAYMENT = 2
    COUNT_OF_MONTHS = 3

class Keyword(IntEnum):
    MONTHS = 0
    PAYMENT = 1

class UserMessage(IntEnum):
    MONTHLY_PAYMENTS_EVEN = 0
    MONTHLY_PAYMENTS_ODD = 1
    COUNT_OF_MONTHS_1 = 2
    COUNT_OF_MONTHS_N = 3

keywords = ['m', 'p']
user_prompts = [f'What do you want to calculate?\n\
type "{keywords[Keyword.MONTHS]}" - for count of months,\n\
type "{keywords[Keyword.PAYMENT]}" - for monthly payment:',
'Enter the credit principal:',\
'Enter monthly payment:',\
'Enter count of months:'\
]

def print_monthly_payment_messages(monthly_payment_even = 0, monthly_payment_odd = 0):
    monthly_payment_messages = [f'Your monthly payment = {monthly_payment_even:.d}',
                     f'Your monthly payment = {monthly_payment_even:.d} with last month payment = {monthly_payment_odd:.d}',
                    ]
    print(monthly_payment_messages[0])

def print_count_of_month_messages(count_of_months = 1):
    count_of_month_messages = [f'It takes {count_of_months} month to repay the credit',
                               f'It takes {count_of_months} months to repay the credit'
                            ]
    print(count_of_month_messages[0])

def calculate_count_of_months(principal = 1000, monthly_payment = 1000):
    return 1

def calculate_monthly_payments(principal = 1000, count_of_months = 9):
    monthly_payment_even = math.ceil(principal / count_of_months)
    monthly_payment_odd = math.ceil(principal - (count_of_months - 1) *  monthly_payment_even)
    return monthly_payment_even, monthly_payment_odd

def get_value(prompt):
    return input(prompt + '\n')

def monthly_payment_calculator(principal):
    count_of_months = get_value(user_prompts[UserPrompt.COUNT_OF_MONTHS])
    monthly_payment_even, monthly_payment_odd = calculate_monthly_payments(principal, count_of_months)
    print_monthly_payment_messages(monthly_payment_even, monthly_payment_odd)

def count_of_months_calculator(principal):
    monthly_payment = get_value(user_prompts[UserPrompt.MONTHLY_PAYMENT])
    count_of_months = calculate_count_of_months(principal, monthly_payment)
    print_count_of_month_messages(count_of_months)

def start_calculation(keyword, principal):
    if keyword == keywords[Keyword.MONTHS]:
        count_of_months_calculator(principal)
    elif keyword == keywords[Keyword.PAYMENT]:
        monthly_payment_calculator(principal)

def request_inputs():
    principal = get_value(user_prompts[UserPrompt.PRINCIPAL])
    keyword = get_value(user_prompts[UserPrompt.KEYWORD])
    start_calculation(keyword, principal)

def calculator_loop():
    global keywords, user_prompts
    keep_going = True
    while keep_going:
        request_inputs()
        keep_going = False

#calculator_loop()
print(calculate_monthly_payments())
print(calculate_monthly_payments())
print(calculate_monthly_payments())