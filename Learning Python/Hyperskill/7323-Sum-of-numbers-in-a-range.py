"""
Your task here is to implement a simple algorithm that counts the sum of those numbers from a list that belong to a specified range.

Input: the first line contains a list of integer numbers separated by spaces. The second line contains two integer numbers aaa and bbb such that a≤ba \le ba≤b. The numbers are separated by a space as well. They represent the range.

Output: the sum of all elements xxx of the list such that a≤x ≤ba \le x \le ba≤x ≤b. If the list doesn't contain elements belonging to the specified range, output 000. See the example for more details.

Sample Input 1:
5 1 3 4 2
2 4

Sample Output 1:
9

Sample Input 2:
4 5 1 3 8
4 6

Sample Output 2:
9
"""

def range_sum(numbers, a, b):
    a, b = int(a), int(b)
    total = 0
    for num in numbers:
        num = int(num)
        if a <= num <= b:
            total += num
    return total

numbers = input().split()
a, b = input().split()
print(range_sum(numbers, a, b))