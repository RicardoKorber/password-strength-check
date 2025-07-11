#Duplicate Check with regex: Verify if there are duplicate characters in the password with the regualar exprections library.
from re import search

def duplicate_check_re(password):
    return bool(search(r"(.)\1+", password))