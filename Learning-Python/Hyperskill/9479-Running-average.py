input_string = input()
output_list = []
for number in range(len(input_string) - 1):
    output_list.append((int(input_string[number]) + int(input_string[number + 1])) / 2)

print(output_list)