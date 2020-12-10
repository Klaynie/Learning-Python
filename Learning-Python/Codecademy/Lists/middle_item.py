def middle_element(lst):
    middle = len(lst) // 2
    if len(lst) % 2 != 0:
        result = lst[middle]
    else:
        result = (lst[middle - 1] + lst[middle]) / 2
    return result


#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, 4, 5]))