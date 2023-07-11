# Introduction
# Slicing is a way of extracting certain elements from lists and strings
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# +indexes: 0  1  2  3  4  5  6  7  8  9
# -indexes:-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(my_list[0])
# print(my_list[-10])
print(my_list[9])
# print(my_list[-1])

# Extracting a range of numbers from a list:
# list[start:end:step]
# The syntax above let's users to extract a range of numbers from that list.
print(
    my_list[0:6]
)  # Prints up until '5', second parameter is not inclusive like the first.

# Going from '3' up until '7':
print(my_list[3:8])
print(my_list[-7:-2])
# We can mix and match these positive and negative indexes
# Going from '1' up until '8':
print(my_list[1:-1])

# 'Step' allows users to skip a certain number of values.
# The default step value is '1', plus users can reverse-step passing in negative values.
# Going from '2' up until '8', taking only even numbers:
print(my_list[2:-1:2])
# Going from '9' up until '3', taking only odd numbers:
print(my_list[-1:2:-2])
# Printing entire list backwards:
print(my_list[::-1])

# Slicing strings:
# Users can apply the same logic for strings as well:
sample_url = "https://inventwithpython.com"

# Reversing the url:
print(sample_url[::-1])
# Get on the top level domain(.com):
print(sample_url[-4:])
# Removing the 'http://':
print(sample_url[7:])
# Removing both 'http://' and top level domain:
print(sample_url[7:-4])
