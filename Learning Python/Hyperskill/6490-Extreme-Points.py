test_dict = {"a": 43, "b": 1233, "c": 8}

min_value = 100000
max_value = 0
min_name = ''
max_name = ''

for key, value in test_dict.items():
    if value > max_value:
        max_value = value
        max_name = key
    elif value < min_value:
        min_value = value
        min_name = key

print(f'min: {min_name}')
print(f'max: {max_name}')