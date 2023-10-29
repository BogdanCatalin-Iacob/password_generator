'''
Generate password containing Uppercase letters,
Lowercase letters and symbols
'''
import string


def contains_upper(password: str) -> bool:
    '''
    Check if the password conatins Uppercase letters
    '''
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbols(password: str) -> bool:
    '''
    Check if the password contains symbols
    '''
    for char in password:
        if char in string.punctuation:
            return True
    return False
