# Built-in Functionalities:
# Absolute Value:
# Basicly removes the ' - ' sign for negative numbers.
print(abs(-10))

# Round Function:
# By default, will round the float values into the nearest integer value.
print(round(5.56))

# Users can also pass in a second argument into the round function;
# which tells the function how many digits to round to.
print(round(3.53286575, 2))


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
# To change these values from strings to integers, users can simply wrap these values into the 'int()' function.
num_3 = int(num_3)
num_4 = int(num_4)
print(num_3 + num_4)
