input_string = input()
output_list = []
for number in range(len(input_string)-1):
    moving_average = (int(input_string[number]) + int(input_string[number+1])) / 2
    output_list.append(moving_average)

print(output_list)