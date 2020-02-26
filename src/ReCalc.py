from src.expression_parser import tokenize
from src.config import *
import unittest
# TODO: add coverage calculation

# get token property by literal and property name
def get_token_prop(literal, prop_name):
    return token_properties.get(literal).get(prop_name)

# checks whether a token is a number
def is_number(number):
    try:
        float(number)
        return True
    except Exception as e:
        return False

def peek(stack):
    return stack[-1]

# Sorting station algorithm
def sorting_station(tokens):
    output_queue = list()
    stack = list()
    for token in tokens:
        if is_number(token):
            output_queue.append(token) # add number to queue
        elif token in functions:
            stack.append(token) # add function to stack
        elif token in separators:
            if stack == [] or '(' not in stack:
                raise SyntaxError("Missing parentheses or separator")
            while (stack != []) and peek(stack) != "(":
                output_queue.append(stack.pop()) # move operator to queue
        elif token in operators:
            if stack != []:
                t_precedence = get_token_prop(token,'prc')
                while (stack != []) and \
                      (get_token_prop(peek(stack),'prc') > t_precedence \
                      or (get_token_prop(peek(stack),'prc') == t_precedence and \
                          get_token_prop(peek(stack),'assoc') == 'left') \
                      and (peek(stack) != '(')):
                    output_queue.append(stack.pop()) # move operator to queue
            stack.append(token) # add operator to stack
        elif token == '(':
            stack.append(token) # add open paren to stac0k
        elif token == ')':
            if stack == [] or '(' not in stack:
                raise SyntaxError("Mismatched parentheses")
            while peek(stack) != '(':
                output_queue.append(stack.pop()) # move operator or function to queue
            if peek(stack) == '(':
                stack.pop() # discard open paren
        else: pass
    while stack != []: # move the rest of the stack to the queue
        if peek(stack) in priorities:
            raise SyntaxError("Mismatched parentheses")
        output_queue.append(stack.pop())
    return output_queue

# Stack machine
def calculate_on_stack(rpn_list):
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
