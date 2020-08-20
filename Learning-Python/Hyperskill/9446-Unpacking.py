hobbies_Adam = ('reading', ('jogging', 'boxing', 'yoga'), 'movies')

def unpack(input_tuple):
    result = tuple()
    for item in input_tuple:
        result += (*item,) if isinstance(item, tuple) else (item,)
    return result

print(unpack(hobbies_Adam))