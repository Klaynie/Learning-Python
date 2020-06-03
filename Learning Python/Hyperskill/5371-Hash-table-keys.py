def hash_function(number):
    return ((number * 7) + 42) % 71

print(hash_function(78))
print(hash_function(41))
print(hash_function(33))