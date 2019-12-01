def sumall(*args):
    sum = 0
    for number in args:
        sum += number
    return sum
    
print(sumall(1,2,3,4,5,6,7,8,9,10,45))