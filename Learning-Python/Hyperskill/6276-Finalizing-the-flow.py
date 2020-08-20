def greeting(name, surname):
    return f"Welcome to our party, {name} {surname}"

try:
    name, surname = input().split()
except ValueError:
    print("You need to enter exactly 2 words. Try again!")
else:
    print(greeting(name, surname))
finally:
    print('You will be more than welcome!')