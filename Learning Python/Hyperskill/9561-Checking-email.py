def check_email(string):
    if (' ' not in string) and ('@' in string) and ('.' in string[string.find('@'):]):
        return True
    return False