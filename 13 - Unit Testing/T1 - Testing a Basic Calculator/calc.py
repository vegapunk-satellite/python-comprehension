# The module contains the four basic arithmetic operations. ('+', '-', '*', '/')
# Created for testing purposes only.


def add(x, y):
    # Addition
    return x + y


def subtract(x, y):
    # Subtraction
    return x - y


def multiply(x, y):
    # Multiplication
    return x * y


def divide(x, y):
    # Division
    if y == 0:  # In cases where the user tries to divide a number by '0';
        raise ValueError("Can not divide a number by zero!")  # raise a 'ValueError'.
    return x / y
