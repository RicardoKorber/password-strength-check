#Symbols Check: Verify if the password contains any symbols.
def symbol_check(password):
    for char in password:
        if not char.isalnum():
            return True
    return False