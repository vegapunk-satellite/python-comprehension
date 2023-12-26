# Sorting Integers

# Sorting Lists:
# The 'sorted()' function returns a new sorted list.
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)  # Ascending order.
print("Sorted Variable:\t", s_li)

# whereas the '.sort()' method sorts the original list and returns 'None'.
# Sorting without creating a variable and in a descending order:
li.sort(
    reverse=True
)  # Users can pass in 'reverse' as a second argument to change sorting order.
print("Original Variable:\t", li)


# The 'sorted()' function provides more flexibility because it lets users to pass in any iterable;
# as opposed to the '.sort()' method which works specifically on lists.
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)

# tup.sort()  # Returns an 'AttributeError'. Because tuples don't have a sort method.
# Proper Tuple sorting:
s_tup = sorted(tup)
print("Tuple\t", s_tup)


# Sorting Dictionaries:
di = {"name": "Arca", "job": "programming", "age": None, "os": "Windows"}
s_di = sorted(di)
print("Dictionary\t", s_di)


# Sorting integers based on their absolute value:
abs_list = [-6, -5, -4, 1, 2, 3]
s_abs_list = sorted(
    abs_list, key=abs
)  # The 'key' parameter runs each element through the 'abs'(absolute value) function before it makes the comparisons.
print(s_abs_list)


# 'key' parameter is extremely useful when sorting objects with named attributes.
# Sort out given employees based on their name, age and salary:
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # Do not be confused, code underneath is only for function representation.
    def __repr__(self):
        return "({},{},${})".format(self.name, self.age, self.salary)


# Sample employees:
e3 = Employee("Galdino", 37, 24000000)
e2 = Employee("Bentham", 32, 32000000)
e1 = Employee("Daz Bonez", 31, 75000000)

# Sample employees list:
employees = [e1, e2, e3]

# s_employees = sorted(employees) # Returns a 'TypeError' in cases where the 'key' parameter is not stated.
# Users need to state a 'key', that bases the sorting of the function on that specific key.


# Writing a custom function for the 'key' parameter:
def e_sort(emp):
    # return emp.name
    return emp.age
    # return emp.salary


s_employees = sorted(
    employees, key=e_sort
)  # Passing in a custom sorting function to the 'key' parameter.
print(s_employees)

# Writing a lambda function for the 'key' parameter:
s_employees = sorted(
    employees, key=lambda e: e.name, reverse=True
)  # Writing a lambda function that bases the sorting on names, in a reverse alphabetical order.
print(s_employees)


# Standard Library can be really helpful when working with the attributes.
from operator import attrgetter


s_employees = sorted(
    employees, key=attrgetter("age")
)  # The 'attrgetter' function becomes a replacement for the previous custom key.
print(s_employees)
