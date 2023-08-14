# Most Common Python Mistakes:


# Mixing tabs and spaces or being inconsistent when using them leads to an 'IndentationError'.
# 'Tabs to spaces' should always be set to 'True' within the user's text editor settings;
# 'tabs to spaces' option helps a great deal when the code gets long and complex.
nums = [11, 30, 44, 54]


for num in nums:
    square = num**2  # 1 tab
    print(square)  # 4 spaces


# Having bad module names:
# Naming the user modules same with the libraries that we try to import leads to an 'ImportError'.
# Assume user module was named 'math.py':
from math import radians, sin


rads = radians(90)  # Will return an 'ImportError';
print(
    sin(rads)
)  # Because python is trying to import radians and sine from the user module, instead of the Standard Library 'math' module.


# A simple renaming process will solve this issue, hence the need to name our modules properly.
# If renaming won't solve the problem, it could be an issue concerning the user 'path'.


# Having bad variable names:
from math import radians, sin


radians = radians(90)
print(sin(radians))  # Seems like working but actually it is not.
# Anytime users reference 'radians' after the variable assignment, it will use the variable and not the function.
# rad45 = radians(45)
# print(rad45)  # Returns a TypeError.


# Mutable Default Arguments:
def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)


emps = ["Bentham", "Galdino"]
add_employee("Daz")
add_employee("Robin")  # Will keep appending into the same list.
# Users might expect the output would be different but in reality;
# the code above only executes those default arguments once when the function is declared, not each time the function is run.


# Averting this issue with a statement:
def add_employee(emp, emp_list=None):
    if emp_list is None:  # If the list does not exist, create one.
        emp_list = []
    emp_list.append(emp)  # In case a list already exists, add the value to that list.
    print(emp_list)


# Now that the statement is inside the function, this will run everytime the function is executed.
add_employee("Daz")
add_employee(
    "Robin"
)  # Will print out a single employee each time it's executed, or gets tagged on to the specific list stated as an argument.


import time
from datetime import datetime


def display_time(time=datetime.now()):
    print(time.strftime("%B %d, %Y %H:%M:%S"))


display_time()
time.sleep(1)  # Sleeping a second between each function call.
display_time()
time.sleep(1)
display_time()  # Returns the exact same moment three times in a row even though user commanded to slept twice in between function calls.


# In order to solve the issue users would need to move the time into the function itself.
import time
from datetime import datetime


def display_time(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime("%B %d, %Y %H:%M:%S"))


display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
# Will sleep one second in between function calls but, and has the current time since user didn't provided one as an argument.


# How iterators get exhausted:
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]


identities = zip(names, heroes)
print(
    identities
)  # Unlike Python 2, instead of an entire list of zipped items, Python 3 returns the zip object's location on the memory.


print(list(identities))  # Converting the zip object into a list.


for identity in identities:  # Looping over that same exhausted zip object again.
    print("{} is actually {}!".format(identity[0], identity[1]))


# Solved one problem, printed the list but now the loop disappeared...
# Reason was quite simple, user is converting the zip object into a list;
# and then trying to loop over that zip object again, but 'zip' was already exhausted upon being converted into a list.


# Converting the object into a list from the beginning does not exhaust the generator, hence the for loop will be operational.
identities = list(zip(names, heroes))
print(identities)


for identity in identities:
    print("{} is actually {}!".format(identity[0], identity[1]))


# Having bad practices while importing modules:
import os


# os.rename(file)  # gets tedious every single time to type in 'os.', so for the sake of shortening our code:
from os import rename, remove


# rename(filename)
# remove(filename)


# In cases where many functions will be used; an alternative would be the '*' sign, that imports all functions that specific module has.


from os import *


# rename(filename)
# remove(filename)


# Using '*' to import is considered to be a bad practice;
# Because users may have hard time finding out where that specific function was declared in cases where they have longer and more complex code.
# or multiple different libraries might have the same function name; hence the confusion:
from html import *
from glob import *


# Both of these libraries have an 'escape' method;
# but each of those methods have completely different functionalities.


# It's always better to import explicitly leads to a better readable code, and easier to debug if anything goes wrong.
# More appropriate way to import the functions that have the same names:
from html import escape as h_escape
from glob import escape as g_escape
