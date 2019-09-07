"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    """
    This function will check if a word is palindrome, a palindrome is word that is the same forwards as backwards like "noon" and "redivider"
    If we take "redivider" We will go through the word from outside to inside in the fashion of 
    "redivider" check r=r -> "edivide" check e=e, "divid" check d=d, "ivi" check i=i, if one of these does not match we return False
    The letter in the middle does not matter for odd letter words. This is handled below by checking if we have an even or odd numbered word
    """
    word = word.lower()
    """
    We convert to lower cases, since we want to check if the first letter and last letter are equal
    """
    if len(word)<3:
       error_message_text = 'Word length must be greater than 2'
       return error_message_text
    """
    We do not care about 2 letter words
    """
    if len(word)%2==0:
        """
        We have to split up the function into two parts, for words with an even amount of letters there will be no single letter middle part
        We therefore need to check each letter pair
        Creating the pairs is handled by the for loop, the loop requires a letter size of more than 4. A second if catches 4 letter words 
        """
        if first(word)==last(word):
            """
            If the first and last letter are equal we enter into the loop, otherwise we return false
            """
            if first(middle(word)) == last(middle(word)):
               old_middle = middle(word)
               for i in range (int((len(word))/2)-2):
                   new_middle = middle(old_middle)
                   if first(new_middle) == last(new_middle):
                      old_middle = new_middle
                   else:
                       return False
            """
            The part below is needed to catch 4 letter words, the for loop is out of range for these
            """
            if first(middle(word)) != last(middle(word)):
                return False
            return True
        else:
            return False
    if len(word)%2!=0:
        """
        For odd letter words, the for loop can handle 3 letter words, since only the first letter and last letter have to be equal
        The for loop will not be run for 3 letter words
        """
        if first(word)==last(word):
            if first(middle(word)) == last(middle(word)):
               old_middle = middle(word)
               for i in range (int((len(word)-1)/2)-1):
                   new_middle = middle(old_middle)
                   if first(new_middle) == last(new_middle):
                      old_middle = new_middle
                   else:
                       return False
            if first(middle(word)) != last(middle(word)):
                return False       
            return True
        else:
            return False

def is_palindrome2(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome('Saippuakivikauppias')) #Odd
print(is_palindrome('Lagerregal')) #Even

print(is_palindrome('SaippuakivikauppiBs')) #Odd
print(is_palindrome('LagerregBl')) #Even

print(is_palindrome2('saippuakivikauppias')) #Odd
print(is_palindrome2('lagerregal')) #Even

print(is_palindrome2('saippuakivikauppibs')) #Odd
print(is_palindrome2('lagerregbl')) #Even