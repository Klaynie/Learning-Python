number_of_inputs = int(input())
output_list = []

for combined_user_input in range(number_of_inputs):
    combined_user_input = input()
    input_list = combined_user_input.split()
    if input_list[1] == "win":
        output_list.append(input_list[0])

print(output_list)
print(len(output_list))