from calculator.config import *
from calculator.util import is_number


def peek(stack):
    return stack[-1]


# Shunting yard algorithm
def infix_to_prn(tokens):
    output_queue = list()
    stack = list()
    for token in tokens:
        if is_number(token):
            output_queue.append(token)  # add number to queue
        elif token in functions:
            stack.append(token)  # add function to stack
        elif token in separators:
            if stack == [] or '(' not in stack:
                raise SyntaxError("Missing parentheses or separator")
            while (stack != []) and peek(stack) != "(":
                output_queue.append(stack.pop())  # move operator to queue
        elif token in operators:
            if stack: # if stack's not empty
                t_precedence = get_token_prop(token, 'prc')
                while (stack != []) and \
                        (get_token_prop(peek(stack), 'prc') > t_precedence
                         or (get_token_prop(peek(stack), 'prc') == t_precedence and
                             get_token_prop(peek(stack), 'assoc') == 'left')
                         and (peek(stack) != '(')):
                    output_queue.append(stack.pop())  # move operator to queue
            stack.append(token)  # add operator to stack
        elif token == '(':
            stack.append(token)  # add open paren to stac0k
        elif token == ')':
            if stack == [] or '(' not in stack:
                raise SyntaxError("Mismatched parentheses")
            while peek(stack) != '(':
                output_queue.append(stack.pop())  # move operator or function to queue
            if peek(stack) == '(':
                stack.pop()  # discard open paren
    while stack:  # move the rest of the stack to the queue
        if peek(stack) in priorities:
            raise SyntaxError("Mismatched parentheses")
        output_queue.append(stack.pop())
    return output_queue
