import re
import string
import unittest

integer_regex = r"(\d+)"
tech_fractional_float = r"(\.\d+)"
float_regex = r"(\d+\.\d+)"
# regex for different num formats are joined by "regex OR" separator
number_regex = r"|".join([float_regex, tech_fractional_float, integer_regex])

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

class TestPatterns(unittest.TestCase):

    def test_number(self):
        self.assertRegex("1.44lk", number_regex)
        self.assertRegex("1dfzs", number_regex)
        self.assertRegex(".35dfss", number_regex)
        self.assertNotRegex("lkjl", number_regex)

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
