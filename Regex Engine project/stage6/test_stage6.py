# this code is in the beginning of the test_calculator.py file
# Run the unit test using python -m unittest test_calculator
# python -m unittest If we do not specify the name of the test file, only files which start with the "test" will be executed.
from stage6 import search
import unittest


class TestStage(unittest.TestCase):

    def test_case1(self):
        code = str(r'\.$|end.')
        self.assertTrue(search(*code.split('|')))
    def test_case2(self):
        code = r'3\+3|3+3=6'
        self.assertTrue(search(*code.split('|')))
    def test_case3(self):
        code = r'\?|Is this working?'
        self.assertTrue(search(*code.split('|')))
    def test_case4(self):
        code = '\\\\|\\'
        self.assertTrue(search(*code.split('|')))
    def test_case5(self):
        code = r'colou\?r|color'
        self.assertFalse(search(*code.split('|')))
    def test_case6(self):
        code = r'colou\?r|colour'
        self.assertFalse(search(*code.split('|')))

if __name__ == "__main__": # This enables us to run it directly using python filename.py
    unittest.main()