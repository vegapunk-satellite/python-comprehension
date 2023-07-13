#Functions
##Keep your code 'DRY' --do not repeat yourself
def hello_func():
    print('Hello Function!')

hello_func()

*****We can treat the 'return' value just like the data type which it is, understanding this will allow users to chain together some functionality.*****
def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func('Greeting'))
#-------------------------------------------------------------------------------------
def student_info(*args, **kwargs):
    print(args)               # A tuple with positional arguments
    print(kwargs)             # A dictionary with all of our keyword values

student_info('Math', 'Art', name='John', age=22)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)        # if we do not use '*' or '**' with our arguments, function won't unpack the values and pass them in individually
student_info(*courses, **info)      #***** 'args' represent positional arguments whereas 'kwargs' represent keyword arguments. When a '*' or '**' used in this context it will unpack a sequence or a dictionary and pass those values to the function individually.*****
#-------------------------------------------------------------------------------------
##Let's manually create two functions; one calculating if a year is a leap year or not, and the other calculates how many days are there in a specific month
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
##Number of days per month. First value placeholder for indexing purposes.

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month and in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(1524))
print(days_in_month(1122, 2))
print(days_in_month(1524, 2))
#-------------------------------------------------------------------------------------
##Importing Modules
## Let's consider the code underneath to be our module which we wish to import.
## 'CompSci' module
print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
    """Find the index of a value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
