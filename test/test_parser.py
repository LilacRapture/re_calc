from src.expression_parser import *
from src.config import *
from src.ReCalc import *
import unittest

class TestPatterns(unittest.TestCase):

    def test_number_regex(self):
        self.assertRegex("1.44lk", NUMBER_REGEX)
        self.assertRegex("1dfzs", NUMBER_REGEX)
        self.assertRegex(".35dfss", NUMBER_REGEX)
        self.assertNotRegex("lkjl", NUMBER_REGEX)

class TestParsing(unittest.TestCase):

    def test_slice_by_pattern(self):
        input_string = "134+256"
        pattern_string = r"\d+"
        result = slice_by_pattern(pattern_string, input_string)
        self.assertEqual(result, ("134", "+256"))

    def test_slice_by_pattern_negative(self):
        input_string = "sdf+256"
        pattern_string = r"\d+"
        result = slice_by_pattern(pattern_string, input_string)
        self.assertEqual(result, None)

    def test_slice_by_string(self):
        input_string = "+98"
        prefix = "+"
        result = slice_by_string(prefix, input_string)
        self.assertEqual(result, ("+", "98"))

    def test_slice_by_string_negative(self):
        input_string = "78+98"
        prefix = "-"
        result = slice_by_string(prefix, input_string)
        self.assertEqual(result, None)

    def test_parse_expression(self):
        expression = '7-1/2(2.3+2)'
        expected_list = ['7', '-', '1', '/', '2', '(', '2.3', '+', '2', ')']
        self.assertEqual(parse_expression(expression), expected_list)

class TestTokenization(unittest.TestCase):

    def test_tokenization(self):
        expr = "1 + 2 - 3 * 4 / 5"
        tokens_list = tokenize(expr)
        expected_list = [1.0, '+', 2.0, '-', 3.0, '*', 4.0, '/', 5.0]
        self.assertEqual(tokens_list, expected_list)

if __name__ == '__main__':
    unittest.main(verbosity=2)
