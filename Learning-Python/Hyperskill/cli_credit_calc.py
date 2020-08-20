from enum import IntEnum
import math
import sys
import argparse

class UserInput(object):

    def __init__(self):
        self.type = None
        self.principal = None
        self.periods = None
        self.interest = None
        self.payment = None

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

command_line_keywords = ['annuity', 'diff']
guardian_texts = ['Incorrect parameters']

# getters

def get_number(user_input):
    result = 0
    if user_input.principal == None:
        result = Keyword.PRINCIPAL
    if user_input.payment == None:
        result = Keyword.PAYMENT
    if user_input.periods == None:
        result = Keyword.MONTHS
    return result

def get_calculation_types():
    return [command_line_keywords[CommandLineKeyword.ANNUITY], command_line_keywords[CommandLineKeyword.DIFFERANTIATE]]

def get_command_line_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', help='specify calculation type ("annuity" or "diff")')
    parser.add_argument('--principal', help='amount of money lent')
    parser.add_argument('--periods', help='duration of credit in months')
    parser.add_argument('--interest', help='interest rate in percantage (5 = 5%, 100 = 100%)')
    parser.add_argument('--payment', help='monthly annuity payment amount')
    result = parser.parse_args()
    return result

def get_year_text(years, paydown_time_texts):
    one_year_text = paydown_time_texts[PaydownText.ONE_YEAR]
    multiple_year_text = paydown_time_texts[PaydownText.N_YEARS]
    result = one_year_text if years == 1 else multiple_year_text
    return result

def get_month_text(months, paydown_time_texts):
    one_month_text = paydown_time_texts[PaydownText.ONE_MONTH]
    multiple_month_text = paydown_time_texts[PaydownText.N_MONTHS]
    result = one_month_text if months == 1 else multiple_month_text
    return result

# generaters

def generate_message(number, variable, convert_variable=False):
    result = ''
    if convert_variable == True:
        years, months = convert_paydown_time_to_years_and_months(variable)
        variable = generate_paydown_time_text(years, months)
    messages = [f'You need {variable} to repay this credit!',\
                f'Your annuity payment = {variable}!',\
                f'Your credit principal = {variable}!'
    ]
    result = messages[number]
    return result

def generate_year_text(years, paydown_time_texts):
    result = ''
    if years:
        result = get_year_text(years, paydown_time_texts)
    return result

def generate_month_text(months, paydown_time_texts):
    result = ''
    if months:
        result = get_month_text(months, paydown_time_texts)
    return result

def generate_year_and_month_text(year_text, month_text, paydown_time_texts):
    result = ''
    concatenation = paydown_time_texts[PaydownText.CONCATENATION]
    if not year_text or not month_text:
        concatenation = ''
    result = year_text + concatenation + month_text
    return result

def generate_paydown_time_text(years, months):
    result = ''
    paydown_time_texts = [f'{years} year',\
                          f'{years} years',\
                          f'{months} month',\
                          f'{months} months',\
                          ' and ']
    year_text = generate_year_text(years, paydown_time_texts)
    month_text = generate_month_text(months, paydown_time_texts)
    result = generate_year_and_month_text(year_text, month_text, paydown_time_texts)
    return result

def generate_diff_message(month, payment):
    return f'Month {month}: paid out {payment}\n'

# converters

def convert_user_input_for_calculation(user_input):
    result = UserInput()
    result.type = user_input.type
    if user_input.principal != None:
        result.principal = convert_user_input_principal(user_input.principal)
    if user_input.payment != None:
        result.payment = convert_user_input_monthly_payment(user_input.payment)
    if user_input.periods != None:
        result.periods = convert_user_input_months(user_input.periods)
    if user_input.interest != None:
        result.interest = convert_user_input_interest(user_input.interest)
    return result

def convert_paydown_time_to_years_and_months(paydown_time):
    years, months = paydown_time // 12, paydown_time % 12
    return years, months

def convert_user_input_principal(user_input):
    return float(user_input)

def convert_user_input_monthly_payment(user_input):
    return float(user_input)

def convert_user_input_interest(user_input):
    return float(user_input) / 100 / 12

def convert_user_input_months(user_input):
    return int(user_input)

# calculators

def calculate_actual_payment_diff(user_input):
    result = 0
    month = 1
    while month <= user_input.periods:
        result += calculate_diff_payment(user_input, month)
        month += 1
    return result

def calculate_actual_payment_annuity(user_input):
    result = 0
    if is_direct_actual_payment_annuity_calculation(user_input):
        result = user_input.periods \
                 * user_input.payment
    elif is_missing_payment_amount_for_actual_payment_annuity_calculation(user_input):
        result = user_input.periods \
                 * calculate_missing_value(user_input)
    elif is_missing_periods_for_actual_payment_annuity_calculation(user_input):
        result = calculate_missing_value(user_input) \
                 * user_input.payment
    return result

def calculate_actual_payment(user_input):
    result = 0
    if user_input.type == command_line_keywords[CommandLineKeyword.DIFFERANTIATE]:
        result = calculate_actual_payment_diff(user_input)
    elif user_input.type == command_line_keywords[CommandLineKeyword.ANNUITY]:
        result = calculate_actual_payment_annuity(user_input)
    return result

def calculate_payment(user_input):
    result = 0
    if user_input.principal != None:
        result = user_input.principal
    else:
        result = calculate_missing_value(user_input)
    return result

def calculate_overpayment(user_input):
    result = round(calculate_actual_payment(user_input) - calculate_payment(user_input))
    return result

def calculate_paydown_time(principal, monthly_payment, interest):
    result = math.ceil( \
                math.log( \
                    monthly_payment \
                    / (monthly_payment \
                      - interest \
                      * principal \
                    ) \
                , (1 + interest) \
                ) \
             )
    return result

def calculate_principal(monthly_payment, months, interest):
    result = math.floor(monthly_payment \
                         / ((interest * (1 + interest) ** months) \
                             / ((1 + interest) ** months - 1)))
    return result

def calculate_monthly_payment(principal, months, interest):
    result = math.ceil(principal * (interest * (1 + interest) ** months) / ((1 + interest) ** months - 1))
    return result

def overpayment_calculation(user_input):
    result = f"\nOverpayment = {calculate_overpayment(user_input)}"
    return result

def annuity_calculation(user_input):
    result = ''
    number = get_number(user_input)
    value = calculate_missing_value(user_input)
    convert_variable = needs_variable_conversion(user_input)
    result = generate_message(number, value, convert_variable)
    return result

def calculate_missing_value(user_input):
    result = 0
    if user_input.principal == None:
        result = calculate_principal(user_input.payment, user_input.periods, user_input.interest)
    if user_input.payment == None:
        result = calculate_monthly_payment(user_input.principal, user_input.periods, user_input.interest)
    if user_input.periods == None:
        result = calculate_paydown_time(user_input.principal, user_input.payment, user_input.interest)
    return result

def calculate_diff_payment(user_input, month):
    result = user_input.principal \
                  / user_input.periods \
                  + user_input.interest \
                    * (user_input.principal \
                        - (user_input.principal \
                            * (month \
                            - 1
                              ) \
                          / user_input.periods
                          )
                      )
    result = math.ceil(result)
    return result

def diff_calculation(user_input):
    result = ''
    month = 1
    while month <= user_input.periods:
        result += generate_diff_message(month, calculate_diff_payment(user_input, month))
        month += 1
    return result

def start_calculation(user_input):
    result = ''
    if user_input.type == command_line_keywords[CommandLineKeyword.ANNUITY]:
        result = annuity_calculation(user_input)
    elif user_input.type == command_line_keywords[CommandLineKeyword.DIFFERANTIATE]:
        result = diff_calculation(user_input)
    result += overpayment_calculation(user_input)
    return result

# checks

def command_line_guardian(user_input):
    result = True
    if count_values(user_input) < 4:
        result = False
    elif count_values(user_input) == 5:
        result = False
    if not can_convert(user_input):
        result = False
    return result

def count_values(user_input):
    result = 0
    if user_input.type != None:
        result += 1
    if user_input.principal != None:
        result += 1
    if user_input.periods != None:
        result += 1
    if user_input.interest != None:
        result += 1
    if user_input.payment != None:
        result += 1
    return result

def can_convert(user_input):
    result = True
    if user_input.principal != None:
        try:
            float(user_input.principal)
        except Exception:
            result = False
        else:
            if float(user_input.principal) < 0:
                result = False
    if user_input.periods != None:
        try:
            int(user_input.periods)
        except Exception:
            result = False
        else:
            if int(user_input.periods) < 0:
                result = False
    if user_input.interest != None:
        try:
            float(user_input.interest)
        except Exception:
            result = False
        else:
            if float(user_input.interest) < 0:
                result = False
    if user_input.payment != None:
        try:
            float(user_input.payment)
        except Exception:
            result = False
        else:
            if float(user_input.payment) < 0:
                result = False
    return result

def is_conflicting_calculation_type_and_parameters(user_input):
    result = False
    if user_input.type == command_line_keywords[CommandLineKeyword.DIFFERANTIATE]:
        if user_input.payment != None:
            result = True
    if user_input.interest == None:
            result = True
    return result

def is_valid_calculation_type(calculation_type):
    result = True
    if calculation_type not in get_calculation_types():
        result = False
    if calculation_type == None:
        result = False
    return result

def is_valid_command_line_input(user_input):
    result = True
    if not command_line_guardian(user_input):
        result = False
    if not is_valid_calculation_type(user_input.type):
        result = False
    if is_conflicting_calculation_type_and_parameters(user_input):
        result = False
    return result

def is_direct_actual_payment_annuity_calculation(user_input):
    return user_input.periods != None and user_input.payment != None

def is_missing_payment_amount_for_actual_payment_annuity_calculation(user_input):
    return user_input.periods != None and user_input.payment == None

def is_missing_periods_for_actual_payment_annuity_calculation(user_input):
    return user_input.periods == None and user_input.payment != None

def needs_variable_conversion(user_input):
    result = False
    if user_input.periods == None:
        result = True
    return result

# handlers

def command_line_handler():
    user_input = get_command_line_input()
    if not is_valid_command_line_input(user_input):
        result = guardian_texts[GuardianText.INCORRECT_PARAMETERS]
    else:
        result = start_calculation(convert_user_input_for_calculation(user_input))
    return result

# starting point

if __name__ == "__main__":
    result = command_line_handler()
    print(result)