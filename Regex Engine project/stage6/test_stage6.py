# this code is in the beginning of the test_calculator.py file
# Run the unit test using python -m unittest test_calculator
# python -m unittest If we do not specify the name of the test file, only files which start with the "test" will be executed.
from stage6 import search
import unittest


class TestStage(unittest.TestCase):

    def test_case1(self):
        code = '\.$|end.'
        self.assertTrue(search(*code.split('|')))
    def test_case1(self):
        code = '3\+3|3+3=6'
        self.assertTrue(search(*code.split('|')))
    def test_case1(self):
        code = '\?|Is this working?'
        self.assertTrue(search(*code.split('|')))
    def test_case1(self):
        code = '\\|\\'
        self.assertTrue(search(*code.split('|')))
    def test_case1(self):
        code = 'colou\?r|color'
        self.assertTrue(search(*code.split('|')))
    def test_case1(self):
        code = 'colou\?r|colour'
        self.assertTrue(search(*code.split('|')))

if __name__ == "__main__": # This enables us to run it directly using python filename.py
    unittest.main()