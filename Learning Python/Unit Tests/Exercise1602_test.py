import sys  
sys.path.append('Chapter16')
from Exercise1602 import *
import unittest

class TimeTestCases(unittest.TestCase):
    def test_t1_hour_greater_t2_hour(self):
        t1 = Time()
        t1.hour = 12
        t1.minute = 30
        t1.second = 30
        
        t2 = Time()
        t2.hour = 11
        t2.minute = 30
        t2.second = 30
        self.assertTrue(is_after(t1, t2))

    def test_t1_minute_greater_t2_minute(self):
        t1 = Time()
        t1.hour = 11
        t1.minute = 31
        t1.second = 30

        t2 = Time()
        t2.hour = 11
        t2.minute = 30
        t2.second = 30
        self.assertTrue(is_after(t1, t2))

    def test_t1_second_greater_t2_second(self):
        t1 = Time()
        t1.hour = 11
        t1.minute = 30
        t1.second = 31

        t2 = Time()
        t2.hour = 11
        t2.minute = 30
        t2.second = 30
        self.assertTrue(is_after(t1, t2))

    def test_t1_equal_t2(self):
        t1 = Time()
        t1.hour = 11
        t1.minute = 30
        t1.second = 30

        t2 = Time()
        t2.hour = 11
        t2.minute = 30
        t2.second = 30
        self.assertFalse(is_after(t1, t2))

    def test_t1_hour_less_t2_hour(self):
        t1 = Time()
        t1.hour = 11
        t1.minute = 30
        t1.second = 30

        t2 = Time()
        t2.hour = 12
        t2.minute = 30
        t2.second = 30
        self.assertFalse(is_after(t1, t2))

    def test_t1_minute_less_t2_minute(self):
        t1 = Time()
        t1.hour = 11
        t1.minute = 30
        t1.second = 30

        t2 = Time()
        t2.hour = 11
        t2.minute = 31
        t2.second = 30
        self.assertFalse(is_after(t1, t2))

    def test_t1_second_less_t2_second(self):
        t1 = Time()
        t1.hour = 11
        t1.minute = 30
        t1.second = 30

        t2 = Time()
        t2.hour = 11
        t2.minute = 30
        t2.second = 31
        self.assertFalse(is_after(t1, t2))