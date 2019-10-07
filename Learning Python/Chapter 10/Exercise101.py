def nested_sum(inputList):
    aggregatedSum = 0
    if inputList == []:
        return 'Please provide a list with content'
    outputList = unnest_list(inputList, [])
    for element in outputList:
        if type(element) == int:
         aggregatedSum += element
    return aggregatedSum

def unnest_list(inputList, outputList):
    '''
    This function will take a nested list and "un-nest" it so the individual parts can be easily summed up
    '''
    for element in inputList:
        if type(element) == list:
            '''
            If the component of the list itself is a list, then it must be broken down further, until it only contains integers
            This assumes that list only contains integers, which is a fair assumption given the requirement "Write a function called nested_sum that takes a nested list of integers"
            '''
            for part in element:
                if type(part) == int:
                    outputList.append(part)
                if type(part) == list:
                    unnest_list(part,outputList)
        if type(element) == int:
           outputList.append(element)
    return outputList

inputList = [1,[13,14],2,[3,4,[5,[15,16],6],[7,8,9,10,[11,12]]]] #should return 136, which it does
     
print(nested_sum(inputList))