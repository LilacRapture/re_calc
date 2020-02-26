import calculator.expression_parser as expression_parser
import calculator.shunting_yard as shunting_yard
import calculator.stack_machine as stack_machine
import sys

if __name__ == "__main__":
    _, *expression_list = sys.argv
    expression = " ".join(expression_list)
    tokens = expression_parser.tokenize(expression)
    rpn_list = shunting_yard.sorting_station(tokens)
    result = stack_machine.calculate_on_stack(rpn_list)
    print(result)
