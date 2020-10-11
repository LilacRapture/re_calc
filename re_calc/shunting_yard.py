from re_calc.config import *
from re_calc.exceptions import CalcException
from re_calc.util import is_number

import re_calc.meta_containers as meta_containers


def peek(stack):
    return stack[-1]


def should_move_to_queue(stack, c_token_prc):
    if stack:
        s_token = peek(stack)
        s_token_prc = get_token_prop(s_token, 'prc')
        s_token_assoc = get_token_prop(s_token, 'assoc')
        return (s_token_prc > c_token_prc
                or (s_token_prc == c_token_prc and
                    s_token_assoc == 'left')
                and (s_token != '('))
    else:
        return False


# Use function meta data to get args count
def get_arity(fun):
    return fun.__code__.co_argcount


def arity_is_valid(fn_token, rest_tokens):
    paren_balance = 1
    properties = token_properties.get(fn_token)
    op_function = properties.get('fun')
    arity = get_arity(op_function)
    expected_separator_count = arity - 1
    arg_tokens = rest_tokens[1:]
    token_idx = 0
    separator_count = 0
    while token_idx < len(arg_tokens) and paren_balance != 0:
        c_token = arg_tokens[token_idx]
        if c_token == '(':
            paren_balance += 1
        elif c_token == ')':
            paren_balance -= 1
        elif (c_token in separators) and (paren_balance == 1):
            separator_count += 1
        token_idx += 1
    return expected_separator_count == separator_count


# Shunting yard algorithm
def infix_to_rpn(tokens):
    meta_tokens = meta_containers.set_meta_indices(tokens)
    output_queue = list()
    stack = list()
    for token in meta_tokens:
        if is_number(token):
            output_queue.append(token)  # add number to queue
        elif token in functions:
            n_token_idx = token.meta + 1
            if ((n_token_idx > len(meta_tokens) - 1)
                    or (meta_tokens[n_token_idx] != "(")):
                raise CalcException(
                    token.meta,
                    meta_tokens,
                    message="Missing function args",
                    loc_string="t:missing_fn_args")
            if not arity_is_valid(token, meta_tokens[token.meta + 1:]):
                raise CalcException(
                    token.meta,
                    meta_tokens,
                    message="Invalid arity",
                    loc_string="t:invalid_arity")
            stack.append(token)  # add function to stack
        elif token in separators:
            if not stack or '(' not in stack:
                raise CalcException(
                    token.meta,
                    meta_tokens,
                    message="Missing parentheses or separator",
                    loc_string="t:missing_separtor")
            while stack and peek(stack) != "(":
                output_queue.append(stack.pop())  # move operator to queue
        elif token in operators:
            if stack:  # if stack's not empty
                c_token_prc = get_token_prop(token, 'prc')
                while should_move_to_queue(stack, c_token_prc):
                    output_queue.append(stack.pop())  # move operator to queue
            stack.append(token)  # add operator to stack
        elif token == '(':
            stack.append(token)  # add open paren to stack
        elif token == ')':
            if not stack or '(' not in stack:
                raise CalcException(
                    token.meta,
                    meta_tokens,
                    message="Missing open paren(s)",
                    loc_string="t:missing_l_paren")
            while peek(stack) != '(':
                output_queue.append(stack.pop())  # move operator or function to queue
            if peek(stack) == '(':
                stack.pop()  # discard open paren
    while stack:  # move the rest of the stack to the queue
        if peek(stack) in priorities:
            raise CalcException(
                peek(stack).meta,
                meta_tokens,
                message="Missing close paren(s)",
                loc_string="t:missing_r_paren")
        output_queue.append(stack.pop())
    return meta_containers.pack_list(output_queue, tokens)
