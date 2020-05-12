number_of_lines = int(input())
user_input = []

for line in range(0, number_of_lines):
    user_input.append(int(input()))
for number in user_input:
    if number % 7 == 0:
        print(number**2)