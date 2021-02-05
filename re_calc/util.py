from typing import Callable
from collections.abc import Collection

def is_number(number: str) -> bool:
    ''' Checks whether a string is valid to be parsed as number.
    '''
    try:
        float(number)
        return True
    except ValueError as e:
        return False


def every(pred: Callable, coll: Collection):
    ''' Checks if all the members of the collection match the predicate.
    '''
    res_list = [pred(x) for x in coll]
    return all(res_list)
