"""
Imagine that your friend asked you to write a program that finds the minimum and the maximum.

Write the code that receives two integers as its input, each number goes on a new line. The output should show:

    The biggest number - in the first line
    The smallest number - in the second line.

Note that your friend might insert identical numbers! Just output both given numbers in this case.
"""

first, second = map(int, [input(), input()])
print(f"{first}\n{second}" if first > second else f"{second}\n{first}")