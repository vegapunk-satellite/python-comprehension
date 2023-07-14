# Scope
#'LEGB' stands for Local, Enclosing, Global, Built-in --the reason that abbreviation is in this order, is because this is the order that determines what a variable is assigned to--


x = "global x"


def test():
    global x
    x = "local x"
    # print(y)
    print(x)


test()
print(x)


def test(z):
    x = "local x"
    print(z)


test("local z")
# print(z)                 #*'z' variable is only local to the test function*
# -------------------------------------------------------------------------------------
# built-in scope
import builtins


print(dir(builtins))  # ** view the variables that are within the built-in scope**


def my_min():  # If a user function has the same name with a built-in python will raise a TypeError
    pass


m = min([5, 1, 4, 2, 3])
print(m)


# -------------------------------------------------------------------------------------
# Enclosing
def outer():
    x = "outer x"

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)


outer()


# -------------------------------------------------------------------------------------
def outer():
    x = "outer x"

    def inner():
        nonlocal x  # Over-writes the x value in which was set in inner function to the local value of the outer function
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()
# nonlocal statement is useful in order to change the state of closures and decorators, will most likely be used more than the global statement
