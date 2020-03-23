def countLettersInString(stringIn,letterToCheck):
    count = 0
    for letter in stringIn:
        if letter == letterToCheck:
            count = count + 1
    print(count)
    
countLettersInString('banana','a')