from math import log

# literal: {prc: precedence, assoc: associativity, fun: function, type: type}
token_properties = {
    '(': {'prc': 0,
          'type': "paren"},
    ')': {'prc': 0,
          'type': "paren"},
    '+': {'prc': 1,
          'assoc': 'left',
          'fun': lambda a, b: a + b,
          'type': "operator"},
    '-': {'prc': 1,
          'assoc': 'left',
          'fun': lambda a, b: a - b,
          'type': "operator"},
    '*': {'prc': 2,
          'assoc': 'left',
          'fun': lambda a, b: a * b,
          'type': "operator"},
    '/': {'prc': 2,
          'assoc': 'left',
          'fun': lambda a, b: a / b,
          'type': "operator"},
    '^': {'prc': 3,
          'assoc': 'right',
          'fun': lambda a, b: a ** b,
          'type': "operator"},
    ',': {'prc': 0,
          'type': "separator"},
    'log': {'prc': 4,
            'assoc': 'left',
            'fun': lambda a, b: log(a, b),
            'type': "function"},
    'sqrt': {'prc': 4,
            'assoc': 'left',
            'fun': lambda a: a**0.5,
            'type': "function"}}


def tokens_by_type(properties, type):
    return [token for token in properties.keys()
            if properties.get(token, {}).get('type') == type]


# extracting token lists by their priority type
operators = tokens_by_type(token_properties, "operator")
functions = tokens_by_type(token_properties, "function")
priorities = tokens_by_type(token_properties, "paren")
separators = tokens_by_type(token_properties, "separator")

control_tokens = (operators + priorities + functions + separators)


# get token property by literal and property name
def get_token_prop(literal, prop_name):
    return token_properties.get(literal).get(prop_name)
