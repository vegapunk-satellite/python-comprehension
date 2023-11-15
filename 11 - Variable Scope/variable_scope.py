# Variable scope determines where to access the variables within the program;
# and what values those variables hold in different contexts.
# Understanding the variable scope really helps with debugging; when a variable doesn't have the value users expected.


# 'LEGB' is a common abbreviation that stands for; 'Local, Enclosing, Global, Built-in'.
# Order of this abbreviation determines what a variable is assigned to.


# Global and local scopes:
x = "global x"  # Contained in the main body of our script hence a 'global' variable.


def test():
    y = "local y"  # Contained inside a function hence a 'local' variable of that specific function.
    print(y)
    print(x)  # Global variables can be used within the local functions.


# print(y)  # Will result in a 'NameError', cannot use a local variable globally.
test()


# Setting a global value within a local function: (not so convenient)
# Using the 'global' command lets users alter the variable globally, even if that variable doesn't exist within the code.
def test_2():
    global x
    x = "local x"
    print(x)


test_2()
print(x)


# Understanding the scope while working with function arguments:
def test_3(
    z,
):  # Argument 'z' is a local variable that is contained within the test function.
    x = "local x"
    print(z)


# print(z)    # Returns a 'NameError' because, 'z' variable is only local to the test_3 function.
test_3(
    "local z"
)  # In the current example the user string becomes the local variable 'z'.


# Built-in scope:
import builtins


m = min(
    [5, 1, 4, 2, 3]
)  # 'min' is one of the built-in functions that reside within python.
print(m)


print(dir(builtins))  # Returns all the variables within the built-in scope.


# Users will be prompted with a 'TypeError' in cases where their function has the same name with a built-in python function.
# def min():    # Bad practice. Python will find built-in min function in the global scope, user function name should be different.
# pass


def my_min():  # Correct usage.
    pass


# Enclosing(nonlocal) scope;
# is a special scope that only exists within nested functions.
# Grasping the meaning of both local and global scopes is crucial for understanding the enclosing scope.
def outer():  # Outer(enclosing) function.
    x = "outer x"

    def inner():  # Inner function.
        # x = 'inner x'   # After closing this line, the program looks for a local scope of any enclosing functions.
        print(x)

    inner()
    print(x)


outer()


# Previously we globalised a local value, same logic can be applied with enclosing;
# with the usage of 'nonlocal' command.
# Nonlocal statement tends to be useful in cases where;
# users desire to change the state of closures and decorators.
# Will most likely be used more than the global statement...
def outer():
    x = "outer x"

    def inner():
        nonlocal x  # Overwrites the 'x' value; which was set in the inner function, to the local value of the outer function.
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()
