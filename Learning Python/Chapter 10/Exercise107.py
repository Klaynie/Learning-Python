'''
Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
'''

def is_anagram(string1, string2):
    i = 0
    string1 = string1.lower()
    string2 = string2.lower()
    word1 = convertString2List(string1)
    word2 = convertString2List(string2)
    word1.sort()
    word2.sort()
    if len(string1) != len(string2):
        return False
    while i < len(word1):
        if word1[i] != word2[i]:
            return False
        i += 1
    return True

def convertString2List(string):
    letterList = []
    for letter in string:
        letterList.append(letter)
    return letterList

print(is_anagram('Atheismus','Mietshaus'))