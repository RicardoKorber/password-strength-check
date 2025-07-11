#Duplicate Check: Verify if there are duplicate characters in the password
def duplicate_check(password):
    for i in range(len(password) - 1):
        if password[i] == password[i]+1:
            return True
    return False