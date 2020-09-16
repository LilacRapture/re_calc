import re_calc.exceptions as exceptions
from re_calc.exceptions import CalcException
import re_calc.expression_parser as parser
import unittest

def excepting_function():
    raise CalcException(2, ['1', '+', '2'], message='message')

def regular_function():
    return 'calc'

class TestExceptions(unittest.TestCase):

    def test_catch_calc_exceptions(self):
        result = exceptions.catch_calc_errors(excepting_function)
        expected_location = '1 + 2\n    ^'
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

    #@unittest.skip("demonstrating skipping")
    def test_catch_parser_exception(self):
        expr = "1 + 2 - 3.45 + lkjkl * 4 / 5"
        result = exceptions.catch_calc_errors(lambda: parser.tokenize(expr))
        self.assertEqual('error', result['status'])
