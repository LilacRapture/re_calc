import unittest

# temp expression for testing
expr = "1 + 2 - 3 * 4 / 5"

# list of operators
ops2 = ('*', '/')
ops1 = ('+', '-')
priorities = ('(', ')')

# convert expression to tokens
def tokenize(expr):
    tokens_list = expr.split()
    for k in range(len(tokens_list)):
        token = tokens_list[k]
        if token in (ops1 + ops2 + priorities):
            continue
        else:
            tokens_list[k] = int(token)
    return tokens_list

# checks whether a token is an operator
def is_operation(token):
    return True if token in (ops1 + ops2) else False

# checks whether a token is a number
def is_number(integer):
    try:
        float(integer)
        return True
    except Exception as e:
        return False

# checks whether a token is a priority separator
def is_priority(token):
    return True if token in priorities else False

# sorint station algorithm
def sorting_station(tokens):
    output_queue = list()
    stack = list()
    for token in tokens:
        print(token)
        #print(tokens)
        print("Stack ", stack)
        print("Queue ", output_queue)
        if is_number(token):
            output_queue.append(token)
        elif token in (ops1 + ops2):
            if stack != []:
                print("while started")
                while (stack[-1] in ops2) and (token != '('):
                    output_queue.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            print("SH1", stack[-1])

            while stack[-1] != '(':
                sh = stack.pop()
                print("SH2", sh)
                output_queue.append(sh)
            if stack[-1] == '(':
                stack.pop()
        else: pass
    print("Stack  PF", stack)
    print("Queue  PF", output_queue)

    while stack != []:
        output_queue.append(stack.pop())
    print("Stack  F", stack)
    print("Queue  F", output_queue)
    return output_queue


# Simple test
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
unittest.main()
