import re_calc.exceptions as exceptions
from re_calc.exceptions import CalcException
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
