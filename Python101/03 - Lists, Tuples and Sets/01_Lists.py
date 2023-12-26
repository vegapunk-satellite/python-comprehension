# Lists allow users to work with sequential data.
# Lists have a lot more functionality than the other data types like tuples or sets...
# As the name implies; it allows users to work with a list of values.


# Let's create one called 'courses'; a list variable that contains our specific courses.
courses = ["History", "Math", "Physics", "CompSci"]


print(courses)  # returns the actual list.
print(len(courses))  # returns the length of the list.


# When in need of a specific element of the list:
# Users can pass in the location of the desired index within square brackets ' [] ' to obtain the data.
print(courses[0])  # returns the first element.
print(courses[3])  # returns the last element; ' len(list) - 1 '.


# Negative indexes allow users to manipulate data more conveniently towards the end of that list.
print(
    courses[-1]
)  # returns the last element, hence users won't be concerning over the length of the list.


# If users accidentally try to access an index that does not exist; python will prompt out an index error.
# print(courses[5])   # Returns IndexError: list index out of range.


# Instead of grabbing a value; users can access a 'range' of values.
# list[starting point:stopping point]
# First index(starting point) is always ‘inclusive’;
# However, after the colon(:), the second index(stopping point) is always ‘not inclusive’.
print(courses[0:2])
print(courses[:2])  # when left out empty; by default starts from the first index: '0'
print(courses[2:])  # when left out empty; by default goes up until the end of list.
