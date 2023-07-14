# Let us try out various list methods that are available for users...
courses = ["History", "Math", "Physics", "CompSci"]


# Adding an item to our list:
# '.append()' method allows you to add an item to the end of the list.
courses.append("Geography")
print(courses)


# Adding an item to a specific location(index).
# .insert(specific index, item)
courses.insert(0, "Art")  # Inserts art at the beginning of the list.
print(courses)


# Adding multiple values to a list:
# Assume that we need to add a list of elements into our previous list.
courses_2 = ["Art", "Geography"]


# courses.insert(0, courses_2)
# Code above does not add elements individually like we intended...
# Instead it appends the list as a whole; hence the use of '.extend()' method.
courses.extend(courses_2)
print(courses)


# Removing Values from a list:
courses.remove("Math")  # Removes 'Math' from the list.
print(courses)


# Popping values out of a list:
# By default will remove the last value of that list.
courses.pop()  # pops 'CompSci' out of the list
print(courses)


# Pop method returns the value that it removed; so users can actually set a variable, and grab that popped value.
popped = courses.pop()  # grabs the popped out 'CompSci' value.
print(popped)
# In cases where a list is used like a stack or a queue; '.pop()' method is extremely useful.
# Users can keep popping values until the list is empty.


# Sorting values within a list:
courses.sort()  # Sorts out the given list in an alphabetical order.
print(courses)
# Reversing the list:
courses.reverse()
print(courses)


# In cases where the given list contains a bunch of numbers;
# sort function by default will return them in an ascending order.
nums = [1, 6, 5, 7, 4, 9, 2, 3, 8]


nums.sort()
print(nums)


# Changing the default sorting parameters:
# Users can simply pass in an argument into the sort method which called 'reverse';
# and set it as a boolean either True or False.
nums.sort(reverse=True)  # Descending order
courses.sort(reverse=True)  # Reverse alphabetical order


print(nums)
print(courses)


# Up until now, with most of these previous methods; users do not need to reset variables upon using these functionalities.
# Our lists were altered at their place...


# Alternative method for obtaining the sorted version of wished list, without altering the original:
# Users need to create a new variable to obtain the sorted version.
sorted_c = sorted(courses)
sorted_n = sorted(nums)


print(sorted_c)
print(sorted_n)


# Honourable Mentions(more built-in functionalities):
print(min(nums))  # smallest value of the given list
print(max(nums))  # largest value of the given list
print(sum(nums))  # total value of the given list


# Searching and finding values within a given list:
print(
    courses.index("CompSci")
)  # Returns the index '3', which holds the value 'CompSci'


# print(courses.index('Gymnastics'))
# If the user tries to find a value that does not exist in the list:
# python will prompt out a value error


# Checking whether a value exists or not, inside the given list:
# Will return a boolean, either True or False.
print("Gymnastics" in courses)  # Returns False, since the condition is false.
print("Math" in courses)  # Returns True, since the condition is true.
# This method will be especially useful within the future topics of 'conditionals' and 'if - else statements'.
