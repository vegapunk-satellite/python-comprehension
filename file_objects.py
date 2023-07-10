##File Objects
# -------------------------------------------------------------------------------------
##Working without the context manager:
f = open("test.txt", "r")

print(f.name)
print(f.mode)

f.close()
# -------------------------------------------------------------------------------------
##With this method we have to close each file we opened
##Context managers help us with this closing issue automatically
##'with' method does the same thing hence its usefulness
##Test if a file closes after it has been used, or not:
with open("test.txt", "r") as f:
    pass

print(f.closed)  # returns True; so passed our test
print(
    f.read()
)  # Will throw a 'ValueError', we can only work with this file within context manager
# -------------------------------------------------------------------------------------
##Working with a context manager:
##Reading files:
with open("test.txt", "r") as f:
    f_contents = f.read()
    f_contents = f.readlines()  # returns all contents of the file within a list
    f_contents = (
        f.readline()
    )  # returns the first line of the file, and so on if called multiple times
    # but rather than calling this function again and again we can simply iterate through it
    for line in f:
        print(line, end="")
# -------------------------------------------------------------------------------------
##Controlling over exactly what we're reading from the file
##with 'f.read' we can actually specify the amount of data we want to read at a time by passing in the size as an argument:
with open("test.txt", "r") as f:
    f_contents = f.read(100)
    print(f_contents, end="")
    # Above; 'read' will show the first hundred characters
    # Below; 'read' will continue from where it left off previously
    f_contents = f.read(100)
    print(f_contents, end="")
# -------------------------------------------------------------------------------------
##If the argument we pass in exceeds the total characters in the file, read will return an empty string
##We avert this problem with passing our argument into a variable then using it inside a 'while' loop
with open("test.txt", "r") as f:
    character_size = 20
    f_contents = f.read(character_size)
    while len(f_contents) > 0:
        print(f_contents, end="/")
        f_contents = f.read(character_size)
# -------------------------------------------------------------------------------------
with open("test.txt", "r") as f:
    character_size = 10
    f_contents = f.read(character_size)
    print(f_contents, end="")
    f_contents = f.read(character_size)
    print(f_contents, end="")
    f_contents = f.read(character_size)
    print(f_contents)
    print(f.tell())  # Returns our current position in the file
    # If users desire to restart from beginning each time they call 'read'
    f.seek(
        0
    )  # We used 'seek(0)' to start at the beginning of the file, but the position can be set to anywhere we like
    f_contents = f.read(character_size)
    print(f_contents)
# -------------------------------------------------------------------------------------
## Writing files:
with open(
    "test2.txt", "w"
) as f:  # This will go ahead and create a file if it does not exist, and overwrite a file if it does exist
    f.write(
        "Test"
    )  # Even if we used the 'pass' command, the file will be created because of the code on the line above
    f.seek(0)  # Using the 'seek' method with writing tends to complicate things
    f.write(
        "R"
    )  # This will return the string of 'Rest'; writes 'Test' returns to 0 index with 'seek' after only changes 'T' into a 'R'
# -------------------------------------------------------------------------------------
## Read & Write
with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:  # took the file that we read
            wf.write(line)  # created it's copy with write
# -------------------------------------------------------------------------------------
##Copying a jpg file
##Same code as the above will throw an UnicodeDecodeError, so we need to open binary mode by simply adding 'b' right next to both 'r' & 'w'
with open("shanks.jpg", "rb") as rf:
    with open("shanks_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)
# -------------------------------------------------------------------------------------
##The alternative for the code above:
with open("shanks.jpg", "rb") as rf:
    with open("shanks_copy.jpg", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
# -------------------------------------------------------------------------------------
