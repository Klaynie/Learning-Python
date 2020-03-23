import sys  
sys.path.append('Chapter16')
from Exercise1602 import *
import unittest

class TimeTestCas(unittest.TestCase):
    def test_t1_hour_greater_t2_hour(self):
    t1 = Time()
    t1.hour = 12
    t1.minute = 30
    t1.second = 30
    t2 = Time()
    t2.hour = 11
    t2.minute = 30
    t2.second = 30
    assertTrue(is_after(t1, t2))
"""
t1 = Time()
t1.hour = 11
t1.minute = 31
t1.second = 30

t2 = Time()
t2.hour = 11
t2.minute = 30
t2.second = 30

print(print_time(t1), print_time(t2), is_after(t1, t2))

t1 = Time()
t1.hour = 11
t1.minute = 30
t1.second = 31

t2 = Time()
t2.hour = 11
t2.minute = 30
t2.second = 30

print(print_time(t1), print_time(t2), is_after(t1, t2))

t1 = Time()
t1.hour = 11
t1.minute = 30
t1.second = 30

t2 = Time()
t2.hour = 11
t2.minute = 30
t2.second = 30

print(print_time(t1), print_time(t2), is_after(t1, t2))

t1 = Time()
t1.hour = 11
t1.minute = 30
t1.second = 30

t2 = Time()
t2.hour = 12
t2.minute = 30
t2.second = 30

print(print_time(t1), print_time(t2), is_after(t1, t2))

t1 = Time()
t1.hour = 11
t1.minute = 30
t1.second = 30

t2 = Time()
t2.hour = 11
t2.minute = 31
t2.second = 30

print(print_time(t1), print_time(t2), is_after(t1, t2))

t1 = Time()
t1.hour = 11
t1.minute = 30
t1.second = 30

t2 = Time()
t2.hour = 11
t2.minute = 30
t2.second = 31

print(print_time(t1), print_time(t2), is_after(t1, t2))
"""