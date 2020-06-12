hobbies_Adam = ('reading', ('jogging', 'boxing', 'yoga'), 'movies')

def unpack(input_tuple):
    result = []
    for item in input_tuple:
        if isinstance(item, tuple):
            for sub_item in item:
                result.append(sub_item)
        else:
            result.append(item)
    result = tuple(result)
    return result

print(unpack(hobbies_Adam))