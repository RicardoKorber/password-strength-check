#Numerical Digit Check
def digit_check(password):
    has_digit = False

    for char in password:
        if char.isdigit():
            has_digit = True
    return has_digit