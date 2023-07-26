# Assume that you have bought and downloaded your favourite album, which has 100's of songs;
# but all of the songs got their name prior to their order in the album, preventing users from auto-playing in the correct order.
# Considering there are a lot of songs, renaming them one by one would be really tedious.
# Let's think about what we learned until this period and solve this common problem with a Python script.


# First let's make sure that we are in that specific directory.
import os


# Change the directory to the folder that holds the album.
os.chdir("C:/Users/MSI/Desktop/Records/OST")
print(os.getcwd())  # To check the directory where we are operating, just to be sure...


# Let us first observe, looping through and printing the files in album's directory;
# using 'os.listdir()' which returns all of the file names in the current working directory.
# And then build the solution one step at a time...
for f in os.listdir():
    print(f)  # Prints out all of the file names that users wish to re-sort.

    # First stage:
    # Separating the file extension;
    # 'os.path.splitext()' method returns the file name and the executable in the form of a tuple.
    print(os.path.splitext(f))

    # Accessing the separated name and file extension values by;
    # setting that tuple into two separate variables.
    f_name, f_ext = os.path.splitext(f)
    print(f_name)

    # Second stage:
    # Altering the file names in a properly sortable fashion:
    # Grabbing the serialisation numbers in each name; inserting them prior to their titles.
    # since the texts in the example file are separated with '-':
    f_title, f_num = f_name.split("-")
    print(f_title)
    print(f_num)

    # Third stage:
    # Formatting the text as desired, in a proper sortable way;
    # 'number'-'title'.'extension'
    print("{}-{}{}".format(f_num, f_title, f_ext))

    # Minor fixes:
    # Lastly we want to strip off the unnecessary empty spaces, using '.strip()' method:
    f_title = f_title.strip()
    f_ext = f_ext.strip()

    # Averting the sorting conflict in between single digit numbers and '10':
    # '.zfill' method allows us to create '0' padded strings and help avoid possible conflicts.
    # Zero padding all the single digit numbers; while at the same time stripping the unnecessary spaces;
    f_num = f_num.strip()[:].zfill(2)

    # Final stage:
    # Since the wished format is accessed; let's pass it into a new variable and rename our files:
    new_name = "{}-{}{}".format(f_num, f_title, f_ext)
    os.rename(f, new_name)
