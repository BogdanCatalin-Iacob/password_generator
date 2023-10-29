'''
Generate password containing Uppercase letters,
Lowercase letters and symbols
'''
import string
import secrets


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


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    '''
    Generate password with the required arguments
    '''
    # create a combination of letters and numbers (0-9)
    combination: str = string.ascii_lowercase + string.digits

    # check if symbols are required and add them to combination
    if symbols:
        combination += string.punctuation

    # check if uppercase is required and add them to combination
    if uppercase:
        combination += string.ascii_uppercase

    # generate a password combination of the required length
    new_password = ''
    for _ in range(length):
        new_password += combination[secrets.randbelow(len(combination))]

    return new_password


if __name__ == '__main__':
    new_pass: str = generate_password(length=20, symbols=True, uppercase=True)

    print(new_pass)
