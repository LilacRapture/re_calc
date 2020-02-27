from calculator.expression_parser import tokenize
from calculator.config import token_properties
from calculator.util import is_number


def get_arity(fun):
    return fun.__code__.co_argcount

# Stack machine
def calculate(rpn_list):
    stack = list()
    args = list()
    for token in rpn_list:
        if is_number(token):
            stack.append(token)
        else:
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            properties = token_properties.get(token)
            if properties == None:
                raise NameError("Not implemented: ", token)
            op_function = properties.get('fun')
            stack.append(op_function(operand_1, operand_2))
    return stack.pop()
