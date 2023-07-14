# Unit Testing:
# Assume that we created a script named 'calc.py' and in that script there are four custom arithmetic operators defined.
# We'll test those custom functions that we created by importing our 'calc.py' here as a module

# A testing module inside the Standard Library
# import unittest
# The custom module we which desire to test
# import calc


# Now we need to create test cases for the functions that we want to test
# In order to create those test cases we first need to create a test class that inherits from 'unittest.TestCase'
# class TestCalc(unittest.TestCase):
#     Because of the naming convention method that we define here needs to start with 'test_', or else won't work
#     testing our custom addition function
#     we can see all the assertions in Python's documentation which we can use while testing
#     def test_add(self):
#         result = calc.add(10, 5)
#         self.assertEqual(result, 15)

# if __name__ == '__main__':
#     unittest.main()
# -------------------------------------------------------------------------------------
# Let's add in a few more tests
# instead of setting a 'result' variable and testing that, we can drop our function directly to the assert statement
import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        ##we usually want to check some edge cases when testing
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        ##Our goal is to enhance the test quality, not quantity

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
        self.assertEqual(calc.divide(5, 2), 2.5)
        # test of dividing a number by zero
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # easier approach via using the context manager:
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
