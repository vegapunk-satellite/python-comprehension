# Standard Library is incredibly useful when performing a common task; which most likely someone has already written.
# These scripts have been optimised to be as performant as possible, and have been written by professional coders.
# Allows users import directly within Standard Libraries; without installing anything separately.


# Random Module:
# Grabbing a random value; within a list of values:
import random


courses = ["History", "Math", "Physics", "CompSci"]


random_course = random.choice(
    courses
)  # Whenever users pass in the given list as an argument inside the '.choice()' method, and set that value as a new variable.


print(
    random_course
)  # Prints out a random item from the user list each time it's executed.


# Math Module:
# In cases where users need to perform common mathematical operations:
# Let us try out the 'math' module with some trigonometric functions.
import math


rads = math.radians(90)  # Converting 90 degrees into radians.


print(rads)
print(math.sin(rads))  # Returns the sine of 90 degrees.


# Datetime Module allows users to work with days and times.
import datetime
import calendar


today = datetime.date.today()  # Returns the current date.
print(today)


print(
    calendar.isleap(2020)
)  # Returns 'True' if the argument is indeed a leap year, returns 'False' if not.


# OS Module:
# Tends to be useful in cases where users need to access the underlying operating system.
# OS Module has tons of functionality like; scanning the filesystem, creating files, deleting files...
import os


print(
    os.getcwd()
)  # Returns the current working directory; where the script is located.


# Discovering through the files and scripts of the Standard Library will be beneficial for the users:
# Since all these useful methods and their contents can be found within.
print(os.__file__)  # Returns the Standard Library directory.


# A standard library which leads the browser to open a webcomic.
import antigravity
