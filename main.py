'''
Generate password containing Uppercase letters,
Lowercase letters and symbols
'''


def contains_upper(password: str) -> bool:
    '''
    Check if the password conatins Uppercase letters
    '''
    for char in password:
        if char.isupper():
            return True
    return False
