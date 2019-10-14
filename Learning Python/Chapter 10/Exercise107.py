'''
Exercise 10.8. The (so-called) Birthday Paradox:
1. Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.
2. If there are 23 students in your class, what are the chances that two of you have the same
birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function
in the random module.
You can read about this problem at http://en.wikipedia.org/wiki/Birthday_paradox
and you can download my solution from http://thinkpython.com/code/birthday.py
'''

import random

def has_duplicates(t):
    i = 0
    j = 1
    while i < len(t):
        while j < len(t):
           if t[i] == t[j]:
               return True
           j += 1
        i += 1
        j = i + 1
    return False

def create_random_int_list(length):
    i = 0
    t = []
    while i < length:
        t.insert(i, random.randint(1, 365))
        i += 1
    return t

def calculate_probability(persons,amount):
    i = 1
    probabilityCounter = 0
    while i <= amount:
        t = create_random_int_list(persons)
        if has_duplicates(t):
            probabilityCounter += 1
        print(i, t, has_duplicates(t), probabilityCounter, probabilityCounter/i)
        i += 1

#print(has_duplicates(t))
calculate_probability(23,1000000)