from calculator.expression_parser import tokenize
from calculator.config import token_properties
from calculator.util import is_number


def get_arity(fun):
    return fun.__code__.co_argcount

# Stack machine
def calculate(rpn_list):
    stack = list()
    for token in rpn_list:
        if is_number(token):
            stack.append(token)
        else:
            properties = token_properties.get(token)
            if properties == None:
                raise NameError("Not implemented: ", token)
            op_function = properties.get('fun')
            arity = get_arity(op_function)
            args = list()
            for k in range(arity):
                args.append(stack.pop())
            args.reverse()
            stack.append(op_function(*args))
    return stack.pop()
