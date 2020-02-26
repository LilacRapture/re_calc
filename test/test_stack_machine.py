from calculator.stack_machine import calculate_on_stack
from calculator.expression_parser import tokenize
import unittest

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
