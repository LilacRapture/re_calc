from calculator.config import control_tokens
import re

integer_regex = r"(\d+)"
tech_fractional_float = r"(\.\d+)"
float_regex = r"(\d+\.\d+)"
# regex for different num formats are joined by "regex OR" separator
NUMBER_REGEX = r"|".join([float_regex, tech_fractional_float, integer_regex])


# slices the matching part of the string using regex;
# returns the matching part and the remaining string
# if pattern doesn't match returns None
def slice_by_pattern(pattern_string, input_string):
    pattern = re.compile(pattern_string)
    match_object = pattern.match(input_string)
    if match_object is None:
        return None
    else:
        start_idx, end_idx = match_object.span()
        return input_string[start_idx:end_idx], input_string[end_idx:]


# if string begins with some prefix (control tokens), return prefix and remaining string tuple
def slice_by_string(prefix, input_string):
    if not input_string.startswith(prefix):
        return None
    else:
        chars_to_cut = len(prefix)
        return prefix, input_string[chars_to_cut:]


def clean_expression(expression):
    return expression.replace(' ', '')


# returns tokens list with parsed floats and control tokens
def tokenize(expression):
    parsing_expression = clean_expression(expression)  # will be rewritten each round
    output_queue = list()
    while parsing_expression != '':
        result = slice_by_pattern(NUMBER_REGEX, parsing_expression)
        if result is not None:
            token, remaining_string = result
            output_queue.append(float(token))  # add number to the output
            parsing_expression = remaining_string
        else:
            found_control_token = False
            for token in control_tokens:
                result = slice_by_string(token, parsing_expression)
                if result is not None:
                    token, remaining_string = result
                    output_queue.append(token)  # add control token to the output
                    parsing_expression = remaining_string
                    found_control_token = True
                    break
            if not found_control_token:
                raise SyntaxError('Unknown token')
    return output_queue
