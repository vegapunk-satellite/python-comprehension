# File Objects:
# Working without the context manager(not recommended):
# Using built-in 'open' command to open and read the 'test.txt' file;
# which is located in a sub-directory, hence the usage of the 'os.chdir()' method.
import os


os.chdir(
    "C:/Users/MSI/Desktop/Records/CS/my_modules/09 - Interacting with Files/sample texts"
)

f = open("test.txt", "r")  # reading.
# f = open("test.txt", "w") # writing.
# f = open("test.txt", "a") # appending.
# f = open("test.txt", "r+")    # reading and writing.


print(f.name)  # Returns the file name.
print(f.mode)  # Returns the mode that the file is currently opened with.


f.close()  # Using the 'open' method we have to close each file that we opened.


# Context managers help us with this closing issue automatically
# 'with' method does the same thing hence its usefulness...
# Testing if a file closes automatically when being opened with a context manager:
with open("test.txt", "r") as f:
    pass


print(f.closed)  # returns True; so passed our test.
# print(
#     f.read()
# )  # Will throw a 'ValueError', users can only work with this file within the context manager.


# Working with a context manager(recommended):
# Reading files:
with open("test.txt", "r") as f:
    f_contents = f.read()  # Returns the file read only.
    print(f_contents)

    f_contents = f.readlines()  # Returns all contents of the file within a list.
    print(f_contents)

    f_contents = (
        f.readline()
    )  # Returns the first line of the file, and so on if called multiple times.
    print(f_contents)

    # But rather than calling this function again and again users can simply iterate through it.
    for line in f:
        print(line, end="")  # Passing in an empty string each time the function prints.


# Controlling exactly what we're reading from the file:
# with 'f.read' we can actually specify the amount of data we want to read at a time by passing in the size as an argument:
with open("test.txt", "r") as f:
    f_contents = f.read(100)  # 'read' will show the first hundred characters.
    print(f_contents, end="")
    f_contents = f.read(100)  # 'read' will continue from where it left off previously.
    print(f_contents, end="")


# If the argument users pass in exceeds the total characters in the file, 'read' will return an empty string;
# users may avert this problem with passing their argument into a variable and then using it inside a 'while' loop:
with open("test.txt", "r") as f:
    character_size = 20  # Size to read.
    f_contents = f.read(
        character_size
    )  # read as many as 'character size' on each iteration.
    while len(f_contents) > 0:  # Checks if users have hit the end of the file.
        print(
            f_contents, end="/"
        )  # '/' separates the each loop that has been iterated through.
        f_contents = f.read(character_size)


with open("test.txt", "r") as f:
    character_size = 10
    f_contents = f.read(character_size)
    print(f_contents, end="")
    f_contents = f.read(character_size)
    print(f_contents, end="")
    f_contents = f.read(character_size)
    print(f_contents)
    print(f.tell())  # Returns our current position in the file.

    # If users desire to restart from the beginning each time they call 'read'.
    f.seek(
        0
    )  # 'seek(0)' by default starts at the beginning of the file, but the starting position can be altered via changing the variable.
    f_contents = f.read(character_size)
    print(f_contents)


# Writing to files:
with open(
    "test2.txt", "w"
) as f:  # This will go ahead and create a file if it does not exist, and overwrite a file if it does exist.
    f.write("Test")
    f.seek(
        0
    )  # Using the 'seek' method with writing tends to complicate things. Second test will overwrite the first one.
    f.write(
        "R"
    )  # This will return the string of 'Rest'; writes 'Test' returns a 0 index with 'seek' after only changes 'T' into a 'R'.


# Using Read & Write on multiple files at the same time:
with open("test.txt", "r") as rf:
    with open(
        "test_copy.txt", "w"
    ) as wf:  # Will go ahead and create 'test_copy.txt' in cases if it does not exist.
        for line in rf:  # took the file that we read.
            wf.write(line)  # created its copy with write.


# Copying a jpg file:
# Previous logic will throw an UnicodeDecodeError, so users need to open binary mode by simply adding 'b' right next to both 'r' & 'w'.
import os


os.chdir(
    "C:/Users/MSI/Desktop/Records/CS/my_modules/09 - Interacting with Files/sample images"
)  # changing the operations directory where the sample jpg files exist.

with open(
    "shanks.jpg", "rb"
) as rf:  # 'rb' = Binary Mode(Reading bytes instead of text).
    with open("shanks_copy.jpg", "wb") as wf:  # 'wb', writing bytes instead of text.
        for line in rf:
            wf.write(line)


# The alternative for the code above:
with open("shanks.jpg", "rb") as rf:
    with open("shanks_copy.jpg", "wb") as wf:
        chunk_size = (
            4096  # Reading a specified amount of data from the picture each time.
        )
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
