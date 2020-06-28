import random
import string
import debugpy

def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    confusing_chars = ('O', '0', '1', 'l')
    password = ''
    while not len(password) == length:
        char = random.choice(chars)
        debugpy.breakpoint()
        if char in confusing_chars:
            password += char
            debugpy.breakpoint()
    return password

password_generator(6)