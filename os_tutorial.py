import os


print(
    dir(os)
)  # Prints out all of the attributes and methods we can access to within this module
print(os.getcwd())  # Prints out the directory of current script


os.chdir(
    "C:/Users/MSI/Desktop/Vega Records/my_modules"
)  # Changes the current directory to the desired address via the argument


print(os.getcwd())
print(os.listdir())  # Prints out the files in current directory
# -------------------------------------------------------------------------------------
# creating folder/s
os.mkdir("hsdh-OP")  # creates a single folder on the current directory
os.makedirs("hsdh-OP/hito")  # creates multiple folders on the current directory


print(os.listdir())
# -------------------------------------------------------------------------------------
# deleting folder/s
os.rmdir("hsdh-OP")  # deletes a single folder on the current directory
os.removedirs("hsdh-OP/hito")  # deletes multiple folders on the current directory


print(os.listdir())
# -------------------------------------------------------------------------------------
# renaming file/s
os.rename("importing_modules", "importing_modules.py")
print(os.listdir())
# -------------------------------------------------------------------------------------
# Obtaining a file's information
print(os.stat("importing_modules.py"))
print(os.stat("importing_modules.py").st_size)  # Returns the size of that file
print(
    os.stat("importing_modules.py").st_mtime
)  # Returns the last modification time of that file


# We can convert the returned timestamp into a more user friendly and readable format
import os
from datetime import datetime


print(os.getcwd())
mod_time = os.stat(
    "importing_modules.py"
).st_mtime  # We need to put the timestamp into a variable
print(
    datetime.fromtimestamp(mod_time)
)  # And use that variable as an argument for 'datetime.fromtimestamp' function
# -------------------------------------------------------------------------------------
# Traversing the directory tree
import os


for dirpath, dirnames, filenames in os.walk(
    os.getcwd()
):  # If the desired directory is not the current one we can pass a specific directory as a string to our argument
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)


# ***** 'os.walk' method can be extremely useful if forgot a file's location or in a web application; keeping track of the file information within a certain directory structure*****
# -------------------------------------------------------------------------------------
# Users can access their home directory location via;
import os


print(os.getcwd())
print(os.environ.get("HOMEPATH"))


file_path = os.path.join(os.environ.get("HOMEPATH"), "test.txt")
print(file_path)


print(os.path.basename("/tmp/test.txt"))  # base name
print(os.path.dirname("/tmp/test.txt"))  # directory name
print(os.path.split("/tmp/test.txt"))  # both
print(os.path.exists("/Users/MSI"))  # Returns true if a path exists, false if not
print(
    os.path.isdir("/Users/MSI")
)  # Returns true if specific path is a directory, false if not
print(
    os.path.isfile("/Users/MSI")
)  # Returns true if specific path is a file, false if not
print(os.path.splitext("/tmp/test.txt"))  # Splits root of the path and the extension.


print(dir(os.path))  # We can see all the useful functions this method has
