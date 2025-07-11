#Higher and Lowercase
def cases_check(password):
    has_uppercase = False
    has_lowercase = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        
        if has_uppercase and has_lowercase:
            return True
    return False