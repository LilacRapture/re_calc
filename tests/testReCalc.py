import unittest

# Testing input processing functions
class TestTokenization(unittest.TestCase):
    @unittest.skip("temp")
    def test_tokenization(self):
        expr = "1 + 2 - 3 * 4 / 5"
        tokens_list = tokenize(expr)
        expected_list = [1.0, '+', 2.0, '-', 3.0, '*', 4.0, '/', 5.0]
        self.assertEqual(tokens_list, expected_list)
    @unittest.skip("temp")
    def test_is_operation(self):
        self.assertTrue(is_operation('+'))
        self.assertFalse(is_operation(2.0))
    @unittest.skip("temp")
    def test_is_number(self):
        self.assertTrue(is_number('4.0'))
        self.assertFalse(is_number('*'))
    @unittest.skip("temp")
    def test_is_priority(self):
        self.assertTrue(is_priority('('))
        self.assertFalse(is_priority(2.0))

class TestSortingStation(unittest.TestCase):
    @unittest.skip("temp")
    def test_sorting_station_simple(self):
        expr = "1 + 2.0"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 2.0, '+']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)
    @unittest.skip("temp")
    def test_sorting_station_ops_priority(self):
        expr = "1 + 2 * 3"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 2.0, 3.0, '*', '+']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)
    @unittest.skip("temp")
    def test_sorting_station_paren_priority(self):
        expr = "( 1 + 2 ) * 3"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 2.0, '+', 3.0, '*']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)
    @unittest.skip("temp")
    def test_sorting_station_right_associativity(self):
        expr = "( 1 + 1 ) ** 2"
        tokens_list = tokenize(expr)
        expected_list = [1.0, 1.0, '+', 2.0, '**']
        output_queue = sorting_station(tokens_list)
        self.assertEqual(output_queue, expected_list)

    def test_mismatched_parens_right(self):
        expr = "( 1 + 2 ( - 3 ) * 4 / 5"
        tokens_list = tokenize(expr)
        with self.assertRaises(SyntaxError, msg="Mismatched parentheses"):
            sorting_station(tokens_list)

    def test_mismatched_parens_left(self):
        expr = "( 1 + 2 ) - 3 ) * 4 / 5"
        tokens_list = tokenize(expr)
        with self.assertRaises(SyntaxError, msg="Mismatched parentheses"):
            sorting_station(tokens_list)

class TestStackMachine(unittest.TestCase):
    @unittest.skip("temp")
    def test_calculate_on_stack(self):
        rpn_list = [1.0, 2.0, '+', 3.0, '/']
        result = calculate_on_stack(rpn_list)
        expected_result = 1.0
        self.assertEqual(result, expected_result)
    @unittest.skip("temp")
    def test_not_implemented_op(self):
        rpn_list = [1.0, 2.0, '$', 3.0, '/']
        with self.assertRaises(NameError, msg="Not implemented: $"):
            calculate_on_stack(rpn_list)
    @unittest.skip("temp")
    def test_right_associativity(self):
        rpn_list = [1.0, 1.0, '+', 2.0, '**']
        result = calculate_on_stack(rpn_list)
        expected_result = 4.0
        self.assertEqual(result, expected_result)

unittest.main(verbosity=2)
