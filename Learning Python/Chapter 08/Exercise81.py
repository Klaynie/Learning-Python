def printLettersPerLine(stringIn):
    reversedString = reverseString(stringIn)
    index = 0
    while index < len(stringIn):
        print(reversedString[index])
        index = index + 1
    
def reverseString(stringIn):
    index = 1
    stringOut = ''    
    while index <= len(stringIn):
        stringOut = stringOut + stringIn[-index]
        index = index + 1
    return stringOut

printLettersPerLine('Ducklings')