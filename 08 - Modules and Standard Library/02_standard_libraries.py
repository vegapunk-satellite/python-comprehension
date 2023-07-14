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
