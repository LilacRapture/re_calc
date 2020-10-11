from re_calc.config import token_properties
from re_calc.exceptions import MathException, CalcException
from re_calc.util import every


# Use function meta data to get args count
def get_arity(fun):
    return fun.__code__.co_argcount


def is_float(x):
    return isinstance(x, float)


def safe_get_meta(o):
    return getattr(o, 'meta', [])


# Stack machine
def calculate(rpn_list):
    stack = list()
    for token in rpn_list:
        if is_float(token):
            stack.append(token)
        else:
            properties = token_properties.get(token)
            op_function = properties.get('fun')
            arity = get_arity(op_function)
            args = list()
            if len(stack) < arity:
                raise CalcException(
                    token.meta,
                    safe_get_meta(rpn_list),
                    message="Invalid expression",
                    loc_string="t:invalid_expr")
            for k in range(arity):
                args.append(stack.pop())
            if not every(is_float, args):
                raise CalcException(
                    token.meta,
                    safe_get_meta(rpn_list),
                    message="Invalid expression",
                    loc_string="t:invalid_expr")
            args.reverse()
            try:
                stack.append(op_function(*args))
            except ZeroDivisionError:
                raise MathException(
                    message="Division by zero",
                    loc_string="t:division_by_0")
            except ValueError:
                if token == 'log':
                    raise MathException(
                        message="Out of log function domain",
                        loc_string="t:log_fn_domain_error")
    if len(stack) > 1:
        error_token = stack[-2]
        raise CalcException(
            error_token.meta,
             safe_get_meta(rpn_list),
             message="Invalid expression",
             loc_string="t:invalid_expr")
    return stack.pop()
