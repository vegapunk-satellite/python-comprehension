import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Edward', 'Newgate', 5046000000)
        emp_2 = Employee('Ben', 'Beckman', 3500000000)

        self.assertEqual(emp_1.email, 'Edward.Newgate@email.com')
        self.assertEqual(emp_2.email, 'Ben.Beckman@email.com')

        emp_1.first = 'Marshall'
        emp_2.first = 'Roux'

        self.assertEqual(emp_1.email, 'Marshall.Newgate@email.com')
        self.assertEqual(emp_2.email, 'Roux.Beckman@email.com')

    def test_fullname(self):
        emp_1 = Employee('Edward', 'Newgate', 5046000000)
        emp_2 = Employee('Ben', 'Beckman', 3500000000)

        self.assertEqual(emp_1.fullname, 'Edward Newgate')
        self.assertEqual(emp_2.fullname, 'Ben Beckman')

        emp_1.first = 'Marshall'
        emp_2.first = 'Roux'

        self.assertEqual(emp_1.fullname, 'Marshall Newgate')
        self.assertEqual(emp_2.fullname, 'Roux Beckman')

    def test_apply_raise(self):
        emp_1 = Employee('Edward', 'Newgate', 5046000000)
        emp_2 = Employee('Ben', 'Beckman', 3500000000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 5298300000)
        self.assertEqual(emp_2.pay, 3675000000)

if __name__ == '__main__':
    unittest.main()
#-------------------------------------------------------------------------------------
##If we had hundreds of tests in our code unlike our example above
##We would need to put those names in time and time again and the process will be tedious
##We need to keep our code DRY(don't repeat yourself)
##Hence the usage of 'setUp' and 'tearDown' methods
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    ##'setUp' method will run its code before every single test
    def setUp(self):
        print('setUp')
        ##in order to access these from our other test, we need to set them as instance attributes by putting 'self.' prior
        self.emp_1 = Employee('Edward', 'Newgate', 5046000000)
        self.emp_2 = Employee('Ben', 'Beckman', 3500000000)
        ##Now that we have this function we can go ahead and delete the creation of these employees from the beginning of every test

    ##'tearDown' method will run its code after every single test
    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Edward.Newgate@email.com')
        self.assertEqual(self.emp_2.email, 'Ben.Beckman@email.com')

        self.emp_1.first = 'Marshall'
        self.emp_2.first = 'Roux'

        self.assertEqual(self.emp_1.email, 'Marshall.Newgate@email.com')
        self.assertEqual(self.emp_2.email, 'Roux.Beckman@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Edward Newgate')
        self.assertEqual(self.emp_2.fullname, 'Ben Beckman')

        self.emp_1.first = 'Marshall'
        self.emp_2.first = 'Roux'

        self.assertEqual(self.emp_1.fullname, 'Marshall Newgate')
        self.assertEqual(self.emp_2.fullname, 'Roux Beckman')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5298300000)
        self.assertEqual(self.emp_2.pay, 3675000000)

if __name__ == '__main__':
    unittest.main()
#-------------------------------------------------------------------------------------
##Tests don't necessarily run in order, hence the reason to keep all of them isolated
##Sometimes it's also useful to have some code that runs at the very beginning of the test file; and then have some cleanup code that runs after all the tests have been run.
##So unlike the 'setUp' and 'tearDown' that run before and after every single test, it would be nice to have some code that ran once before anything and once after everything.
##This can be achieved with two class methods called 'setUpClass' and 'tearDownClass'
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    ##These two class methods below basically mean that we're working with the class, rather than the instance of the class
    ##like in the previous example with 'self'
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
    ##'setUpClass' and 'tearDownClass' can be useful if we just want to do something once and it's too costly to do before each test
    ##for example if we want to populate a database to run tests against


    ##'setUp' method will run its code before every single test
    def setUp(self):
        print('setUp')
        ##in order to access these from our other test, we need to set them as instance attributes by putting 'self.' prior
        self.emp_1 = Employee('Edward', 'Newgate', 5046000000)
        self.emp_2 = Employee('Ben', 'Beckman', 3500000000)
        ##Now that we have this function we can go ahead and delete the creation of these employees from the beginning of every test

    ##'tearDown' method will run its code after every single test
    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Edward.Newgate@email.com')
        self.assertEqual(self.emp_2.email, 'Ben.Beckman@email.com')

        self.emp_1.first = 'Marshall'
        self.emp_2.first = 'Roux'

        self.assertEqual(self.emp_1.email, 'Marshall.Newgate@email.com')
        self.assertEqual(self.emp_2.email, 'Roux.Beckman@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Edward Newgate')
        self.assertEqual(self.emp_2.fullname, 'Ben Beckman')

        self.emp_1.first = 'Marshall'
        self.emp_2.first = 'Roux'

        self.assertEqual(self.emp_1.fullname, 'Marshall Newgate')
        self.assertEqual(self.emp_2.fullname, 'Roux Beckman')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5298300000)
        self.assertEqual(self.emp_2.pay, 3675000000)

if __name__ == '__main__':
    unittest.main()
#-------------------------------------------------------------------------------------
##Basic usage of mocking
##If our function relies on some information that given by a website, and in cases where the website cannot be reached;
##we can use mocking to get around this problem, we only want our test to fail if there is something wrong with our code
import unittest
##we can use patch either as a decorator, or a context manager;
##it will allow us to mock the object during a test, and than that object is automatically restored after the test is run
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    ##These two class methods below basically mean that we're working with the class, rather than the instance of the class
    ##like in the previous example with 'self'
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
    ##'setUpClass' and 'tearDownClass' can be useful if we just want to do something once and it's too costly to do before each test
    ##for example if we want to populate a database to run tests against


    ##'setUp' method will run its code before every single test
    def setUp(self):
        print('setUp')
        ##in order to access these from our other test, we need to set them as instance attributes by putting 'self.' prior
        self.emp_1 = Employee('Edward', 'Newgate', 5046000000)
        self.emp_2 = Employee('Ben', 'Beckman', 3500000000)
        ##Now that we have this function we can go ahead and delete the creation of these employees from the beginning of every test

    ##'tearDown' method will run its code after every single test
    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Edward.Newgate@email.com')
        self.assertEqual(self.emp_2.email, 'Ben.Beckman@email.com')

        self.emp_1.first = 'Marshall'
        self.emp_2.first = 'Roux'

        self.assertEqual(self.emp_1.email, 'Marshall.Newgate@email.com')
        self.assertEqual(self.emp_2.email, 'Roux.Beckman@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Edward Newgate')
        self.assertEqual(self.emp_2.fullname, 'Ben Beckman')

        self.emp_1.first = 'Marshall'
        self.emp_2.first = 'Roux'

        self.assertEqual(self.emp_1.fullname, 'Marshall Newgate')
        self.assertEqual(self.emp_2.fullname, 'Roux Beckman')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5298300000)
        self.assertEqual(self.emp_2.pay, 3675000000)

    def test_monthly_schedule(self):
        ##In this example we will use the 'patch' as a context manager
        ##within patch we pass in the data that we want to mock
        ##we want to mock 'request.get' of the 'employee' module
        ##and then we are setting that equal to 'mocked_get'
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Newgate/May')
            self.assertEqual(schedule, 'Success')

            ##Finally we want to test a failed response
            mocked_get.return_value.ok = False
            ##we don't need a text value, because our function already returns 'Bad Response!'

            schedule = self.emp_2.monthly_schedule('July')
            mocked_get.assert_called_with('http://company.com/Beckman/July')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()

##Our tests shouldn't rely on, or affect other tests. We should be able to run any test independently
##In the examples above; we were adding tests to an existing code,
##'Test Driven Development' means writing tests before writing our code, and in some cases can be really useful
##So basically the concept is; we should think about what we want our code to do, and than write a test implementing that behaviour
##Than watch the test fail since it doesn't actually have any code to run against, and then to write the code in a way that gets the test to pass
