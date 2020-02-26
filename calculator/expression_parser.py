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

# parses expression independent of spaces
def parse_expression(expression):
    parsing_expression = expression # will be rewritten each round
    output_queue = list()
    while parsing_expression != '':
        result = slice_by_pattern(NUMBER_REGEX, parsing_expression)
        if result != None:
            token, remaining_string = result
            output_queue.append(token) # add number to the output
            parsing_expression = remaining_string
        else:
            found_control_token = False
            for token in control_tokens:
                result = slice_by_string(token, parsing_expression)
                if result != None:
                    token, remaining_string = result
                    output_queue.append(token) # add control token to the output
                    parsing_expression = remaining_string
                    found_control_token = True
                    break
            if found_control_token == False:
                raise SyntaxError('Unknown token')
    return output_queue

# parses tokens list and convert numbers to floats
def parse_floats(tokens_list):
    for k in range(len(tokens_list)):
        token = tokens_list[k]
        if token in control_tokens:
            continue
        else:
            tokens_list[k] = float(token)
    return tokens_list

# returns tokens list with parsed floats and contol tokens
def tokenize(expression):
    tokens_list = parse_expression(expression.replace(' ','')) # removes whitespaces
    return parse_floats(tokens_list)
