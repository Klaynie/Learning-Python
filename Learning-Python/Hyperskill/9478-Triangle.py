height = int(input())
max_length = 1 + 2 * (height - 1)
for i in range(height):
    string_ = (1 + 2 * i) * '#'
    print(string_.center(max_length))