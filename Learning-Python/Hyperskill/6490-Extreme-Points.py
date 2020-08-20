test_dict = {"a": 43, "b": 1233, "c": 8}

for k, v in test_dict.items():
    if v == min(test_dict.values()):
        print(f'min: {k}')

for k, v in test_dict.items():
    if v == max(test_dict.values()):
        print(f'max: {k}')