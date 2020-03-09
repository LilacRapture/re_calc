import re_calc.command_line as command_line
import unittest


class TestCommandLine(unittest.TestCase):

    def test_process_args(self):
        args_list = ["module_name", '1', '*', '3.5', '/', '.5']
        result = command_line.process_args(args_list)
        self.assertEqual(7.0, result)
