interval_start = int(input())
interval_end = int(input())

divisiable_by_three_aggregator = 0
divisiable_by_three_counter = 0

for number in range(interval_start, interval_end + 1):
    if number % 3 == 0:
        divisiable_by_three_aggregator += number
        divisiable_by_three_counter += 1
print(divisiable_by_three_aggregator / divisiable_by_three_counter)