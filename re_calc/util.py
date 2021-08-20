
def is_number(number):
    ''' Checks whether a string is valid to be parsed as number.
    '''
    try:
        float(number)
        return True
    except ValueError as e:
        return False


def every(pred, coll):
    ''' Checks if all the members of the collection match the predicate.
    '''
    res_list = [pred(x) for x in coll]
    return all(res_list)
