# TODO: add coverage calculation
# TODO: add functions support
# TODO: RegEx tokenizer

from math import log
import unittest

# literal: {prc: precedence, assoc: associativity, fun: function, type: type}
token_properties = {
    '(': {"prc": 0,
          "assoc": None,
          "fun": None,
          "type": "paren"},
    ')': {"prc": 0,
          "assoc": None,
          "fun": None,
          "type": "paren"},
    '+': {"prc": 1,
          "assoc": 'left',
          "fun": lambda a, b : a + b,
          "type": "operator"},
    '-': {"prc": 1,
          "assoc": 'left',
          "fun": lambda a, b : a - b,
          "type": "operator"},
    '*': {"prc": 2,
          "assoc": 'left',
          "fun": lambda a, b : a * b,
          "type": "operator"},
    '/': {"prc": 2,
          "assoc": 'left',
          "fun": lambda a, b : a / b,
          "type": "operator"},
    '**': {"prc": 3,
          "assoc": 'right',
          "fun": lambda a, b : a ** b,
          "type": "operator"},
    ',': {"prc": 0,
          "assoc": None,
          "fun": None,
          "type": "separator"},
    'log': {"prc": 0,
            "assoc": 'left',
            "fun": lambda a, b : log(a, b),
            "type": "function"}}

def tokens_by_type(token_properties, type):
    return list(dict((token, props) for token, props in token_properties.items() \
           if props.get('type') == type).keys())

# extracting token lists by their priority type
operators = tokens_by_type(token_properties, "operator")
functions = tokens_by_type(token_properties, "function")
priorities = tokens_by_type(token_properties, "paren")
separators = tokens_by_type(token_properties, "separator")

# get token property by literal and property name
def get_token_prop(literal, prop_name):
    return token_properties.get(literal).get(prop_name)

# convert expression to tokens
def tokenize(expr):
    tokens_list = expr.split()
    for k in range(len(tokens_list)):
        token = tokens_list[k]
        if token in (operators + priorities + functions + separators):
            continue
        else:
            tokens_list[k] = float(token)
    return tokens_list

# checks whether a token is an operator
def is_operation(token):
    return True if token in operators else False

# checks whether a token is a number
def is_number(number):
    try:
        float(number)
        return True
    except Exception as e:
        return False

#TODO: add test
def is_function(token):
    return True if token in functions else False

# checks whether a token is a priority separator
def is_priority(token):
    return True if token in priorities else False

def peek(stack):
    return stack[-1]

# Sorting station algorithm
def sorting_station(tokens):
    output_queue = list()
    stack = list()
    for token in tokens:
        if is_number(token):
            output_queue.append(token) # add number to queue
        elif is_function(token):
            stack.append(token) # add function to stack
        elif token in separators:
            if stack == [] or '(' not in stack:
                raise SyntaxError("Missing parentheses or separator")
            while (stack != []) and peek(stack) != "(":
                output_queue.append(stack.pop()) # move operator to queue
        elif token in operators:
            if stack != []:
                t_precedence = get_token_prop(token,"prc")
                while (stack != []) and \
                      (get_token_prop(peek(stack),"prc") > t_precedence \
                      or (get_token_prop(peek(stack),"prc") == t_precedence and \
                          get_token_prop(peek(stack),"assoc") == 'left') \
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
            op_function = properties.get("fun")
            stack.append(op_function(operand_1, operand_2))
    return stack.pop()
