import sys  
sys.path.append('Hyperskill')
from SmartCalculator import *
import unittest

class IsVariableTestCases(unittest.TestCase):
    def test_is_variable_1(self):
        string = 'a'
        self.assertTrue(is_variable(string))