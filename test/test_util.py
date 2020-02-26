from calculator.util import is_number
import unittest

class TestInputProcessing(unittest.TestCase):

    def test_is_number(self):
        self.assertTrue(is_number('4.0'))
        self.assertFalse(is_number('*'))
