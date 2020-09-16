class CalcException(Exception):

    """
    Attributes:
        token_position -- position of the token caused the error
        tokens_list
        message -- explanation
    """

    def __init__(self, token_position, tokens_list, message):
        self.token_position = token_position
        self.tokens_list = tokens_list
        self.message = message
        super().__init__(self.message)

def process_float_token(token):
    if isinstance(token, float):
        return "{0:g}".format(token)
    else:
        return token

def get_error_location(token_position, tokens_list):
    string_token_list = [process_float_token(token) for token in tokens_list]
    expression_line = ' '.join(string_token_list)
    padds_count = token_position
    padd = ' ' * 2
    padds_line = padd * padds_count + '^'
    return expression_line + '\n' + padds_line

def catch_calc_errors(f):
    try:
        return {'result': f(),
                'status': 'success'}
    except Exception as e:
        if hasattr(e, 'message') and hasattr(e, 'token_position') and hasattr(e, 'tokens_list'):
            return {'message': e.message,
                    'token_position': e.token_position,
                    'tokens_list': e.tokens_list,
                    'error_location': get_error_location(e.token_position, e.tokens_list),
                    'status': 'error'}
        else:
            raise Exception(message='not implemented')
