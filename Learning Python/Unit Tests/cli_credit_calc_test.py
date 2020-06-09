from Hyperskill.cli_credit_calc import *
import unittest

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
        user_input = UserInput()
        user_input.type = 'annuity'
        user_input.principal = 1000000
        user_input.periods = 60
        user_input.interest = 10 / 100 / 12
        self.assertEqual(calculate_overpayment(user_input), 274880)
    def test_overpayment_2(self):
        user_input = UserInput()
        user_input.type = 'diff'
        user_input.principal = 500000
        user_input.periods = 8
        user_input.interest = 7.8 / 100 / 12
        self.assertEqual(calculate_overpayment(user_input), 14628)
    def test_overpayment_3(self):
        user_input = UserInput()
        user_input.type = 'annuity'
        user_input.payment = 8722
        user_input.periods = 120
        user_input.interest = 5.6 / 100 / 12
        self.assertEqual(calculate_overpayment(user_input), 246622)
    def test_overpayment_4(self):
        user_input = UserInput()
        user_input.type = 'annuity'
        user_input.principal = 500000
        user_input.payment = 23000
        user_input.interest = 7.8 / 100 / 12
        self.assertEqual(calculate_overpayment(user_input), 52000)
class CalculateDiffCases(unittest.TestCase):
    def test_diff_1(self):
        user_input = UserInput()
        user_input.principal = 1000000
        user_input.periods = 10
        user_input.interest = 10 / 100 / 12
        result = ("Month 1: paid out 108334\n"
                  "Month 2: paid out 107500\n"
                  "Month 3: paid out 106667\n"
                  "Month 4: paid out 105834\n"
                  "Month 5: paid out 105000\n"
                  "Month 6: paid out 104167\n"
                  "Month 7: paid out 103334\n"
                  "Month 8: paid out 102500\n"
                  "Month 9: paid out 101667\n"
                  "Month 10: paid out 100834\n")
        self.assertEqual(diff_calculation(user_input), result)
    def test_diff_2(self):
        user_input = UserInput()
        user_input.principal = 500000
        user_input.periods = 8
        user_input.interest = 7.8 / 100 / 12
        result = ("Month 1: paid out 65750\n"
                  "Month 2: paid out 65344\n"
                  "Month 3: paid out 64938\n"
                  "Month 4: paid out 64532\n"
                  "Month 5: paid out 64125\n"
                  "Month 6: paid out 63719\n"
                  "Month 7: paid out 63313\n"
                  "Month 8: paid out 62907\n")
        self.assertEqual(diff_calculation(user_input), result)
class NegativeInputValueCases(unittest.TestCase):
    def test_negative_input_1(self):
        user_input = UserInput()
        user_input.principal = -1
        self.assertFalse(can_convert(user_input))
    def test_negative_input_2(self):
        user_input = UserInput()
        user_input.periods = -1
        self.assertFalse(can_convert(user_input))
    def test_negative_input_3(self):
        user_input = UserInput()
        user_input.interest = -1
        self.assertFalse(can_convert(user_input))
    def test_negative_input_4(self):
        user_input = UserInput()
        user_input.payment = -1
        self.assertFalse(can_convert(user_input))
class PercentageSignInInterestCases(unittest.TestCase):
    def test_negative_input_1(self):
        user_input = UserInput()
        user_input.interest = '100%'
        self.assertFalse(can_convert(user_input))
class cliInputCases(unittest.TestCase):
    def test_cli_input_1(self):
        user_input = UserInput()
        user_input.principal = 1000000
        user_input.periods = 60
        user_input.interest = 10
        self.assertFalse(is_valid_command_line_input(user_input))
    def test_cli_input_2(self):
        user_input = UserInput()
        user_input.type = 'diff'
        user_input.principal = 1000000
        user_input.interest = 10
        user_input.payment = 100000
        self.assertFalse(is_valid_command_line_input(user_input))
    def test_cli_input_3(self):
        user_input = UserInput()
        user_input.type = 'annuity'
        user_input.principal = 100000
        user_input.payment = 10400
        user_input.periods = 8
        self.assertFalse(is_valid_command_line_input(user_input))
    def test_cli_input_4(self):
        user_input = UserInput()
        user_input.type = 'annuity'
        user_input.principal = 1000000
        user_input.payment = 104000
        self.assertFalse(is_valid_command_line_input(user_input))
    def test_cli_input_5(self):
        user_input = UserInput()
        user_input.type = 'diff'
        user_input.principal = 30000
        user_input.periods = -14
        user_input.interest = 10
        self.assertFalse(is_valid_command_line_input(user_input))
    def test_cli_input_6(self):
        user_input = UserInput()
        user_input.type = 'diff'
        user_input.principal = 30000
        user_input.periods = 10
        user_input.interest = 10
        self.assertTrue(is_valid_command_line_input(user_input))
    def test_cli_input_7(self):
        user_input = UserInput()
        user_input.type = 'diff'
        user_input.principal = 500000
        user_input.periods = 8
        user_input.interest = 7.8
        self.assertTrue(is_valid_command_line_input(user_input))
    def test_cli_input_8(self):
        user_input = UserInput()
        user_input.type = 'annuity'
        user_input.principal = 1000000
        user_input.periods = 60
        user_input.interest = 10
        self.assertTrue(is_valid_command_line_input(user_input))
    def test_cli_input_9(self):
        user_input = UserInput()
        user_input.type = 'annuity'
        user_input.principal = 1000000
        user_input.payment = 23000
        user_input.interest = 10
        self.assertTrue(is_valid_command_line_input(user_input))