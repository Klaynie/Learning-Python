def check_email(string):
    if (' ' not in string) and ('@' in string) and ('.' in string[string.find('@') + 2:]):
        return True
    return False