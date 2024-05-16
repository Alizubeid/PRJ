from hashlib import sha256
from re import fullmatch

class PasswordType(Exception):
    pass

def hashing(TEXT : str):
    if fullmatch(r"[A-Za-z0-9_!@#$%^&*()-/<>`~=+{}]{8,}",TEXT):
        return sha256(TEXT.encode()).hexdigest()
    try:
        raise PasswordType("the password must contain 1 uppercase 1 lowercase, 1 number and 1 special character")
    except PasswordType as e:
        print(e)