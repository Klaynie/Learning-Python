"""
Round the number from input to the required number of decimals.

The input format:

Two lines: the first with a floating-point number, the second with an integer representing the decimal count.

The output format:

The rounded number.

Do NOT forget to convert the input numbers and to enclose each value in {} in a formatted string.

Sample Input 1:
2.71828
3

Sample Output 1:
2.718
"""

input_number = float(input())
rounding = int(input())

print(f'{input_number:.{rounding}f}')