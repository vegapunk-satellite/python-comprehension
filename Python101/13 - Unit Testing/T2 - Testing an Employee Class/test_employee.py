# Tests shouldn't rely on, or affect other tests. Users should be able to run any test independently...


import unittest  # Importing a testing module within the Standard Library.
from employee import (
    Employee,
)  # Importing the previously created 'Employee' class within the 'employee.py' module for testing purposes.


# Creating the test case that inherits from 'unit.TestCase':
class TestEmployee(unittest.TestCase):
    # Within the class there are three different tests.

    # Testing e-mail generating module:
    def test_email(self):
        # Creating two employees, passing in data for the required instances(name, surname, salary):
        emp_1 = Employee("Edward", "Newgate", 5046000000)
        emp_2 = Employee("Ben", "Beckman", 3500000000)

        # Testing whether if the previously created instances transform to the proper e-mail format:
        self.assertEqual(emp_1.email, "edward.newgate@email.com")
        self.assertEqual(emp_2.email, "ben.beckman@email.com")

        # Changing the first name instances to see whether if the code will respond accordingly or not:
        emp_1.first = "Marshall"
        emp_2.first = "Roux"
        self.assertEqual(emp_1.email, "marshall.newgate@email.com")
        self.assertEqual(emp_2.email, "roux.beckman@email.com")

    # Testing the full name generating module with an approach similar to the previous one
    def test_fullname(self):
        # Creating employees:
        emp_1 = Employee("Edward", "Newgate", 5046000000)
        emp_2 = Employee("Ben", "Beckman", 3500000000)

        # Testing the full name generator:
        self.assertEqual(emp_1.fullname, "Edward Newgate")
        self.assertEqual(emp_2.fullname, "Ben Beckman")

        # Tweaking the first name instances to test the function response:
        emp_1.first = "Marshall"
        emp_2.first = "Roux"
        self.assertEqual(emp_1.fullname, "Marshall Newgate")
        self.assertEqual(emp_2.fullname, "Roux Beckman")

    # Test to make sure that the salary was raised by %5:
    def test_apply_raise(self):
        # Creating employees:
        emp_1 = Employee("Edward", "Newgate", 5046000000)
        emp_2 = Employee("Ben", "Beckman", 3500000000)

        # Applying the raise:
        emp_1.apply_raise()
        emp_2.apply_raise()

        # Checking if the applied raises were correct or not:
        self.assertEqual(emp_1.pay, 5298300000)
        self.assertEqual(emp_2.pay, 3675000000)


if __name__ == "__main__":
    unittest.main()


# In cases where users have hundreds of tests within the script; changing an instance manually would be tedious.
# So having the functionality to prevent repetition is a must. Instances could be set individually for different tests in one fell swoop.
# With the usage of 'setUp' and 'tearDown' methods:
# Both these methods are 'camel cased', meaning typing uppercase 'U' and 'D' is essential.
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    # 'setUp' method will run its code before every single test.
    # Instead of creating new employee information every single time, try passing those into the 'setUp' method.
    # In order to access values from other tests, users need to set them as instance attributes by putting 'self.' prior to those values.
    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Edward", "Newgate", 5046000000)
        self.emp_2 = Employee("Ben", "Beckman", 3500000000)
        # Users don't need to create employees in the beginning of each and every test from this point on.

    # 'tearDown' method will run its code after every single test.
    def tearDown(self):
        print(
            "tearDown\n"
        )  # Since the current module has nothing to tear down, it is used for displaying the separation.

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Edward Newgate")
        self.assertEqual(self.emp_2.fullname, "Ben Beckman")

        self.emp_1.first = "Marshall"
        self.emp_2.first = "Roux"

        self.assertEqual(self.emp_1.fullname, "Marshall Newgate")
        self.assertEqual(self.emp_2.fullname, "Roux Beckman")


# Tests don't necessarily run in a specific order, so the users should keep them isolated.
if __name__ == "__main__":
    unittest.main()


# Some cases require to have some code that runs at the very beginning of each test file; and then have some cleanup code that runs after all the tests have been run.
# So unlike the 'setUp' and 'tearDown' methods that run separately before or after every single test;
# it would be nice to have some code that ran once before anything and once after everything.
# Two class methods called; 'setUpClass' and 'tearDownClass' have the aforementioned functionality:
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    # These two class methods below basically mean that users are working with the class itself;
    # rather than an instance of the class, like the previous examples that begin with 'self.'.
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # 'setUpClass' and 'tearDownClass' can be useful in cases where the action before each test is too costly.
    # A real life example would be populating a database, to run tests against.
    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Edward", "Newgate", 5046000000)
        self.emp_2 = Employee("Ben", "Beckman", 3500000000)

    def tearDown(self):
        print("tearDown\n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "edward.newgate@email.com")
        self.assertEqual(self.emp_2.email, "ben.beckman@email.com")

        self.emp_1.first = "Marshall"
        self.emp_2.first = "Roux"

        self.assertEqual(self.emp_1.email, "marshall.newgate@email.com")
        self.assertEqual(self.emp_2.email, "roux.beckman@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Edward Newgate")
        self.assertEqual(self.emp_2.fullname, "Ben Beckman")

        self.emp_1.first = "Marshall"
        self.emp_2.first = "Roux"

        self.assertEqual(self.emp_1.fullname, "Marshall Newgate")
        self.assertEqual(self.emp_2.fullname, "Roux Beckman")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5298300000)
        self.assertEqual(self.emp_2.pay, 3675000000)


if __name__ == "__main__":
    unittest.main()


# Basic usage of mocking:
# In cases where the function relies on the information given by a website, and that website is cannot be reached:
# Using the patch either as a decorator, or a context manager allows users to mock the object during a test;
# and then restoring that object automatically after the test is run.


import unittest


from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Edward", "Newgate", 5046000000)
        self.emp_2 = Employee("Ben", "Beckman", 3500000000)

    def tearDown(self):
        print("tearDown\n")

    # In the example 'patch' has been used as a context manager;
    # users need to pass in the data to be mocked within the patch.
    def test_monthly_schedule(self):
        # Mocking 'request.get' of the 'employee' module;
        # and then setting that equal to 'mocked_get':
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            # Testing a successful response:
            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Newgate/May")
            self.assertEqual(schedule, "Success")

            # Testing a failed response:
            mocked_get.return_value.ok = False
            # Won't be placing a text value, because the function already returns 'Bad Response!'.
            schedule = self.emp_2.monthly_schedule("July")
            mocked_get.assert_called_with("http://company.com/Beckman/July")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
