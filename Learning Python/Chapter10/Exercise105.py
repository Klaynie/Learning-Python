'''
Exercise 10.5. Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None.
'''

def chop(inputList):
    del inputList[len(inputList)-1]
    del inputList[0]
    print(inputList)
    return None
    
list = [1,2,3,4]

print(chop(list))