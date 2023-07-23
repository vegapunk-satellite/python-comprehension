# Assume that you have bought and downloaded your favourite album, which has 100's of songs;
# but all of the songs got their name prior to their order in the album.
# Considering there are a lot of songs, renaming them one by one would be really tedious.
# Let's think what we learned over this period to solve this common problem using Python:


# First let's make sure that we are on that specific directory.
import os


os.chdir(
    "C:/Users/MSI/Desktop/Records/OST"
)  # Change the directory to the folder that holds the album.
print(os.getcwd())  # To check the directory where we are operating.


# Let us first observe, looping through the files in album's directory:
for f in os.listdir():
    # Let's build the solution one step at a time.
    print(f)  # Prints out the original list, all of the desired file names.

    # Splits the file name and the executable, returns a tuple.
    print(os.path.splitext(f))

    # Setting that tuple into two separate variables.
    f_name, f_ext = os.path.splitext(f)
    print(f_name)

    # Now we can even further split this new variable to serve our purposes.
    f_num, f_title = f_name.split("-")
    print(f_title)
    print(f_num)

    # Lastly we want to strip off the unnecessary empty spaces, using '.strip()' method:
    f_title = f_title.strip()
    f_ext = f_ext.strip()

    # '.zfill' method allows us to create 0 padded strings and help avoid possible conflicts while and we strip the '#' from the beginning.
    f_num = f_num.strip()[:].zfill(2)

    # The desired format;
    # 'number'-'title'.'extension'
    print("{}-{}{}".format(f_num, f_title, f_ext))

    # Finally got the format we desired, now let's pass it into a new variable and rename our files:
    new_name = "{}-{}{}".format(f_num, f_title, f_ext)
    os.rename(f, new_name)
