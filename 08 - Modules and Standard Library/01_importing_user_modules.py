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


# Importing the function itself within a module, cuts from memory and really efficient.
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


# If the desired module is in the same directory with our current file. We can simply import it.
from test_module import find_index, test_string
import sys

courses = ["History", "Math", "Physics", "CompSci"]

index = find_index(courses, "Math")
# print(index)
# print(test_string)

print(sys.path)  # Allows users to see the directories


# If not in same directory, we can append the location of the desired module to our python path
import sys

sys.path.append("-------Directory_Address-------")
