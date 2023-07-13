# Boolean values are one of the data types, these values will either return true or false.
# We'll be taking a closer look at them on the 'conditionals' scipts up ahead.
"""
Comparisons:  (always returns Boolean)
Equal:                ==
Not Equal:            !=
Greater Than:         >
Less Than:            <
Greater or Equal:     >=
Less or Equal:        <=
"""

num_1 = 56
num_2 = 29

print(num_1 == num_2)  # Will compare if the two numbers are equal.
print(num_1 != num_2)  # Will compare if the two numbers are not equal.
print(num_1 > num_2)  # Will compare if the first number is greater than second.
print(
    num_1 <= num_2
)  # Will compare if the first number is smaller or equal to the second.

# If user input was explicitly set to strings:
num_3 = "56"
num_4 = "29"

print(
    num_3 + num_4
)  # Won't be working as expected. Will end up concatenating strings...
# Solution would be:
# Data type should be converted into an integer first.
# To cast these values from strings to integers, users can simply wrap these values into the 'int()' function.
num_3 = int(num_3)
num_4 = int(num_4)
print(num_3 + num_4)
