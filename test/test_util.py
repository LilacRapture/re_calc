from re_calc.util import is_number, every
import unittest


class TestInputProcessing(unittest.TestCase):

    def test_is_number(self):
        self.assertTrue(is_number('4.0'))
        self.assertFalse(is_number('*'))

    def test_every(self):
        numbers_list = [1, 2, 4, 5]
        result = every(lambda x: x % 2 == 0, numbers_list)
        self.assertFalse(result)
        numbers_list_2 = (2, 6, 8)
        result_2 = every(lambda x: x % 2 == 0, numbers_list_2)
        self.assertTrue(result_2)
