from src.config import token_properties
from src.parser import *
from src.ReCalc import *
import unittest

class TestInputProcessing(unittest.TestCase):

    def test_get_token_prop(self):
        result = get_token_prop('log', 'assoc')
        self.assertEqual(result, 'left')

    def test_is_number(self):
        self.assertTrue(is_number('4.0'))
        self.assertFalse(is_number('*'))


class TestSortingStation(unittest.TestCase):

    def test_sorting_station_simple(self):
        expr = "1 + 2.0"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 2.0, '+']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_sorting_station_ops_priority(self):
        expr = "1 + 2 * 3"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 2.0, 3.0, '*', '+']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_sorting_station_paren_priority(self):
        expr = "( 1 + 2 ) * 3"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 2.0, '+', 3.0, '*']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_sorting_station_paren_priority_complex(self):
        expr = "1 + 2 + 3 + ( 6 / 8 )"
        tokens_list = tokenize(expr)
        expected_list = [1, 2, '+', 3, '+', 6, 8, '/', '+']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_sorting_station_right_associativity(self):
        expr = "( 1 + 1 ) ^ 2"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 1.0, '+', 2.0, '^']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_mismatched_parens_right(self):
        expr = "( 1 + 2 ( - 3 ) * 4 / 5 ( 4 ( 4 ("
        tokens_list = tokenize(expr)
        with self.assertRaises(SyntaxError, msg="Mismatched parentheses"):
            sorting_station(tokens_list)

    def test_mismatched_parens_left(self):
        expr = "( 1 + 2 ) - 3 ) ) * 4 / 5 )"
        tokens_list = tokenize(expr)
        with self.assertRaises(SyntaxError, msg="Mismatched parentheses"):
            sorting_station(tokens_list)

    def test_sorting_station_function(self):
        expr = "1 + log ( 27 , 3 ) * 3"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 27.0, 3.0, 'log', 3.0, '*', '+']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_sorting_station_function_with_power(self):
        expr = "2 ^ log ( 27 , 3 )"
        tokens_list = tokenize(expr)
        expected_list = [2.0, 27.0, 3.0, 'log', '^']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_sorting_station_function_with_double_power(self):
        expr = "3 ^ log ( 9 , 3 ) ^ 2"
        tokens_list = tokenize(expr)
        expected_list = [3.0, 9.0, 3.0, 'log', 2.0, '^', '^']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

class TestStackMachine(unittest.TestCase):

    def test_calculate_on_stack(self):
        rpn_list = [1.0, 2.0, '+', 3.0, '/']
        result = calculate_on_stack(rpn_list)
        expected_result = 1.0
        self.assertEqual(result, expected_result)

    def test_not_implemented_op(self):
        rpn_list = [1.0, 2.0, '$', 3.0, '/']
        with self.assertRaises(NameError, msg="Not implemented: $"):
            calculate_on_stack(rpn_list)

    def test_right_associativity(self):
        rpn_list = [1.0, 1.0, '+', 2.0, '^']
        result = calculate_on_stack(rpn_list)
        expected_result = 4.0
        self.assertEqual(result, expected_result)

    def test_function(self):
        rpn_list = [1.0, 27.0, 3.0, 'log', '+']
        result = calculate_on_stack(rpn_list)
        expected_result = 4.0
        self.assertEqual(result, expected_result)

    def test_function_with_power(self):
        rpn_list = [2.0, 27.0, 3.0, 'log', '^']
        result = calculate_on_stack(rpn_list)
        expected_result = 8.0
        self.assertEqual(result, expected_result)

    def test_function_with_double_power(self):
        rpn_list = [3.0, 9.0, 3.0, 'log', 2.0, '^', '^']
        result = calculate_on_stack(rpn_list)
        expected_result = 81.0
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
