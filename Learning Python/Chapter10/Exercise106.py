'''
Exercise 10.6. Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with the relational operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should re-
turn False.
'''

def is_sorted(t):
    i = 0
    while i < len(t)-1:
        if t[i]>t[i+1]:
            return False
        i += 1
    return True    

print(is_sorted([1,2,2]))

print(is_sorted(['b','a']))