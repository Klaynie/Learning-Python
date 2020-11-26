def index_all(search_list, search_value):
    result = list()
    for i in range(len(search_list)):
        if search_list[i] == search_value:
            result.append([i])
        elif isinstance(search_list[i], list):
            for j in index_all(search_list[i], search_value):
                result.append([i] + j)
    return result


my_list = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(index_all(my_list, 2))