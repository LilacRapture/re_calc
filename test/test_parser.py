import calculator.expression_parser as parser
import unittest


class TestPattern(unittest.TestCase):

    def test_number_regex(self):
        self.assertRegex("1.44lk", parser.NUMBER_REGEX)
        self.assertRegex("1dfzs", parser.NUMBER_REGEX)
        self.assertRegex(".35dfss", parser.NUMBER_REGEX)
        self.assertNotRegex("lkjl", parser.NUMBER_REGEX)


class TestParsing(unittest.TestCase):

    def test_slice_by_pattern(self):
        input_string = "134+256"
        pattern_string = r"\d+"
        result = parser.slice_by_pattern(pattern_string, input_string)
        self.assertEqual(result, ("134", "+256"))

    def test_slice_by_pattern_negative(self):
        input_string = "sdf+256"
        pattern_string = r"\d+"
        result = parser.slice_by_pattern(pattern_string, input_string)
        self.assertEqual(result, None)

    def test_slice_by_string(self):
        input_string = "+98"
        prefix = "+"
        result = parser.slice_by_string(prefix, input_string)
        self.assertEqual(result, ("+", "98"))

    def test_slice_by_string_negative(self):
        input_string = "78+98"
        prefix = "-"
        result = parser.slice_by_string(prefix, input_string)
        self.assertEqual(result, None)

    def test_tokenization(self):
        expr = "1 + 2 - 3.45 * 4 / 5"
        tokens_list = parser.tokenize(expr)
        expected_list = [1.0, '+', 2.0, '-', 3.45, '*', 4.0, '/', 5.0]
        self.assertEqual(tokens_list, expected_list)

    def test_combine_unary_negation(self):
        tokens_list = ['-', 1.0, '-', 12.0, '-', '(', '-', 2.0, '*', '-', 3.0, ')', '-', '-', 5.0]
        result = parser.combine_unary_sign(tokens_list)
        expected_list = [-1.0, '-', 12.0, '-', '(', -2.0, '*', -3.0, ')', '-', -5.0]
        self.assertEqual(expected_list, result)

    def test_combine_unary_positivity(self):
        tokens_list = ['+', 1.0, '-', 12.0, '-', '(', '+', 2.0, '*', '+', 3.0, ')', '-', '+', 5.0]
        result = parser.combine_unary_sign(tokens_list)
        expected_list = [1.0, '-', 12.0, '-', '(', 2.0, '*', 3.0, ')', '-', 5.0]
        self.assertEqual(expected_list, result)

    def test_combine_unary_negation_pow(self):
        tokens_list = ['-', 1.0, '-', 12.0, '-', '(', '-', 2.0, '^', '-', 3.0, ')', '-', '-', 5.0]
        result = parser.combine_unary_sign(tokens_list)
        expected_list = [-1.0, '-', 12.0, '-', '(', -2.0, '^', -3.0, ')', '-', -5.0]
        self.assertEqual(expected_list, result)

    def test_combine_unary_negation_fun(self):
        tokens_list = [1.0, '-', '-', 'log', '(', 4.0, ',', 2.0, ')', '-', '-', 'sqrt', '(', 4.0, ')']
        result = parser.combine_unary_sign(tokens_list)
        expected_list = [1.0, '-', -1, '*', 'log', '(', 4.0, ',', 2.0, ')', '-', -1, '*', 'sqrt', '(', 4.0, ')']
        self.assertEqual(expected_list, result)

    def test_combine_unary_negation_sqrt(self):
        tokens_list = ['-', 'sqrt', '(', 4.0, ')']
        result = parser.combine_unary_sign(tokens_list)
        expected_list = [-1, '*', 'sqrt', '(', 4.0, ')']
        self.assertEqual(expected_list, result)