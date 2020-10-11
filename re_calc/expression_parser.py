from re_calc.config import control_tokens, operators, functions
from re_calc.util import is_number
from re_calc.exceptions import CalcException

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
    if match_object:
        start_idx, end_idx = match_object.span()
        return input_string[start_idx:end_idx], input_string[end_idx:]


# if string begins with some prefix (control tokens), return prefix and remaining string tuple
def slice_by_string(prefix, input_string):
    if input_string.startswith(prefix):
        chars_to_cut = len(prefix)
        return prefix, input_string[chars_to_cut:]


# Combines unary signs with adjacent value
def combine_unary_sign(tokens_list):
    output_queue = list()
    while tokens_list[:-1]:
        token = tokens_list[0]
        next_token = tokens_list[1]
        if not output_queue or output_queue[-1] in operators + ['(']:
            if token == '-' and is_number(next_token):
                output_queue.append(next_token * (-1))
                tokens_list.pop(0)
            elif token == '-' and next_token in functions:
                output_queue.extend([-1, '*', next_token])
                tokens_list.pop(0)
            else:
                output_queue.append(token)
        else:
            output_queue.append(token)
        tokens_list.pop(0)
    return output_queue + tokens_list


# returns tokens list with parsed floats and control tokens
def tokenize(expression):
    parsing_expression = expression.strip()
    output_queue = list()
    while parsing_expression != '':
        result = slice_by_pattern(NUMBER_REGEX, parsing_expression)
        if result:
            token, remaining_string = result
            output_queue.append(float(token))  # add number to the output
            parsing_expression = remaining_string.strip()
        else:
            found_control_token = False
            for token in control_tokens:
                result = slice_by_string(token, parsing_expression)
                if result:
                    token, remaining_string = result
                    output_queue.append(token)  # add control token to the output
                    parsing_expression = remaining_string.strip()
                    found_control_token = True
                    break
            if not found_control_token:
                combined_token_list = combine_unary_sign(output_queue)
                combined_token_list.append(parsing_expression)
                error_tokens = combined_token_list
                token_position = len(combined_token_list) - 1
                raise CalcException(token_position, error_tokens, message='Unknown token')
    return combine_unary_sign(output_queue)
