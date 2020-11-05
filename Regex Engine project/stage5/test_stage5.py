# this code is in the beginning of the test_calculator.py file
# Run the unit test using python -m unittest test_calculator
# python -m unittest If we do not specify the name of the test file, only files which start with the "test" will be executed.
from stage5 import Regexp
import unittest
from inspect import currentframe, getframeinfo


# def count_char_matches(text,starting_pos, final_letter):
#     """

#     """
#     # print('text:' + text,'pos:' + str(starting_pos),'final_letter:' +final_letter)
#     counter = 0
#     for pos in range(starting_pos,len(text),1):
#         if text[pos] != final_letter:
#             print('test',text[pos],pos,len(text), 'color'[3])
#             counter +=1
#         else:
#             break
#     return counter

# class Test_check_repetition_char(unittest.TestCase):
#     def test_check_repetition_char(self):
#         text = 'color'
#         starting_pos = 4
#         final_letter = 'r'
#         count = count_char_matches(text,starting_pos,final_letter)
#         self.assertEqual(0, count)

class TestStage(unittest.TestCase):

    def test_case1(self):
        code = 'colou?r|color'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case2(self):
        code = 'colou?r|colour'
        exp = Regexp(code)
        self.assertTrue(exp.result)

    def test_case3(self):
        code = 'colou?r|colouur'
        exp = Regexp(code)
        self.assertFalse(exp.result)
    
    def test_case4(self):
        code = 'colou*r|color'
        exp = Regexp(code)
        self.assertTrue(exp.result)

    def test_case5(self):
        code = 'colou*r|colour'
        exp = Regexp(code)
        self.assertTrue(exp.result)

    def test_case6(self): 
        code = 'colou*r|colouur'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case7(self):
        code = 'col.*r|color'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case8(self):
        code = 'col.*r|colour'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case9(self):
        code = 'col.*r|colr'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case10(self):
        code = 'col.*r|collar'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case11(self):
        code = 'col.*r$|colors'
        exp = Regexp(code)
        self.assertFalse(exp.result)
    
    def test_case13(self):
        code = 'colou+r|color'
        exp = Regexp(code)
        self.assertFalse(exp.result)

    def test_case12(self):
        code = 'a|a'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case14(self):
        code = '.*|aaa'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case15(self):
        code = '.+|aaa'
        exp = Regexp(code)
        self.assertTrue(exp.result)

    def test_case16(self):
        code = '.?|aaa'
        exp = Regexp(code)
        self.assertTrue(exp.result)
    
    def test_case17(self):
        code = 'no+$|noooooooope'
        exp = Regexp(code)
        self.assertFalse(exp.result)


if __name__ == "__main__": # This enables us to run it directly using python filename.py
    unittest.main()