from re_calc.expression_parser import tokenize
from re_calc.config import token_properties


# Use function meta data to get args count
def get_arity(fun):
    return fun.__code__.co_argcount


# Stack machine
def calculate(rpn_list):
    stack = list()
    for token in rpn_list:
        if type(token) is float:
            stack.append(token)
        else:
            properties = token_properties.get(token)
            if not properties:
                raise NameError("Not implemented: ", token)
            op_function = properties.get('fun')
            arity = get_arity(op_function)
            args = list()
            for k in range(arity):
                args.append(stack.pop())
            args.reverse()
            stack.append(op_function(*args))
    return stack.pop()
