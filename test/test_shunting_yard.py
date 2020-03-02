import calculator.shunting_yard as shunting_yard
from calculator.expression_parser import tokenize
import unittest


class TestShuntingYard(unittest.TestCase):

    def test_shunting_yard_simple(self):
        expr = "1 + 2.0"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 2.0, '+']
        output_queue = shunting_yard.infix_to_prn(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_shunting_yard_ops_priority(self):
        expr = "1 + 2 * 3"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 2.0, 3.0, '*', '+']
        output_queue = shunting_yard.infix_to_prn(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_shunting_yard_paren_priority(self):
        expr = "(1 + 2) * 3"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 2.0, '+', 3.0, '*']
        output_queue = shunting_yard.infix_to_prn(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_shunting_yard_paren_priority_complex(self):
        expr = "1 + 2 + 3 + (6 / 8)"
        tokens_list = tokenize(expr)
        expected_list = [1, 2, '+', 3, '+', 6, 8, '/', '+']
        output_queue = shunting_yard.infix_to_prn(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_shunting_yard_right_associativity(self):
        expr = "(1 + 1) ^ 2"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 1.0, '+', 2.0, '^']
        output_queue = shunting_yard.infix_to_prn(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_mismatched_parens_right(self):
        expr = "(1 + 2 (- 3) * 4 / 5 (4 (4 ("
        tokens_list = tokenize(expr)
        with self.assertRaises(SyntaxError, msg="Mismatched parentheses"):
            shunting_yard.infix_to_prn(tokens_list)

    def test_mismatched_parens_left(self):
        expr = "(1 + 2) - 3)) * 4 / 5)"
        tokens_list = tokenize(expr)
        with self.assertRaises(SyntaxError, msg="Mismatched parentheses"):
            shunting_yard.infix_to_prn(tokens_list)

    def test_shunting_yard_function(self):
        expr = "1 + log(27, 3) * 3"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 27.0, 3.0, 'log', 3.0, '*', '+']
        output_queue = shunting_yard.infix_to_prn(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_shunting_yard_function_with_power(self):
        expr = "2^log(27 , 3)"
        tokens_list = tokenize(expr)
        expected_list = [2.0, 27.0, 3.0, 'log', '^']
        output_queue = shunting_yard.infix_to_prn(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_shunting_yard_function_with_double_power(self):
        expr = "3^log(9 , 3)^2"
        tokens_list = tokenize(expr)
        expected_list = [3.0, 9.0, 3.0, 'log', 2.0, '^', '^']
        output_queue = shunting_yard.infix_to_prn(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_shunting_yard_unary(self):
        expr = "1 + sqrt(9)*2"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 9.0, 'sqrt', 2.0, '*', '+']
        output_queue = shunting_yard.infix_to_prn(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_shunting_yard_abs(self):
        expr = "1 - abs(-2)"
        tokens_list = tokenize(expr)
        expected_list = [1.0, -2.0, 'abs', '-']
        output_queue = shunting_yard.infix_to_prn(tokens_list)
        self.assertEqual(output_queue, expected_list)
