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

def catch_calc_errors(f):
    try:
        f()
    except Exception as e:
        if hasattr(e, 'message') and hasattr(e, 'token_position') and hasattr(e, 'tokens_list'):
            return e.tokens_list
        else:
            raise Exception(message='not implemented')
