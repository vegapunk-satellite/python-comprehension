# Now we can use the 'find_index' function with the 'import' command.
import test_module


courses = ["History", "Math", "Physics", "CompSci"]

index = test_module.find_index(courses, "Math")
print(index)


# If the module's name tends to be tedious we can use 'as'
import test_module as TM


courses = ["History", "Math", "Physics", "CompSci"]

index = TM.find_index(courses, "Math")
print(index)


# Using the "'from' *module 'import' *function" format is another way
from test_module import (
    find_index,
    test_string,
)  # 'as' can be used to shorten functions just like modules

# from CompSci import *                      # Using '*' imports every function from that module. But this method is frowned upon because python can't tell which function will be imported from that specific module.


courses = ["History", "Math", "Physics", "CompSci"]
index = find_index(courses, "Math")
print(index)


# If the desired module is in the same directory with our current file. We can simply import it.
from test_module import find_index, test_string
import sys

courses = ["History", "Math", "Physics", "CompSci"]

index = find_index(courses, "Math")
# print(index)
# print(test_string)

print(sys.path)  # Allows users to see the directories


# If not in same directory, we can append the location of the desired module to our python path
import sys

sys.path.append("-------Directory_Address-------")


# Standard Libraries
import random

courses = ["History", "Math", "Physics", "CompSci"]

random_course = random.choice(courses)

print(random_course)


import math

courses = ["History", "Math", "Physics", "CompSci"]

rads = math.radians(90)

print(rads)
print(math.sin(rads))  # 'sin' --Sine is one of the trigonometric functions--


import datetime
import calendar

courses = ["History", "Math", "Physics", "CompSci"]

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))


import os

courses = ["History", "Math", "Physics", "CompSci"]

print(
    os.getcwd()
)  #'getcwd' function prints out the current working directory where the script is located
print(
    os.__file__
)  # '__file__' function prints out the Standard Library file's location in the directory


# A standard library which leads the browser to open a webcomic.
import antigravity
