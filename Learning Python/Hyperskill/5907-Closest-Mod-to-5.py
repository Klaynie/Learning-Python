def closest_mod_5(x):
    while x % 5 != 0:
        x += 1
    return x

print(closest_mod_5(44))