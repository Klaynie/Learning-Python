# Write your function here
def reversed_list(lst1, lst2):
    result = True
    j = len(lst2) - 1
    for i in range(len(lst1)):
        if lst1[i] != lst2[j]:
            result = False
            break
        j -= 1
    return result

# Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
#print(reversed_list([1, 5, 3], [3, 2, 1]))
