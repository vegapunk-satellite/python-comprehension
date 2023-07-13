# Introduction:
# Python allows users to work with various data types, to serve their specific purposes.
# Strings('str') are one of those data types, pretty useful in cases where we need to work with textual data.


#'print' is a built in python function, which allows users to prompt their desired message to the terminal within the usage of proper syntax ofcourse.
# The message can be a string, or any other object.
# If it's an object, then it will be converted into a string before written to the screen.
# We are passing in a text value into the print function in this case specificly 'Hello friend!'.
# As seen in the examples below; using apostrophes or quotation marks are optional. But either way users should be consistent.
print("Hello friend!")
print("Hello friend!")

"""
Common bad syntax examples:
print('Hey there") ---> proper syntax: print('Hey there')
print('Lammy's world') ---> proper syntax: print("Lammy's world")
print("Khabib "the eagle" Nurmagomedov") ---> proper syntax: print('Khabib "the eagle" Nurmagomedov')
"""

# Passing in the text data into a 'variable':
# By convention our variables should always be lowercase, and seperated with an underscore('_').
# Variable names should be as descriptive as possible in parallel with the value they hold.
my_message = "Hello friend!"
# after creating a variable, users are able to pass that variable inside the 'print' function, without the quotation marks.
print(my_message)


# Creating a multi-line string:
# Adding three quotation marks to the beginning and the end of the string will allow users to type in a multi-line text.
multi_line_message = """Wealth,
Fame,
Power...
The man who had acquired everything in this world, the 'Pirate King', Gol D Roger.
"""
print(multi_line_message)


# We can think of our text as a string of individual characters, and we can access these individual characters also.
# But first let's see how many charachters do we have in our string, to achive this we can use the 'len' function, which stands for length.
message = "What's up doc?"
print(len(message))


# After obtaining the character count; we can access each with passing in the location of that specific character inside the square brackets('[]') after our string
# This location is called an 'index' and always starts with zero('0').
"""
First character ---> index 0
Last character ---> len(string) - 1
"""
print(message[0])
print(message[13])


# Accessing a range of characters:
# Slicing out the specific parts of the full text.
# Users need to state from which index they would like to start slicing, followed by a colon(':') and finally type in the index that they would like to stop slicing.
# First index the starting point is always inclusive, while the second index the stopping point is always exclusive.
print(message[0:11])
# print(message[:11]) ---> alternative code for the one line above
print(message[10:13])
# print(message[10:]) ---> alternative code for the one line above
