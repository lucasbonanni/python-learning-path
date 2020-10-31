# this code is in the beginning of the test_calculator.py file
# Run the unit test using python -m unittest test_calculator
# python -m unittest If we do not specify the name of the test file, only files which start with the "test" will be executed.
import unittest
import calculator

class TestCalculator(unittest.TestCase):  # a test case for the calculator.py module

    def test_add(self):
        # tests for the add() function
        self.assertEqual(calculator.add(6, 4), 10)
        self.assertEqual(calculator.add(6, -4), 2)
        self.assertEqual(calculator.add(-6, 4), -2)
        self.assertEqual(calculator.add(-6, -4), -10)

    def test_add_error(self):
        # tests for the add() function        
        self.assertEqual(calculator.add(6, 4), 10, 'Error when adding two positive numbers')

    def test_divide(self):
        # tests for the divide() function
        # ...
        self.assertRaises(ValueError, calculator.divide, 5, 0)

if __name__ == "__main__": # This enables us to run it directly using python filename.py
    unittest.main()