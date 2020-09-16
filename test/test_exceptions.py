import re_calc.exceptions as exceptions
from re_calc.exceptions import CalcException
import unittest

def excepting_function():
    raise CalcException(3, ['1', '+', '2'], message='message')

class TestExceptions(unittest.TestCase):

    def test_catch_calc_exceptions(self):
        result = exceptions.catch_calc_errors(excepting_function)
        self.assertEqual(['1', '+', '2'], result)
