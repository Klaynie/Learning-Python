import itertools

def avoid(word,string):
    for letter in string:
        #print(word, string, letter)
        if word.find(letter) != -1:
            return False
    return True

def get_input():
    prompt = "This program will check if it can find a word that do not contain certain letters. Please type up to 5 letters!\n"
    string = input(prompt).lower()
    if len(string) > 5:
        print("Please only provide 5 letters.")
        get_input()
    if check_input(string) != True:
        print(check_input(string))
        get_input()
    return string

def check_input(string):
    for letter in string:
        if letter.isnumeric() == True:
            return "Please only provide letters."
    return True

def check_list():
    string = get_input()
    totalCounter = 0
    hasNoLetterFromStringCounter = 0
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        if avoid(word,string) == True:
            #print(word)
            hasNoLetterFromStringCounter = hasNoLetterFromStringCounter + 1
        totalCounter = totalCounter + 1
        #print(hasNoLetterFromStringCounter, totalCounter)
    print('Out of ' + str(totalCounter) + ' words there are ' + str(hasNoLetterFromStringCounter) + ' words without your string which is ' + str(round(hasNoLetterFromStringCounter/totalCounter*100,2)) +'%')

#Out of 113809 words there are 37641 words without an e which is 33.07% - Verified

#check_list()

def combination_of_letters():
    list = itertools.combinations('abcdefghijklmnopqrstuvwxyz', 5)
    maximumHasNoLetterFromStringCounter = 0
    for items in list:
        string = items[0] + items[1] + items[2] + items[3] + items[4]
        if check_list2(string) > maximumHasNoLetterFromStringCounter:
            maximumHasNoLetterFromStringCounter = check_list2(string)
            maximumString = string
        print(maximumHasNoLetterFromStringCounter, maximumString, string)
    
'''
To Do:
Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
'''

def check_list2(string):
    totalCounter = 0
    hasNoLetterFromStringCounter = 0
    wordList = open('words.txt')
    for line in wordList:
        word = line.strip()
        if avoid(word,string) == True:
            hasNoLetterFromStringCounter = hasNoLetterFromStringCounter + 1
        totalCounter = totalCounter + 1
    return hasNoLetterFromStringCounter
    
combination_of_letters()