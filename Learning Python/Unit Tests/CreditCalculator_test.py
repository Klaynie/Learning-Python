import sys  
sys.path.append('Hyperskill')
from CreditCalculator import *
import unittest

class GetNumberCases(unittest.TestCase):
    def test_get_number_1(self):
        self.assertEqual(get_number('n'), 0)
    def test_get_number_2(self):
        self.assertEqual(get_number('a'), 1)
    def test_get_number_3(self):
        self.assertEqual(get_number('p'), 2)

class CalculatePaydownTimeCases(unittest.TestCase):
    def test_calculate_paydown_time_1(self):
        principal = 1000000
        monthly_payment = 15000
        interest = 10 / 100 / 12
        self.assertEqual(calculate_paydown_time(principal, monthly_payment, interest), 98)

class CalculateAnnuityPaymentCases(unittest.TestCase):
    def test_calculate_annuity_payment_1(self):
        principal = 1000000
        months = 60
        interest = 10 / 100 / 12
        self.assertEqual(calculate_monthly_payment(principal, months, interest), 21248)

class CalculateCreditPrincipalCases(unittest.TestCase):
    def test_calculate_credit_pricipal_1(self):
        monthly_payment = 8721.8
        months = 120
        interest = 5.6 / 100 / 12
        self.assertEqual(calculate_principal(monthly_payment, months, interest), 800000)

class ConvertPaydowmTimeCases(unittest.TestCase):
    def test_convert_paydown_time(self):
        paydown_time = 98
        self.assertEqual(convert_paydown_time_to_years_and_months(paydown_time), (8, 2))

class GeneratePaydownTimesCases(unittest.TestCase):
    def test_generate_paydown_time_1(self):
        years = 8
        months = 2
        self.assertEqual(generate_paydown_time_text(years, months), '8 years and 2 months')
    
    def test_generate_paydown_time_2(self):
        years = 0
        months = 11
        self.assertEqual(generate_paydown_time_text(years, months), '11 months')
    
    def test_generate_paydown_time_3(self):
        years = 1
        months = 0
        self.assertEqual(generate_paydown_time_text(years, months), '1 year')
    
    def test_generate_paydown_time_4(self):
        years = 0
        months = 1
        self.assertEqual(generate_paydown_time_text(years, months), '1 month')
    
    def test_generate_paydown_time_5(self):
        years = 2
        months = 0
        self.assertEqual(generate_paydown_time_text(years, months), '2 years')
    
    def test_generate_paydown_time_6(self):
        years = 1
        months = 11
        self.assertEqual(generate_paydown_time_text(years, months), '1 year and 11 months')

class PrintPaydownTimeCases(unittest.TestCase):
    def test_paydown_time_1(self):
        number = 0
        variable = '8 years and 2 months'
        self.assertEqual(generate_message(number, variable), 'You need 8 years and 2 months to repay this credit!')

class PrintAnnuityPaymentCases(unittest.TestCase):
    def test_annuity_payment_1(self):
        number = 1
        variable = 21248
        self.assertEqual(generate_message(number, variable), 'Your annuity payment = 21248!')

class PrintCreditPrincipalCases(unittest.TestCase):
    def test_credit_principal_1(self):
        number = 2
        variable = 800000
        self.assertEqual(generate_message(number, variable), 'Your credit principal = 800000!')