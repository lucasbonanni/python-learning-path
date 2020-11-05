# this code is in the beginning of the test_calculator.py file
# Run the unit test using python -m unittest test_calculator
# python -m unittest If we do not specify the name of the test file, only files which start with the "test" will be executed.
from sol1 import search
import unittest
from inspect import currentframe, getframeinfo




class TestStage(unittest.TestCase):

    def test_case1(self):
        code = 'colou?r|color'
        self.assertTrue(search(*code.split('|')))
    
    def test_case2(self):
        code = 'colou?r|colour'
        self.assertTrue(search(*code.split('|')))

    def test_case3(self):
        code = 'colou?r|colouur'
        self.assertFalse(search(*code.split('|')))
    
    def test_case4(self):
        code = 'colou*r|color'
        self.assertTrue(search(*code.split('|')))

    def test_case5(self):
        code = 'colou*r|colour'
        self.assertTrue(search(*code.split('|')))

    def test_case6(self): 
        code = 'colou*r|colouur'
        self.assertTrue(search(*code.split('|')))
    
    def test_case7(self):
        code = 'col.*r|color'
        self.assertTrue(search(*code.split('|')))
    
    def test_case8(self):
        code = 'col.*r|colour'
        self.assertTrue(search(*code.split('|')))
    
    def test_case9(self):
        code = 'col.*r|colr'
        self.assertTrue(search(*code.split('|')))
    
    def test_case10(self):
        code = 'col.*r|collar'
        self.assertTrue(search(*code.split('|')))
    
    def test_case11(self):
        code = 'col.*r$|colors'
        self.assertFalse(search(*code.split('|')))
    
    def test_case13(self):
        code = 'colou+r|color'
        self.assertFalse(search(*code.split('|')))

    def test_case12(self):
        code = 'a|a'
        self.assertTrue(search(*code.split('|')))
    
    def test_case14(self):
        code = '.*|aaa'
        self.assertTrue(search(*code.split('|')))
    
    def test_case15(self):
        code = '.+|aaa'
        self.assertTrue(search(*code.split('|')))

    def test_case16(self):
        code = '.?|aaa'
        self.assertTrue(search(*code.split('|')))
    
    def test_case17(self):
        code = 'no+$|noooooooope'
        self.assertFalse(search(*code.split('|')))


if __name__ == "__main__": # This enables us to run it directly using python filename.py
    unittest.main()