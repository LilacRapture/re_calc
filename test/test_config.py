from calculator.config import tokens_by_type
import unittest

class TestConfig(unittest.TestCase):

    def test_tokens_by_type(self):
        dict = {')': {'type': "paren"},
                '+': {'type': "operator"}}
        result = tokens_by_type(dict, 'operator')
        self.assertEqual(result, ['+'])
