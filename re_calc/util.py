# checks whether a token is a number
def is_number(number):
    try:
        float(number)
        return True
    except ValueError as e:
        return False


def every(predicate_fn, collection):
    res_list = [predicate_fn(x) for x in collection]
    return all(res_list)
