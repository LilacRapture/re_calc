# TODO: add coverage calculation
# TODO: add functions support
# TODO: add command line interface
# TODO: RegEx tokenizer

import unittest

# list of operators
operators = ('*', '/', '+', '-', '**')
priorities = ('(', ')')

# literal: (precedence, associativity, operator)
operator_properties = {
    '(': {"priority": 0,
          "assoc": None,
          "fun": None},
    ')': {"priority": 0,
          "assoc": None,
          "fun": None},
    '+': {"priority": 1,
          "assoc": 'left',
          "fun": lambda a, b : a + b},
    '-': {"priority": 1,
          "assoc": 'left',
          "fun": lambda a, b : a - b},
    '*': {"priority": 2,
          "assoc": 'left',
          "fun": lambda a, b : a * b},
    '/': {"priority": 2,
          "assoc": 'left',
          "fun": lambda a, b : a / b},
    '**': {"priority": 3,
          "assoc": 'right',
          "fun": lambda a, b : a ** b}}

# def get_op_properties(literal):
#     return operator_properties.get(literal)

def get_op_prop(literal, prop_name):
    return operator_properties.get(literal).get(prop_name)

# convert expression to tokens
def tokenize(expr):
    tokens_list = expr.split()
    for k in range(len(tokens_list)):
        token = tokens_list[k]
        if token in (operators + priorities):
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
        elif token in operators:
            if stack != []:
                t_precedence = get_op_prop(token,"priority")
                while (stack != []) and \
                      (get_op_prop(peek(stack),"priority") > t_precedence \
                      or (get_op_prop(peek(stack),"priority") == t_precedence and \
                          get_op_prop(peek(stack),"assoc") == 'left') \
                      and (peek(stack) != '(')):
                    output_queue.append(stack.pop()) # move operator to queue
            stack.append(token) # add operator to stack
        elif token == '(':
            stack.append(token) # add open paren to stac0k
        elif token == ')':
            if stack == [] or '(' not in stack:
                raise SyntaxError("Mismatched parentheses")
            while peek(stack) != '(':
                output_queue.append(stack.pop()) # move operator to queue
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
            properties = operator_properties.get(token)
            if properties == None:
                raise NameError("Not implemented: ", token)
            operator = properties.get("fun")
            stack.append(operator(operand_1, operand_2))
    return stack.pop()
