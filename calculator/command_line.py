import calculator.expression_parser as expression_parser
import calculator.shunting_yard as shunting_yard
import calculator.stack_machine as stack_machine

def process_args(args):
    _, *expression_list = args
    expression = " ".join(expression_list)
    tokens = expression_parser.tokenize(expression)
    rpn_list = shunting_yard.infix_to_prn(tokens)
    return stack_machine.calculate(rpn_list)
