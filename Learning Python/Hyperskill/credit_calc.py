from enum import IntEnum
import math
import sys
import argparse

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

class CommandLineKeyword(IntEnum):
    ANNUITY = 0
    DIFFERANTIATE = 1

class PaydownText(IntEnum):
    ONE_YEAR = 0
    N_YEARS = 1
    ONE_MONTH = 2
    N_MONTHS = 3
    CONCATENATION = 4

class GuardianText(IntEnum):
    INCORRECT_PARAMETERS = 0

keywords = ['n', 'a', 'p']
command_line_keywords = ['annuity', 'diff']
user_prompts = [f'What do you want to calculate?\n\
type "{keywords[Keyword.MONTHS]}" - for count of months,\n\
type "{keywords[Keyword.PAYMENT]}" - for monthly payment:\n\
type  "{keywords[Keyword.PRINCIPAL]}" - for credit principal:',
'Enter the credit principal:',\
'Enter monthly payment:',\
'Enter count of periods:',\
'Enter credit interest:'
]
guardian_texts = ['Incorrect parameters']

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
        result = float(user_input) / 100 / 12
    return result

def convert_user_input_months(user_input):
    try:
        int(user_input)
    except Exception:
        result = 12
    else:
        result = int(user_input)
    return result

def calculate_overpayment():
    return 1

def generate_paydown_time_text(years, months):
    paydown_time_texts = [f'{years} year',\
             f'{years} years',\
             f'{months} month',\
             f'{months} months',\
             ' and '
            ]
    if years == 0:
        year_text = ''
    elif years == 1:
        year_text = paydown_time_texts[PaydownText.ONE_YEAR]
    elif years > 1:
        year_text = paydown_time_texts[PaydownText.N_YEARS]
    if months == 0:
        month_text = ''
    elif months == 1:
        month_text = paydown_time_texts[PaydownText.ONE_MONTH]
    elif months > 1:
        month_text = paydown_time_texts[PaydownText.N_MONTHS]
    if year_text == '' or month_text == '':
        concatenation = ''
    elif year_text != '' and month_text != '':
        concatenation = paydown_time_texts[PaydownText.CONCATENATION]
    result = year_text + concatenation + month_text
    return result

def convert_paydown_time_to_years_and_months(paydown_time):
    years, months = paydown_time // 12, paydown_time % 12
    return years, months

def calculate_paydown_time(principal, monthly_payment, interest):
    result = math.ceil(math.log(monthly_payment / (monthly_payment - interest * principal) , (1 + interest)))
    return result

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
    paydown_time = calculate_paydown_time(converted_principal, converted_monthly_payment, converted_interest)
    years, months = convert_paydown_time_to_years_and_months(paydown_time)
    result = generate_paydown_time_text(years, months)
    return result

def calculate_principal(monthly_payment, months, interest):
    result = math.floor(monthly_payment / ((interest * (1 + interest) ** months) / ((1 + interest) ** months - 1)))
    return result

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
    result = math.ceil(principal * (interest * (1 + interest) ** months) / ((1 + interest) ** months - 1))
    return result

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

def get_guardian_message():
    global guardian_texts
    result = guardian_texts[GuardianText.INCORRECT_PARAMETERS]
    return result

def command_line_guardian(user_input):
    result = True
    return result

def check_calculation_type(calculation_type):
    result = True
    if calculation_type not in [command_line_keywords[CommandLineKeyword.ANNUITY], command_line_keywords[CommandLineKeyword.DIFFERANTIATE]]:
        result = False
    return result

def check_command_line_input(user_input):
    result = True
    if not command_line_guardian(user_input):
        result = False
    elif not check_calculation_type(user_input.type):
        result = False
    return result

def get_command_line_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', help='specify calculation type ("annuity" or "diff")')
    parser.add_argument('--principal', help='amount of money lent')
    parser.add_argument('--periods', help='duration of credit in months')
    parser.add_argument('--interest', help='interest rate in percantage (5 = 5%, 100 = 100%)')
    parser.add_argument('--payment', help='monthly annuity payment amount')
    result = parser.parse_args()
    return result

def command_line_handler():
    user_input = get_command_line_input()
    if not check_command_line_input(user_input):
        result = get_guardian_message()
    else:
        result = '1'
    return result

if __name__ == "__main__":
    result = command_line_handler()
    print(result)