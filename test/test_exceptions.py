import re_calc.exceptions as exceptions
from re_calc.exceptions import CalcException
import unittest

def excepting_function():
    raise CalcException(2, ['1', '+', '2'], message='message')

class TestExceptions(unittest.TestCase):

    def test_catch_calc_exceptions(self):
        result = exceptions.catch_calc_errors(excepting_function)
        expected_location = '1 + 2\n    ^'
        print('\n' + expected_location)
        self.assertEqual(expected_location, result['error_location'])
