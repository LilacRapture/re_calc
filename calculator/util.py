# checks whether a token is a number
def is_number(number):
    try:
        float(number)
        return True
    except ValueError as e:
        return False
