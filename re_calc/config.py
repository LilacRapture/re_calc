from math import log, sin, cos, tan, atan, factorial

# literal: {prc: precedence, assoc: associativity, fun: function,
# type: type, loc_string: description}
token_properties = {
    '(': {'prc': 0,
          'type': "paren"},
    ')': {'prc': 0,
          'type': "paren"},
    '+': {'prc': 1,
          'assoc': 'left',
          'fun': lambda a, b: a + b,
          'type': "operator",
          'loc_string': "t_plus"},
    '-': {'prc': 1,
          'assoc': 'left',
          'fun': lambda a, b: a - b,
          'type': "operator",
          'loc_string': "t_minus"},
    '*': {'prc': 2,
          'assoc': 'left',
          'fun': lambda a, b: a * b,
          'type': "operator",
          'loc_string': "t_multiply"},
    '/': {'prc': 2,
          'assoc': 'left',
          'fun': lambda a, b: a / b,
          'type': "operator",
          'loc_string': "t_divide"},
    '^': {'prc': 3,
          'assoc': 'right',
          'fun': lambda a, b: a ** b,
          'type': "operator",
          'loc_string': "t_power"},
    ',': {'prc': 0,
          'type': "separator"},
    'log': {'prc': 4,
            'assoc': 'left',
            'fun': lambda a, b: log(a, b),
            'type': "function",
            'loc_string': "t_logarithm"},
    'sqrt': {'prc': 4,
             'assoc': 'left',
             'fun': lambda a: a ** 0.5,
             'type': "function",
             'loc_string': "t_square_root"},
    'abs': {'prc': 4,
            'assoc': 'left',
            'fun': lambda a: abs(a),
            'type': "function",
            'loc_string': "t_absolute_value"},
    'sin': {'prc': 4,
            'assoc': 'left',
            'fun': lambda a: sin(a),
            'type': "function",
            'loc_string': "t_sin"},
    'cos': {'prc': 4,
            'assoc': 'left',
            'fun': lambda a: cos(a),
            'type': "function",
            'loc_string': "t_cos"},
    'tan': {'prc': 4,
            'assoc': 'left',
            'fun': lambda a: tan(a),
            'type': "function",
            'loc_string': "t_tan"},
    'atan': {'prc': 4,
            'assoc': 'left',
            'fun': lambda a: atan(a),
            'type': "function",
            'loc_string': "t_atan"},
    'factorial': {'prc': 4,
            'assoc': 'left',
            'fun': lambda a: factorial(a),
            'type': "function",
            'loc_string': "t_factorial"}}


def tokens_by_type(properties, token_type):
    return [token for token in properties.keys()
            if properties.get(token, {}).get('type') == token_type]


# extracting token lists by their priority type
operators = tokens_by_type(token_properties, "operator")
functions = tokens_by_type(token_properties, "function")
priorities = tokens_by_type(token_properties, "paren")
separators = tokens_by_type(token_properties, "separator")

control_tokens = (operators + priorities + functions + separators)


# get token property by literal and property name
def get_token_prop(literal, prop_name):
    return token_properties.get(literal).get(prop_name)
