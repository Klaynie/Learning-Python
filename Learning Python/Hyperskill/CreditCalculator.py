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

class MonthMessage(IntEnum):
    COUNT_OF_MONTHS_1 = 0
    COUNT_OF_MONTHS_N = 1

class PaymentMessage(IntEnum):
    EVEN_MONTHLY_PAYMENT = 0
    ADJUSTED_PAYMENT = 1

keywords = ['m', 'p']
user_prompts = [f'What do you want to calculate?\n\
type "{keywords[Keyword.MONTHS]}" - for count of months,\n\
type "{keywords[Keyword.PAYMENT]}" - for monthly payment:',
'Enter the credit principal:',\
'Enter monthly payment:',\
'Enter count of months:'\
]

def get_value(prompt):
    return input(prompt + '\n')

def get_monthly_payment_message(monthly_payment = 100, monthly_payment_last_month_adjustment = 0):
    result = ''
    monthly_payment_messages = [f'Your monthly payment = {monthly_payment:d}',
                                f'Your monthly payment = {monthly_payment:d} with last month payment = {monthly_payment + monthly_payment_last_month_adjustment:d}',
                              ]
    if monthly_payment_last_month_adjustment == 0:
        result = monthly_payment_messages[PaymentMessage.EVEN_MONTHLY_PAYMENT]
    else:
        result = monthly_payment_messages[PaymentMessage.ADJUSTED_PAYMENT]
    return result

def get_count_of_month_message(count_of_months = 1):
    result = ''
    count_of_month_messages = [f'It takes {count_of_months} month to repay the credit',
                               f'It takes {count_of_months} months to repay the credit'
                            ]
    if count_of_months == 1:
        result = count_of_month_messages[MonthMessage.COUNT_OF_MONTHS_1]
    else:
        result = count_of_month_messages[MonthMessage.COUNT_OF_MONTHS_N]
    return result

def calculate_count_of_month(principal = 1000, monthly_payment = 1000):
    return math.ceil(principal / monthly_payment)

def calculate_monthly_payment(principal = 1000, count_of_months = 9):
    monthly_payment = math.ceil(principal / count_of_months)
    monthly_payment_last_month_adjustment =  math.ceil(principal - (count_of_months - 1) *  monthly_payment) - monthly_payment
    return monthly_payment, monthly_payment_last_month_adjustment

def monthly_payment_calculator(principal):
    count_of_months = get_value(user_prompts[UserPrompt.COUNT_OF_MONTHS])
    monthly_payment, monthly_payment_last_month_adjustment = calculate_monthly_payment(principal, int(count_of_months))
    result = get_monthly_payment_message(monthly_payment, monthly_payment_last_month_adjustment)
    return result

def count_of_months_calculator(principal):
    monthly_payment = get_value(user_prompts[UserPrompt.MONTHLY_PAYMENT])
    count_of_months = calculate_count_of_month(principal, int(monthly_payment))
    result = get_count_of_month_message(count_of_months)
    return result

def start_calculation(keyword, principal):
    result = ''
    if keyword == keywords[Keyword.MONTHS]:
        result = count_of_months_calculator(principal)
    elif keyword == keywords[Keyword.PAYMENT]:
        result = monthly_payment_calculator(principal)
    return result

def print_result(result):
    print('\n')
    print(result)

def request_inputs():
    principal = get_value(user_prompts[UserPrompt.PRINCIPAL])
    keyword = get_value(user_prompts[UserPrompt.KEYWORD])
    return principal, keyword

def calculator_loop():
    global keywords, user_prompts
    keep_going = True
    while keep_going:
        principal, keyword = request_inputs()
        result = start_calculation(keyword, int(principal))
        print_result(result)
        keep_going = False

if __name__ == "__main__":
    calculator_loop()