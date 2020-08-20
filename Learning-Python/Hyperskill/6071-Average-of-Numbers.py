interval_start = int(input())
interval_end = int(input())

divisible_by_three_aggregator = 0
divisible_by_three_counter = 0

for number in range(interval_start, interval_end + 1):
    if number % 3 == 0:
        divisible_by_three_aggregator += number
        divisible_by_three_counter += 1
print(divisible_by_three_aggregator / divisible_by_three_counter)