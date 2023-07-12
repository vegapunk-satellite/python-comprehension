student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['name'])
print(student['age'])
print(student['courses'])
print(student.get('name'))
print(student.get('phone', 'Not Found'))
student['phone'] = '555-5555'
student['name'] = 'Franky'
print(student.get('phone', 'Not Found'))                ##***Takes the second argument as a value only if there is none given by default***
print(student)

##Update method allows user to have more configuration over the specific dictionary
student.update({'name': 'Franky', 'age': 35, 'courses': ['Physics', 'CompSci', 'Math', 'Chemistry'], 'phone': '568-8888'})
del student['age'] removes the key directly
print(len(student))
print(student.keys())
print(student.values())
print(student.items())            ##**Returns key and value pairs**
#-------------------------------------------------------------------------------------
##Looping through key and values
for key in student:
    print(key)        #We don't want just keys

for key, value in student.items():
    print(key, value)
#-------------------------------------------------------------------------------------
##If / else statements
##Comparisons:
##Equal:            ==
##Not Equal:        !=
##Greater Than:     >
##Less Than:        <
##Greater or Equal: >=
##Less or Equal:    <=
##Object Identity:  is

language = 'Java'

if language == 'Python':
    print('Conditional was True')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')
#-------------------------------------------------------------------------------------
## 'and', 'or', 'not':
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')
#-------------------------------------------------------------------------------------
##***Difference between '==' and 'is'*** is checks for id
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(id(a))
print(id(b))
print(a is b)

a = b
print(a is b)
#-------------------------------------------------------------------------------------
##Values that evaluate to False: ***Everything else by default evaluate to True***
##False
##None
##Zero of any numeric type
##Any empty sequence. For example, '', (), [].
##Any empty mapping. For example, {}.

condition = ''

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
#-------------------------------------------------------------------------------------
##loops
##***'break' quits the loop, while 'continue' moves on with the next iteration***
nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)

x = 0

while x < 10:
    print(x)
    x +=1
#-------------------------------------------------------------------------------------
##Functions
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
