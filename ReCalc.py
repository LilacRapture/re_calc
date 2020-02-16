import unittest

# temp expression for testing
expr = "1 + 2 - 3 * 4 / 5"

# list of operators
ops2 = ('*', '/')
ops1 = ('+', '-')
operators = ops1 + ops2
priorities = ('(', ')')

# convert expression to tokens
def tokenize(expr):
    tokens_list = expr.split()
    for k in range(len(tokens_list)):
        token = tokens_list[k]
        if token in (operators + priorities):
            continue
        else:
            tokens_list[k] = int(token)
    return tokens_list

# checks whether a token is an operator
def is_operation(token):
    return True if token in operators else False

# checks whether a token is a number
def is_number(integer):
    try:
        float(integer) #why float&
        return True
    except Exception as e:
        return False

# checks whether a token is a priority separator
def is_priority(token):
    return True if token in priorities else False

def stack_to_queue(stack, output_queue):
    output_queue.append(stack.pop())

# sorint station algorithm
def sorting_station(tokens):
    output_queue = list()
    stack = list()
    for token in tokens:
        if is_number(token):
            output_queue.append(token) # add number to queue
        elif token in operators:
            if stack != []:
                while (stack[-1] in ops2) and (token != '('):
                    stack_to_queue(stack, output_queue) # move operator to queue
            stack.append(token) # add operator to stack
        elif token == '(':
            stack.append(token) # add open paren to stack
        elif token == ')':
            while stack[-1] != '(':
                stack_to_queue(stack, output_queue) # move operator to queue
            if stack[-1] == '(':
                stack.pop() # discard open paren
        else: pass
    while stack != []: # move the rest of the stack to the queue
        stack_to_queue(stack, output_queue)
    return output_queue

def calculate(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a / b

def calculate_on_stack(rpn_list):
    stack = list()
    args = list()
    for token in rpn_list:
        if is_number(token):
            stack.append(token)
        else:
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            stack.append(calculate(token, operand_1, operand_2))
    return stack.pop()

# Testing input processing functions
class TestCalc(unittest.TestCase):

    def test_tokenization(self):
        expr = "1 + 2 - 3 * 4 / 5"
        tokens_list = tokenize(expr)
        expected_list = [1, '+', 2, '-', 3, '*', 4, '/', 5]
        self.assertEqual(tokens_list, expected_list)

    def test_is_operation(self):
        self.assertTrue(is_operation('+'))
        self.assertFalse(is_operation(2))

    def test_is_number(self):
        self.assertTrue(is_number('4'))
        self.assertFalse(is_number('*'))

    def test_is_priority(self):
        self.assertTrue(is_priority('('))
        self.assertFalse(is_priority(2))

# Testing sorting station itself
class TestSortingStation(unittest.TestCase):

    def test_sorting_station_simple(self):
        expr = "1 + 2"
        tokens_list = tokenize(expr)
        expected_list = [1, 2, '+']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_sorting_station_ops_priority(self):
        expr = "1 + 2 * 3"
        tokens_list = tokenize(expr)
        expected_list = [1, 2, 3, '*', '+']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_sorting_station_paren_priority(self):
        expr = "( 1 + 2 ) * 3"
        tokens_list = tokenize(expr)
        expected_list = [1, 2, '+', 3, '*']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

class TestStackMachine(unittest.TestCase):

    def test_calculate_on_stack(self):
        rpn_list = [1, 2, '+', 3, '*']
        result = calculate_on_stack(rpn_list)
        expected_result = 9
        self.assertEqual(result, expected_result)
unittest.main()
