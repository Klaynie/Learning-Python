number_of_lines = int(input())

for number in range(0, number_of_lines):
    number = int(input())
    if number % 7 == 0:
        print(number**2)