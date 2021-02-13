# Source: https://florian.github.io//xor-trick/
# Swap two values x and y in-place, i.e. without using any helper variables.
x = 1
y = 2

print(f"Old values: x:{x} y:{y}")

x ^= y
y ^= x
x ^= y

print(f"New values: x:{x} y:{y}")

# You are given an array of n - 1 integers which are in the range between 1 and n. All numbers appear exactly once, except one number, which is missing. Find this missing number.


def find_missing(list_in, n):
    result = 0
    for value in range(1, n + 1):
        result ^= value
    for value in list_in:
        result ^= value
    return result


list_in = [1, 2, 3, 4, 6, 7, 8, 9, 10]
n = max(list_in)

print(find_missing(list_in, n))
