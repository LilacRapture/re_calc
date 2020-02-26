from calculator.shunting_yard import sorting_station
from calculator.expression_parser import tokenize
import unittest

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
