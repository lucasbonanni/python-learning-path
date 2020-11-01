# this code is in the beginning of the test_calculator.py file
# Run the unit test using python -m unittest test_calculator
# python -m unittest If we do not specify the name of the test file, only files which start with the "test" will be executed.
from stage5 import Regexp
import unittest

class TestStage(unittest.TestCase):

    def test_case1(self):
        code = '^app|apple'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case2(self):
        code = 'le$|apple'
        exp = Regexp(code)
        self.assertTrue(exp.result)

    def test_case3(self):
        code = '^a|apple'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case4(self):
        code = '.$|apple'
        exp = Regexp(code)
        self.assertTrue(exp.result)

    def test_case5(self):
        code = 'apple$|tasty apple'
        exp = Regexp(code)
        self.assertTrue(exp.result)

    def test_case6(self): #repetido
        code = 'apple$|tasty apple'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case7(self):
        code = '^apple$|apple'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case8(self):
        code = '^apple$|tasty apple'
        exp = Regexp(code)
        self.assertFalse(exp.result)
    
    def test_case9(self):
        code = '^apple$|apple pie'
        exp = Regexp(code)
        self.assertFalse(exp.result)
    
    def test_case10(self):
        code = 'app$|apple'
        exp = Regexp(code)
        self.assertFalse(exp.result)
    
    def test_case11(self):
        code = '^le|apple'
        exp = Regexp(code)
        self.assertFalse(exp.result)

if __name__ == "__main__": # This enables us to run it directly using python filename.py
    unittest.main()