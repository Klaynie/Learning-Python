from Hyperskill.credit_calc import *
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

    def test_calculate_paydown_time_1(self):
        principal = 500000
        monthly_payment = 23000
        interest = 7.8 / 100 / 12
        self.assertEqual(calculate_paydown_time(principal, monthly_payment, interest), 24)

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

    def test_calculate_credit_pricipal_2(self):
        monthly_payment = 8722
        months = 120
        interest = 5.6 / 100 / 12
        self.assertEqual(calculate_principal(monthly_payment, months, interest), 800018)

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

class CalculateOverpaymentCases(unittest.TestCase):

    def test_overpayment_1(self):
        principal = 1000000
        periods = 60
        interest = 10 / 100 / 12
        self.assertEqual(calculate_overpayment(), 274880)

    def test_overpayment_2(self):
        principal = 500000
        periods = 8
        interest = 7.8 / 100 / 12
        self.assertEqual(calculate_overpayment(), 14628)

    def test_overpayment_3(self):
        payment = 8722
        periods = 120
        interest = 5.6 / 100 / 12
        self.assertEqual(calculate_overpayment(), 246622)

    def test_overpayment_4(self):
        payment = 500000
        periods = 23000
        interest = 7.8 / 100 / 12
        self.assertEqual(calculate_overpayment(), 52000)