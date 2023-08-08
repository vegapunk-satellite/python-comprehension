# Unit Testing:
# Because of the naming convention, the method that users define when testing needs to start with 'test_', or else won't work.


import unittest  # Importing a testing module within the Standard Library.
import calc  # Importing the previously created 'calc.py' script for testing purposes.


# Users need to create test cases for the functions that they desire to test.
# In order to create those test cases, users first need to create a test class that inherits from 'unittest.TestCase'.
# Prompts '.' for successful, 'F' for failed tests.
class TestCalc(unittest.TestCase):
    def test_add(self):  # Testing our custom addition function.
        result = calc.add(10, 5)
        self.assertEqual(
            result, 15
        )  # Python's documentation contains all the assertions users need while testing.


# Running the test:
if __name__ == "__main__":
    unittest.main()


# Adding in multiple tests:
# User goal should be to enhance the test quality, not the quantity...
import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(
            calc.add(10, 5), 15
        )  # Instead of setting a 'result' variable and testing that, users can drop the function directly to the assert statement.
        self.assertEqual(
            calc.add(-1, 1), 0
        )  # Better to check some edge cases when testing. Like a negative number and a positive number.
        self.assertEqual(
            calc.add(-1, -1), -2
        )  # Having two negative numbers also counts as an edge case, so better check that as well.

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(
            calc.divide(5, 2), 2.5
        )  # Dividing an odd number can be counted as an edge case as well.

        # Test of dividing a number by '0':
        self.assertRaises(
            ValueError, calc.divide, 10, 0
        )  # No arguments being passed into the function, hence no parenthesis.

        # Instead of passing in all of the arguments separately;
        # users can call the function normally via using the context manager.
        with self.assertRaises(ValueError):  # Within the context manager;
            calc.divide(
                10, 0
            )  # Users can call the desired function normally when testing.


if __name__ == "__main__":
    unittest.main()
