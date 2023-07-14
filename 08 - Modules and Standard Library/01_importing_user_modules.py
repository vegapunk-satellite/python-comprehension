# Importing Modules:
# Proper syntax;
""" import module_name """


# Importing the our own modules:
# Let's try to import the 'test_module' script that we previously created.
# These two user scripts have to be inside the same directory.
import test_module


courses = ["History", "Math", "Physics", "CompSci"]
# Using a specific functionality within our module:
# Users have to type in the module name first; and after the desired functionality.
index = test_module.find_index(
    courses, "Math"
)  # Looking into the list of 'courses', to find the value of 'Math'.


print(index)


# Users have the ability to specify a name for their imported modules.
# Generally tends to be used for shortening tedious module names.
# Proper syntax;
""" import module_name as MN """


import test_module as TM


courses = ["History", "Math", "Physics", "CompSci"]
index = TM.find_index(courses, "Math")


print(index)


# Importing the function itself within a module, cuts from memory and is really efficient.
# But only imports that specific function.
# Proper syntax;
""" from module_name import function_name """


from test_module import (
    find_index,
    test_string,
)  # 'as' can be used to shorten functions just like modules.


courses = ["History", "Math", "Physics", "CompSci"]
index = find_index(courses, "Math")


print(index)
print(test_string)


# Importing each and every functionality from a module:
# Using '*' imports every function from that module.
# But this method is frowned upon because python can't tell which function will be imported from that specific module.
# Correct syntax;
""" from module_name import * """


# Whenever the users import a module, the system checks multiple locations of a list called; 'sys.path'.
# Users can access this list by importing the 'sys' module.
# If the desired module is in the same directory with our current file. We can simply import it.
from test_module import find_index, test_string
import sys


courses = ["History", "Math", "Physics", "CompSci"]


index = find_index(courses, "Math")


print(
    sys.path
)  # Returns the list of directories within the system where Python looks for modules.
# Order of sys directories;
"""
-- The directory of the running script
-- Directories listed in the Python path environment variable
-- Standard Library Directories
-- Site Packages Directory for third party packages
"""


# In cases the module that users are trying to import is in a different directory.
# Users can manually add that directory to the 'sys.path' list.
import sys


sys.path.append("Directory/of/the/imported/module")
from test_module import find_index, test_string


courses = ["History", "Math", "Physics", "CompSci"]
index = find_index(courses, "Math")


print(sys.path)


# Manually adding directories is not the best approach.
# Because of appending the directory before importing the remaining modules.
# So making this change via the Python Path Environment variable makes more sense...
# Changing the environment variables may be different in various operating systems,
# but there are plenty of tutorials for each and every one of them on the internet.
