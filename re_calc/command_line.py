import re_calc.expression_parser as expression_parser
import re_calc.shunting_yard as shunting_yard
import re_calc.stack_machine as stack_machine


def process_args(args):
    _, *expression_list = args
    expression = " ".join(expression_list)
    tokens = expression_parser.tokenize(expression)
    rpn_list = shunting_yard.infix_to_rpn(tokens)
    return stack_machine.calculate(rpn_list)
