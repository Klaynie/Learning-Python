import sys  
sys.path.append('Hyperskill')
from CreditCalculator import *
import unittest

class CalculatePaymentCases(unittest.TestCase):
    def test_calculate_payment_1(self):
        self.assertEqual(calculate_monthly_payment(), (112, -8))

    def test_calculate_payment_2(self):
        principal = 1000
        months = 10
        self.assertEqual(calculate_monthly_payment(principal, months), (100, 0))

class CalculateMonthCases(unittest.TestCase):
    def test_calculate_month_1(self):
        self.assertEqual(calculate_count_of_month(), 1)

    def test_calculate_month_2(self):
        principal = 1000
        payment = 150
        self.assertEqual(calculate_count_of_month(principal, payment), 7)

class PrintPaymentCases(unittest.TestCase):
    def test_print_payment_1(self):
        self.assertEqual(get_monthly_payment_message(), 'Your monthly payment = 100')

    def test_print_payment_2(self):
        self.assertEqual(get_monthly_payment_message(112, -8), 'Your monthly payment = 112 with last month payment = 104')

class PrintMonthCases(unittest.TestCase):
    def test_print_months_1(self):
        self.assertEqual(get_count_of_month_message(), 'It takes 1 month to repay the credit')

    def test_print_months_2(self):
        self.assertEqual(get_count_of_month_message(2), 'It takes 2 months to repay the credit')