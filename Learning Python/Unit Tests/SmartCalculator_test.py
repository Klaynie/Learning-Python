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