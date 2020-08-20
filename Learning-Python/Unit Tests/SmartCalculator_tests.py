import sys  
sys.path.append('Hyperskill')
from SmartCalculator import *
import unittest

class IsVariableTestCases(unittest.TestCase):
    def test_is_variable_1(self):
        string = 'a'
        self.assertTrue(is_variable(string))
    
    def test_is_variable_2(self):
        string = 'BIG'
        self.assertTrue(is_variable(string))

    def test_is_variable_3(self):
        string = 'small'
        self.assertTrue(is_variable(string))

    def test_is_variable_4(self):
        string = 'Rick'
        self.assertTrue(is_variable(string))

    def test_is_variable_5(self):
        string = 'ö'
        self.assertFalse(is_variable(string))

    def test_is_variable_6(self):
        string = 'a2a'
        self.assertFalse(is_variable(string))

    def test_is_variable_7(self):
        string = 'an2'
        self.assertFalse(is_variable(string))

    def test_is_variable_8(self):
        string = 'aö2'
        self.assertFalse(is_variable(string))

class IsValiadMathTestCases(unittest.TestCase):
    def test_is_valid_math_1(self):
        string = '3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)'
        self.assertTrue(check_for_valid_math(string))
    
    def test_is_valid_math_2(self):
        string = '3 + 2 * 4'
        self.assertTrue(check_for_valid_math(string))

    def test_is_valid_math_3(self):
        string = '2 * (3 + 4) + 1'
        self.assertTrue(check_for_valid_math(string))

    def test_is_valid_math_4(self):
        string = '2^2'
        self.assertTrue(check_for_valid_math(string))

    def test_is_valid_math_5(self):
        string = '2*2^3'
        self.assertTrue(check_for_valid_math(string))

    def test_is_valid_math_6(self):
        string = '8 * 3 + 12 * (4 - 2)'
        self.assertTrue(check_for_valid_math(string))

    def test_is_valid_math_7(self):
        string = '2 - 2 + 3'
        self.assertTrue(check_for_valid_math(string))

    def test_is_valid_math_8(self):
        string = 'a*2+b*3+c*(2+3)'
        self.assertTrue(check_for_valid_math(string))

    def test_is_valid_math_9(self):
        string = '1 +++ 2 * 3 -- 4'
        self.assertTrue(check_for_valid_math(string))

    def test_is_valid_math_10(self):
        string = '4 * (2 + 3'
        self.assertFalse(check_for_valid_math(string))

    def test_is_valid_math_11(self):
        string = '3 *** 5'
        self.assertFalse(check_for_valid_math(string))

    def test_is_valid_math_12(self):
        string = '4+3)'
        self.assertFalse(check_for_valid_math(string))

class CheckMatchingBracketsTestCases(unittest.TestCase):
    def test_matching_brackets_1(self):
        string = '3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)'
        self.assertTrue(check_for_matching_brackets(string))

    def test_matching_brackets_2(self):
        string = 'a*2+b*3+c*(2+3)'
        self.assertTrue(check_for_matching_brackets(string))

    def test_matching_brackets_3(self):
        string = '2 * (3 + 4) + 1'
        self.assertTrue(check_for_matching_brackets(string))

    def test_matching_brackets_4(self):
        string = '8 * 3 + 12 * (4 - 2)'
        self.assertTrue(check_for_matching_brackets(string))

    def test_matching_brackets_5(self):
        string = '4 * (2 + 3'
        self.assertFalse(check_for_matching_brackets(string))

    def test_matching_brackets_6(self):
        string = '4+3)'
        self.assertFalse(check_for_matching_brackets(string))

class CheckVariablesDeclaredTestCases(unittest.TestCase):
    def test_variables_declared_1(self):
        variables_dict = {'a': 4, 'b': 5}
        string = 'a*2+b*3+c*(2+3)'
        self.assertFalse(check_all_variables_declared(string))

class CheckIsSingleNumberTestCases(unittest.TestCase):
    def test_is_single_number_1(self):
        string = '1'
        self.assertTrue(is_single_number(string))

    def test_is_single_number_2(self):
        string = '-1'
        self.assertTrue(is_single_number(string))

    def test_is_single_number_3(self):
        string = '10'
        self.assertTrue(is_single_number(string))

    def test_is_single_number_4(self):
        string = '-10'
        self.assertTrue(is_single_number(string))

    def test_is_single_number_5(self):
        string = '100'
        self.assertTrue(is_single_number(string))

    def test_is_single_number_6(self):
        string = '-100'
        self.assertTrue(is_single_number(string))

    def test_is_single_number_7(self):
        string = 'a'
        self.assertFalse(is_single_number(string))

    def test_is_single_number_8(self):
        string = '-a'
        self.assertFalse(is_single_number(string))

class CheckPostfixCalculation(unittest.TestCase):
        def test_postfix_calculation_1(self):
            string = '2 + 2'
            self.assertTrue(postfix_calculation(convert_input(string)) == 4)

        def test_postfix_calculation_2(self):
            string = '2+2'
            self.assertTrue(postfix_calculation(convert_input(string)) == 4)

        def test_postfix_calculation_3(self):
            string = '2^2'
            self.assertTrue(postfix_calculation(convert_input(string)) == 4)

        def test_postfix_calculation_4(self):
            string = '2*2^3'
            self.assertTrue(postfix_calculation(convert_input(string)) == 16)

        def test_postfix_calculation_5(self):
            string = '8 * 3 + 12 * (4 - 2)'
            self.assertTrue(postfix_calculation(convert_input(string)) == 48)

        def test_postfix_calculation_7(self):
            string = '1 +++ 2 * 3 -- 4'
            self.assertTrue(postfix_calculation(convert_input(string)) == 11)

        def test_postfix_calculation_8(self):
            string = '2 - 2 + 3'
            self.assertTrue(postfix_calculation(convert_input(string)) == 3)

        def test_postfix_calculation_9(self):
            string = '3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)'
            self.assertTrue(postfix_calculation(convert_input(string)) == 121)

        def test_postfix_calculation_10(self):
            string = '-2+3'
            self.assertTrue(postfix_calculation(convert_input(string)) == 1)

        def test_postfix_calculation_11(self):
            string = '-(2+3)'
            self.assertTrue(postfix_calculation(convert_input(string)) == -5)

        def test_postfix_calculation_12(self):
            string = '+2+3'
            self.assertTrue(postfix_calculation(convert_input(string)) == 5)

        def test_postfix_calculation_13(self):
            string = '(2+3)'
            self.assertTrue(postfix_calculation(convert_input(string)) == 5)

        def test_postfix_calculation_14(self):
            string = '(2+3)-(2+3)'
            self.assertTrue(postfix_calculation(convert_input(string)) == 0)
