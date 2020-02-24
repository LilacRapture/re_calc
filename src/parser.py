import re
import unittest

integer_regex = r"(\d+)"
tech_fractional_float = r"(\.\d+)"
float_regex = r"(\d+\.\d+)"
# regex for different num formats are joined by "regex OR" separator
number_regex = r"|".join([float_regex, tech_fractional_float, integer_regex])

add_regex = r"(\+)"
substract_regex = r"(\-)"
multiply_regex = r"(\*)"
divide_regex = r"(\/)"
power_regex = r"(\^)"

# slices the matching part of the string; returns the matching part and the remaining string
# if pattern doesn't match returns None
def slice_by_pattern(pattern_string, input_string):
    pattern = re.compile(pattern_string)
    match_object = pattern.match(input_string)
    if match_object == None:
        return None
    else:
        start_idx, end_idx = match_object.span()
        return (input_string[start_idx:end_idx], input_string[end_idx:])

# def parse_expression(expression):
#     parsing_expression = expression
#     output_queue = list()
#     while parsing_expression != '':
#         # try to parse sequentially
#             # (number
#             # control token literals (ops, parens, funcs, separators))
#                 # put parsed_token to output_queue
#                 # update parse_expression with remaining part
#             # if nothing found throw Exception


class TestPatterns(unittest.TestCase):

    # start of the line RegEx
    line_start = "^"

    def test_number(self):
        self.assertRegex("1.44lk", number_regex)
        self.assertRegex("1dfzs", number_regex)
        self.assertRegex(".35dfss", number_regex)
        self.assertNotRegex("lkjl", number_regex)

    def test_add(self):
        self.assertRegex("+38", self.line_start + add_regex)
        self.assertNotRegex("2.45+16", self.line_start + add_regex)

    def test_substract(self):
        self.assertRegex("-2.22", self.line_start + substract_regex)
        self.assertNotRegex("12-56", self.line_start + substract_regex)

    def test_multiply(self):
        self.assertRegex("*44", self.line_start + multiply_regex)
        self.assertNotRegex("87*220", self.line_start + multiply_regex)

    def test_divide(self):
        self.assertRegex("/3", self.line_start + divide_regex)
        self.assertNotRegex("78/2", self.line_start + divide_regex)

    def test_power(self):
        self.assertRegex("^4", self.line_start + power_regex)
        self.assertNotRegex("8^2", self.line_start + power_regex)


    def test_slice(self):
        input_string = "134+256"
        pattern_string = r"\d+"
        result = slice_by_pattern(pattern_string, input_string)
        self.assertEqual(result, ("134", "+256"))

    def test_slice_negative(self):
        input_string = "sdf+256"
        pattern_string = r"\d+"
        result = slice_by_pattern(pattern_string, input_string)
        self.assertEqual(result, None)

unittest.main(verbosity=2)
