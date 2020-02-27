import calculator.stack_machine as stack_machine
from calculator.expression_parser import tokenize
import unittest


class TestStackMachine(unittest.TestCase):

    def test_stack_machine(self):
        rpn_list = [1.0, 2.0, '+', 3.0, '/']
        result = stack_machine.calculate(rpn_list)
        expected_result = 1.0
        self.assertEqual(result, expected_result)

    def test_not_implemented_op(self):
        rpn_list = [1.0, 2.0, '$', 3.0, '/']
        with self.assertRaises(NameError, msg="Not implemented: $"):
            stack_machine.calculate(rpn_list)

    def test_right_associativity(self):
        rpn_list = [1.0, 1.0, '+', 2.0, '^']
        result = stack_machine.calculate(rpn_list)
        expected_result = 4.0
        self.assertEqual(result, expected_result)

    def test_function(self):
        rpn_list = [1.0, 27.0, 3.0, 'log', '+']
        result = stack_machine.calculate(rpn_list)
        expected_result = 4.0
        self.assertEqual(result, expected_result)

    def test_function_with_power(self):
        rpn_list = [2.0, 27.0, 3.0, 'log', '^']
        result = stack_machine.calculate(rpn_list)
        expected_result = 8.0
        self.assertEqual(result, expected_result)

    def test_function_with_double_power(self):
        rpn_list = [3.0, 9.0, 3.0, 'log', 2.0, '^', '^']
        result = stack_machine.calculate(rpn_list)
        expected_result = 81.0
        self.assertEqual(result, expected_result)

    def test_get_arity(self):
        def fun_two_args(a, b): return a + b
        def fun_three_args(a, b, c): return a ** 2 + b ** 2 == c ** 2
        self.assertEqual(stack_machine.get_arity(fun_two_args), 2)
        self.assertEqual(stack_machine.get_arity(fun_three_args), 3)

    def test_unary_operator(self):
        rpn_list = [4.0, 'sqrt']
        result = stack_machine.calculate(rpn_list)
        self.assertEqual(result, 2.0)
