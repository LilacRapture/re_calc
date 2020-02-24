from ReCalc import control_tokens
import re
import unittest

integer_regex = r"(\d+)"
tech_fractional_float = r"(\.\d+)"
float_regex = r"(\d+\.\d+)"
# regex for different num formats are joined by "regex OR" separator
NUMBER_REGEX = r"|".join([float_regex, tech_fractional_float, integer_regex])

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

# if string begins with some prefix (control tokens), return prefix and remaining string tuple
def slice_by_string(prefix, input_string):
    if not input_string.startswith(prefix):
        return None
    else:
        chars_to_cut = len(prefix)
        return (prefix, input_string[chars_to_cut:])

# parse expression independent of spaces
def parse_expression(expression):
    parsing_expression = expression
    output_queue = list()
    while parsing_expression != '':
        result = slice_by_pattern(NUMBER_REGEX, parsing_expression)
        if result != None:
            token, remaining_string = result
            output_queue.append(token)
            parsing_expression = remaining_string
        else:
            found_control_token = False
            for token in control_tokens:
                result = slice_by_string(token, parsing_expression)
                if result != None:
                    token, remaining_string = result
                    output_queue.append(token)
                    parsing_expression = remaining_string
                    found_control_token = True
                    break
            if found_control_token == False:
                raise SyntaxError('Unknown token')
    return output_queue

class TestPatterns(unittest.TestCase):

    def test_number(self):
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

unittest.main(verbosity=2)
