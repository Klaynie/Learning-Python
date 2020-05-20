height = int(input())
max_length = 1 + 2 * height
for i in range(height):
    string_ = (1 + 2 * i)*'#'
    print(string_.center(max_length))