##Sorting Integers
##'sorted()' function returns a new sorted list whereas '.sort()' method sorts the original list and returns 'None'
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(
    li
)  # we can pass in 'reverse=True' as a second argument to change its order

print("Sorted Variable:\t", s_li)

##sorting without creating a variable and in a descending order
li.sort(reverse=True)
print("Original Variable:\t", li)
# -------------------------------------------------------------------------------------
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print("Tuple\t", s_tup)

di = {"name": "Arca", "job": "programming", "age": None, "os": "Windows"}
s_di = sorted(di)
print("Dictionary\t", s_di)
# -------------------------------------------------------------------------------------
##Sorting Integers based on their absolute value:
abs_list = [-6, -5, -4, 1, 2, 3]
s_abs_list = sorted(abs_list, key=abs)
print(s_abs_list)


# -------------------------------------------------------------------------------------
##Sort out given employees based on their name, age and salary
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "({},{},${})".format(self.name, self.age, self.salary)


e3 = Employee("Galdino", 37, 24000000)
e2 = Employee("Bentham", 32, 32000000)
e1 = Employee("Daz Bonez", 31, 75000000)

employees = [e1, e2, e3]


# s_employees = sorted(employees)
##Above this line we are trying to do a sorting but based on what? This return a type error
##we need to state a 'key', telling our function to base the sorting on that specific key
##Writing a custom function for 'key':
def e_sort(emp):
    # return emp.name
    return emp.age
    # return emp.salary


s_employees = sorted(employees, key=e_sort, reverse=True)
print(s_employees)

##Writing a lambda function for 'key':
s_employees = sorted(employees, key=lambda e: e.name)
print(s_employees)

##Working with attributes like this we can use the Standard Library:
from operator import attrgetter

s_employees = sorted(employees, key=attrgetter("age"), reverse=True)
print(s_employees)
