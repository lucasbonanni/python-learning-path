# this code is in the beginning of the test_calculator.py file
# Run the unit test using python -m unittest test_calculator
# python -m unittest If we do not specify the name of the test file, only files which start with the "test" will be executed.
from stage4 import Regexp
import unittest


class testStage(unittest.TestCase):

    def case1(self):
        code = '^app|apple'
        print(code)
        self.assertEqual(Regexp(code),'True')


if __name__ == "__main__": # This enables us to run it directly using python filename.py
    unittest.main()