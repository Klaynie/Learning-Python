def unnest_list(inputList, outputList):
    '''
    This function will take a nested list and "un-nest" it so the individual parts can be used
    '''
    for element in inputList:
        if type(element) == list:
            for part in element:
                if type(part) != list:
                    outputList.append(part)
                if type(part) == list:
                    unnest_list(part,outputList)
        else:
           outputList.append(element)
    return outputList

def remove_duplicates(inputList):
    inputList = unnest_list(inputList, [])
    newList = []
    for item in inputList:
        if (item in newList) == False:
            newList.append(item)
    return newList

inputList = ['duck','duck','goose']

print(remove_duplicates(inputList))