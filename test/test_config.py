from calculator.config import tokens_by_type, get_token_prop
import unittest


class TestConfig(unittest.TestCase):



    def test_tokens_by_type(self):
        props = {')': {'type': "paren"},
                 '+': {'type': "operator"}}
        result = tokens_by_type(props, 'operator')
        self.assertEqual(result, ['+'])

    def test_get_token_prop(self):
        result = get_token_prop('log', 'assoc')
        self.assertEqual(result, 'left')
