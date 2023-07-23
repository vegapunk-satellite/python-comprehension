# OS Module helps users access the underlying operating system.
import os


print(
    dir(os)
)  # Prints out all of the attributes and methods users can access to within this module.


# Commonly used OS Module Functionalities:
# Accessing the current working directory:
print(os.getcwd())  # Prints out the directory of the current script.


# Navigating into a new location on the filesystem:
os.chdir(
    "C:/Users/MSI/Desktop/Vega Records/my_modules"
)  # Changes the current directory to the desired new location.


# Accessing all the files and folders on current working directory:
print(os.listdir())  # Prints out the files & folders in the current directory.


# Creating folders and directories:
os.mkdir("hsdh-OP")  # creates a single folder in the current directory.
os.makedirs("hsdh-OP/hito")  # creates multiple folders in the current directory.


print(os.listdir())


# Deleting folders and directories:
os.rmdir("hsdh-OP")  # deletes a single folder on the current directory.
os.removedirs("hsdh-OP/hito")  # deletes multiple folders on the current directory.


print(os.listdir())


# Renaming files and folders:
# Proper syntax;
# os.rename("file_to_be_renamed", "new_name")
os.rename("importing_modules", "importing_modules.py")
print(os.listdir())


# Obtaining information about files:
print(
    os.stat("importing_modules.py")
)  # Returns various file information that later can be used.
print(os.stat("importing_modules.py").st_size)  # Returns the size of that file.
print(
    os.stat("importing_modules.py").st_mtime
)  # Returns the last modification time of that file, in the form of a 'timestamp'.


# Converting the returned timestamp; into a more user friendly and readable format.
import os
from datetime import datetime


print(os.getcwd())
mod_time = os.stat(
    "importing_modules.py"
).st_mtime  # Setting the returned 'timestamp' value as a variable.
print(
    datetime.fromtimestamp(mod_time)
)  # And passing in that variable as an argument for '.fromtimestamp()'. Prompts out the readable date.


# Traversing the entire directory tree and files within it:
# '.walk()' method is a generator that yields a tuple of three values as it walks the directory tree.
# For each directory that it sees; yields the directory path, directories within that path and files within that directories.
# By default traverses from top going down.
import os


for dirpath, dirnames, filenames in os.walk(
    os.getcwd()
):  # If the desired directory is not the current one we can pass in a specific directory to our argument.
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
# 'os.walk' method useful in cases like finding lost files or keeping track of the file information of a web application; within a certain directory structure.


# Users can access their home directory location by grabbing home environment variable:
import os


print(os.getcwd())
# print(os.environ) # Prompts out all created environments.
print(os.environ.get("HOMEPATH"))  # Prompts out only the home directory.


# Combining a file with the desired path:
# Could be done using concatenation but leaves room for user mistakes, so instead;
# 'os.path.join()' method tends to be a lot more convenient...
file_path = os.path.join(os.environ.get("HOMEPATH"), "test.txt")
print(file_path)


# Various useful methods available through using 'os.path':
print(
    os.path.basename("/tmp/test.txt")
)  # Returns the file name, and that does not have to be an existent path.
print(os.path.dirname("/tmp/test.txt"))  # Returns the directory name.
print(os.path.split("/tmp/test.txt"))  # Returns both file and directory names.
print(
    os.path.exists("/Users/MSI")
)  # Returns true if a path exists within the filesystem, false if not.
print(
    os.path.isdir("/Users/MSI")
)  # Returns true if a specific path is directory, false if not.
print(
    os.path.isfile("/Users/MSI")
)  # Returns true if a specific path is file, false if not.
print(
    os.path.splitext("/tmp/test.txt")
)  # Splits the root of the path and its extension.


print(
    dir(os.path)
)  # Returns all of the attributes and methods users can access to within this module.
