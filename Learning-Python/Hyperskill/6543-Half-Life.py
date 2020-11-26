starting_amount = int(input())
resulting_amount = int(input())

half_life = 12

cycle_counter = 0

while starting_amount > resulting_amount:
    starting_amount /= 2
    cycle_counter += 1

print(half_life * cycle_counter)