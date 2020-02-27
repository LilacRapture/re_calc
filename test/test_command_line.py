import calculator.command_line as command_line
import unittest


class TestCommandLine(unittest.TestCase):

    def test_process_args(self):
        args_list = ["module_name", '1', '*', '3.5', '/', '.5']
        result = command_line.process_args(args_list)
        self.assertEqual(result, 7.0)
