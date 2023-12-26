# Exceptions and Error Handling in Python:

# When users anticipate sections of their code that might throw an error or an exception;
# those anticipated errors could be handled with 'try' and 'except' blocks.
# Users have to be as specific as possible when catching exceptions;
# because the goal of try/except blocks is not to just get around all of the possible errors.
# Try/except blocks meant to catch the errors that users expect and handle them properly...

# Running some code that throws an error; will help users understand the need to use these try/except blocks.
# Navigating to the folder where the sample text files exist:
import os


os.chdir("C:/Users/MSI/Desktop/Records/CS/my_modules/12 - Error Handling/sample files")


# Assume that user misremembered the file name and tried to open 'test_file.txt' instead of 'test.txt':
# f = open("test_file.txt") # Returns a 'FileNotFoundError'.


# Instead of prompting out the whole 'FileNotFoundError'; users can simplify the display of errors.
try:
    f = open("test_file.txt")  # Wrong file name entered. Will throw an exception.
except Exception:
    print(
        "File does not exist!"
    )  # Catches the exception and prompts the custom error instead of 'FileNotFoundError'.


# Exceptions are not limited with 'FileNotFoundError', they could catch various errors.
# Even though the user wrote the correct file name; the code below will catch an exception again, caused by the bad variable naming.
try:
    f = open("test.txt")  # Correct file name. Ran successfully.
    var = bad_var  # Bad variable name. Will throw an exception.
except Exception:
    print(
        "Bad variable name."
    )  # Catches the exception and prompts the custom error instead of 'NameError'.


# Catching specific errors:
try:
    f = open("test.txt")
except FileNotFoundError:  # Be as specific as possible when catching exceptions.
    print("File does not exist.")


# Handling multiple exceptions:
# Exception priority is always with the higher block. So more specific ones should be listed above.
try:
    f = open("test.txt")
    var = bad_var
except FileNotFoundError:  # Expected error with higher priority.
    print("This file does not exist.")
except Exception:  # General exception with lower priority.
    print("Something went wrong.")


# In cases users wish to just print out a short version of the built-in exception, instead of custom errors;
# 'as' command is pretty useful.
try:
    f = open("test_file.txt")
    # var = bad_var
except FileNotFoundError as x:  # Catches 'FileNotFoundError'.
    print(x)  # Prompts out the error's own message shortly.
except Exception as y:  # 'x' and 'y' are just names that are user preferential.
    print(y)


# Else Clause:
# 'else' clause runs the code that needs to be executed in cases where; 'try' clause doesn't raise an exception.
try:
    f = open("test.txt")  # Correct file name, no exceptions.
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:  # Since no exceptions have been caught, the code within the else clause will be executed.
    print(f.read())  # Prompts out the contents of the file.
    f.close()  # Closes the file.


# Finally clause:
# Even if code will throw an exception; finally clause will still be executed no matter what.
# So if an action must be executed regardless of the code's success; users can insert it in the finally clause.
# For example when working with a database, users should place the command that closes the database inside the 'finally' clause.
try:
    f = open("test_file.txt")  # Wrong file name. Throws an exception.
except FileNotFoundError as e:  # Exception caught.
    print(e)  # Simple built-in error message prompted.
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing...'test_file'...")  # Executed even though there was an error.


# Manually raising exceptions:
try:
    f = open("corrupt_file.txt")
    if f.name == "corrupt_file.txt":  # Inserting a condition that;
        raise Exception  #  lets users to manually raise an error.
except FileNotFoundError as e:
    print(e)
except Exception as e:  # The exception raised by the user caught here.
    print("User file might be corrupted.")
else:
    print(f.read())
    f.close()
finally:
    print("Executing...'corrupt_file'...")  # Will be executed no matter what.
