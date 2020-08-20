number_of_inputs = int(input())
output_list = []

for _ in range(number_of_inputs):
    name, outcome = input().split()
    if outcome == "win":
        output_list.append(name)

print(output_list)
print(len(output_list))