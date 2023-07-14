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
    if y == 0:
        raise ValueError("Can not divide a number by zero!")
    return x / y
