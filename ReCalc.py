import unittest

expr = "1 + 2 - 3 * 4 / 5"

ops = ('+', '-', '*', '/')

def tokenize(expr):
    tokens_list = expr.split()
    for k in range(len(tokens_list)):
        token = tokens_list[k]
        if token in ops:
            continue
        else:
            tokens_list[k] = int(token)
    return tokens_list

def is_operation(token):
    return True if (token in ops) else False

def is_number(integer):
    try:
        float(integer)
        return True
    except Exception as e:
        return False

# TODO: add predicate for priority separator

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

unittest.main()
