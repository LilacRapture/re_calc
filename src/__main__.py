import ReCalc
import sys
if __name__ == "__main__":
    _, *expression_list = sys.argv
    expression = " ".join(expression_list)
    tokens = ReCalc.tokenize(expression)
    rpn_list = ReCalc.sorting_station(tokens)
    result = ReCalc.calculate_on_stack(rpn_list)
    print(result)
