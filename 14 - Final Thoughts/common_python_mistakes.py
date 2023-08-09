# Most Common Python Mistakes:

# Mixing tabs and spaces or being inconsistent when using both(leads to indentation error):
# Tabs to spaces should always be set to 'True' within the editor settings;
# helps in great deal when the code gets long and complex.
nums = [11, 30, 44, 54]


for num in nums:
    square = num**2  # 1 tab
    print(square)  # 4 spaces


# Bad module names:
# Naming our modules same with the libraries that we try to import.
# Assume user named this module 'math.py':
from math import radians, sin


rads = radians(90)  # Will return an 'ImportError';
print(
    sin(rads)
)  # because python is trying to import radians and sine from the user module, instead of Standard Library.

# A simple renaming process will solve this issue, hence the need to name our modules more appropriate.
# If not it could be an issue concerning the user 'path'...


# Bad variable names:
from math import radians, sin


radians = radians(90)
print(sin(radians))  # Seems like it's working but actually it is not.


# rad45 = radians(45)
# print(rad45)  # Returns a TypeError. Anytime users reference radians after the variable assignment, it will use the variable and not the function.


# Mutable Default Arguments:
def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)


emps = ["Bentham", "Galdino"]
add_employee("Daz")
add_employee("Robin")


# will keep appending into the same list, and be longer
# averting this issue with a statement:
def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)


# Now that the statement is inside the function, this will run everytime the function is executed
add_employee("Daz")
add_employee("Robin")
# will print out a single employee each time it's executed, or gets tagged on to the specific list stated as an argument


import time
from datetime import datetime


def display_time(time=datetime.now()):
    print(time.strftime("%B %d, %Y %H:%M:%S"))


display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
# Returns the exact same moment three times in a row even though we slept twice.
# Users might expect the output would be different but in reality;
# our code above only executes those default arguments once when the function is declared, not each time the function is run.


# In order to solve this we would need to move this into the function itself
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
# Will sleep one second inbetween function calls but, it actually got the current time since we didn't provided one


# How iterators get exhausted:


names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]


# identities = zip(names, heroes)
# print(identities)


# Instead of an entire list of zipped items, returns zip object's location on the memory
# Tends to be more efficient for the CPU when imagining a list that has thousands of items
# print(list(identities))


# Solved one problem printed the list but now our loop below disappeared
# Reason was quite simple, we are converting our zip object into a list;
# and then trying to loop over that zip object again but it's already exhausted upon being converted to a list
# if we want both functions to operate; we need to convert it into a list from the beginning
# this way the generator is not exhausted so both functions are operational
identities = list(zip(names, heroes))
print(identities)


for identity in identities:
    print("{} is actually {}!".format(identity[0], identity[1]))


# Bad practices while importing modules
import os


# os.rename(file)


# gets tedious every single time to type in 'os.' so;
# for the sake of shortening our code
from os import rename, remove


# rename(filename)
# remove(filename)


# in cases where many functions will be used an alternative would be the '*' sign;
# which imports all functions that specific module has
from os import *


# rename(filename)
# remove(filename)
# using '*' to import is considered to be a bad practice;
# we may have hard time finding out where that specific function was declared
# in cases where we have longer and more complex code


# or multiple different libraries might have the same function name; hence the confusion
from html import *
from glob import *


# both of these libraries have an 'escape' method
# but each of these methods have a complete different functionality


# it's always better to import explicitly leads to a better readable code;
# and easier to debug if anything goes wrong
# a wiser way to import the functions that have the same names:
from html import escape as h_escape
from glob import escape as g_escape
