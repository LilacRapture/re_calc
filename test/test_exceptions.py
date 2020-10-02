import re_calc.exceptions as exceptions
import re_calc.shunting_yard as shunting_yard
import re_calc.stack_machine as stack_machine
import re_calc.expression_parser as parser
from re_calc.exceptions import CalcException

import unittest


def excepting_function():
    raise CalcException(4, ['1', '+', '2.1', '-', '23'], message='message')


def regular_function():
    return 'calc'


class TestExceptions(unittest.TestCase):

    def test_catch_calc_exceptions(self):
        result = exceptions.catch_calc_errors(excepting_function)
        expression_line = '1 + 2.1 - 23'
        padding_line    = '          ^'
        expected_location = expression_line + '\n' + padding_line
        self.assertEqual(expected_location, result['error_location'])

    def test_catch_calc_exceptions_regular(self):
        result = exceptions.catch_calc_errors(regular_function)
        self.assertEqual('success', result['status'])
        self.assertEqual('calc', result['result'])

    def test_process_float_token(self):
        result = exceptions.process_float_token(1.0)
        self.assertEqual('1', result)
        result_fractional = exceptions.process_float_token(1.23)
        self.assertEqual('1.23', result_fractional)


class TestParserExceptions(unittest.TestCase):

    def test_catch_parser_exception(self):
        expr = "1 + 2 - 3.45 + lkjkl * 4 / 5"
        result = exceptions.catch_calc_errors(lambda: parser.tokenize(expr))
        self.assertEqual('error', result['status'])

    def test_catch_left_paren_exception(self):
        expr = "(1 + 2) - 3)) * 4 / 5)"
        tokens_list = parser.tokenize(expr)
        result = exceptions.catch_calc_errors(lambda: shunting_yard.infix_to_rpn(tokens_list))
        self.assertEqual('error', result['status'])

    def test_catch_right_paren_exception(self):
        expr = "(1 + 2 (- 3) * 4 / 5 (4 (4 ()"
        tokens_list = parser.tokenize(expr)
        result = exceptions.catch_calc_errors(lambda: shunting_yard.infix_to_rpn(tokens_list))
        self.assertEqual('error', result['status'])

    def test_catch_parser_exception_normal_int(self):
        expr = "0.5 + 0.5"
        tokens_list = parser.tokenize(expr)
        rpn_list = shunting_yard.infix_to_rpn(tokens_list)
        result = exceptions.catch_calc_errors(lambda: stack_machine.calculate(rpn_list))
        self.assertEqual('success', result['status'])
        self.assertEqual('1', result['result'])

    def test_catch_parser_exception_normal_float(self):
        expr = "1.0 + 0.5"
        tokens_list = parser.tokenize(expr)
        rpn_list = shunting_yard.infix_to_rpn(tokens_list)
        result = exceptions.catch_calc_errors(lambda: stack_machine.calculate(rpn_list))
        self.assertEqual('success', result['status'])
        self.assertEqual('1.5', result['result'])

class TestStackMachineExceptions(unittest.TestCase):

    def test_catch_division_by_zero(self):
        rpn_list = [1.0, 0.0, '/']
        result = exceptions.catch_calc_errors(lambda: stack_machine.calculate(rpn_list))
        print("res", result)
        self.assertEqual('error', result['status'])
        self.assertEqual('Division by zero', result['message'])
