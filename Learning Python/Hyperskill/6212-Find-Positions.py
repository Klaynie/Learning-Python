# put your python code here
list_of_numbers = input().split()
number_to_look_for = input()

count_of_number_found = 0
list_of_found_index = []
for index, value in enumerate(list_of_numbers):
    if value == number_to_look_for:
        list_of_found_index.append(str(index))
        count_of_number_found += 1

if count_of_number_found == 0:
    print("not found")
else:
    print(" ".join(list_of_found_index))