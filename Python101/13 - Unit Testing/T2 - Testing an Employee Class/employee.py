# The module contains a sample 'Employee' class;
# that lets users access specific information about a company's employees.
# Created for testing purposes only.


import requests


class Employee:
    """A sample employee class"""

    # Percentage of the raise to an employee's salary:
    raise_amt = 1.05  # By default set to %5.

    # Creating three instances to set employee's first name, last name, and salary informations:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(
        self,
    ):  # Method that generates employee's e-mail address with created instances.
        return "{}.{}@email.com".format(self.first.lower(), self.last.lower())

    @property
    def fullname(
        self,
    ):  # Method that generates employee's full name with created instances.
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):  # Method that applies raise to the employee salary.
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(
        self, month
    ):  # Method that pretends to check an employee's schedule from the company's website.
        response = requests.get(f"http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
