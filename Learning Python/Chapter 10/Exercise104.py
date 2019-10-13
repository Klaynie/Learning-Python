'''
Exercise 10.4. Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. So middle([1,2,3,4]) should return [2,3].
'''

def middle(inputList):
    del inputList[len(inputList)-1]
    del inputList[0]
    return inputList
    
list = [1,2,3,4]

print(middle(list))