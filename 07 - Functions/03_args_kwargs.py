# '*args' and '**kwargs' allow users to accept an arbitrary number of positional or keyword arguments.
# Assume user function takes positional arguments that represent the 'classes which the student is taking'.
# Plus the keyword arguments that passed in will be 'random information about the students'.
# For both of these examples; users don't know how many positional or keyword arguments there will be.
# Hence the usage of *args **kwargs; they are by convention named as such.
# Sticking with conventions enhances the readability of our code.
def student_info(*args, **kwargs):
    print(args)  # A tuple with positional arguments.
    print(kwargs)  # A dictionary with all of our keyword values.


# Calling user function with random values:
# Positional arguments should be passed out prior to keyword arguments.
student_info("Math", "Art", name="John", age=22)


# Function call with arguments using the * or **:
# When a '*' or '**' used in this context it will unpack a sequence, or a dictionary and pass those values to the function individually.
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

student_info(courses, info)  # function won't unpack the values individually as desired.
student_info(*courses, **info)  # Proper unpacking.


# Let's manually create two functions; one calculating if a year is a leap year or not;
# and the other calculates how many days are there in a specific month.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Number of days per month. First value is a placeholder with no useage, inserted only for indexing purposes.


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month and in that year."""

    # year 1524(leap year)
    # month 5(May)
    if not 1 <= month <= 12:
        return "Invalid Month"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(1522))
print(days_in_month(1122, 5))
print(days_in_month(1524, 5))
