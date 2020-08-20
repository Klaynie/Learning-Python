number_of_values = int(input())
sum_of_numbers = 0
for number in range(0, number_of_values):
    sum_of_numbers += int(input())
print(float(sum_of_numbers/number_of_values))