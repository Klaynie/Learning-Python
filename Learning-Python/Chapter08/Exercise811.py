def any_lowercase1(s):
    for c in s:
        if c.islower():
           return True
        else:
           return False
    '''
    This function will only check the first letter in s, since islower() will either return Ture or False
    on the first letter the return is executed
    '''
       
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
    '''
    This function will always return 'True' as a string since the condition 'c'.islower() will always be True
    as it is checking lowercase 'c' as a string and not the variable c
    '''
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
    '''
    This function will return the c.islower() condition of the last letter, since the flag is overwritten during every
    cycle of the for loop
    '''

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
    '''
    This function will return True if at least one character is lower case
    '''

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
    '''
    This function will return False once it has encountered the first upper case letter, there could be lower case
    letters after the upper case letters
    '''