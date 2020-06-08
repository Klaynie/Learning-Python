import sys  
sys.path.append('Hyperskill')
from CreditCalculator import *
import unittest

class CalculatePaymentCases(unittest.TestCase):
    def test_calculate_payment_1(self):
        self.assertTrue(calculate_monthly_payments() == (112, 104))