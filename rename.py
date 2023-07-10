## Assume that you have bought and downloaded your favourite album, which has 100's of songs; but all of the songs got their name prior to their number of album orders.
## Considering there are a lot of songs, renaming them one by one would be really tedious.
## Let's think what we learned over this period to solve this common problem using Python:

## First let's make sure that we are on that specific directory
import os

os.chdir("C:/Users/MSI/Desktop/Records/One Piece/OST")
# print(os.getcwd())                                                  #To check the directory where we are operating
for f in os.listdir():
    # print(f)                                                        #Prints out the original list
    # print(os.path.splitext(f))                                      #Splits the file name and the executable,
    f_name, f_ext = os.path.splitext(f)  # and stores them in two separate variables
    # print(f_name)
    f_title, f_num = f_name.split(
        "-"
    )  ##Now we can even further split this new variable to serve our ways
    # print(f_title)
    # print(f_num)
    ##Lastly we want to strip off the unnecessary empty spaces
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(
        2
    )  #'zfill' method allows us to create 0 padded strings and help avoid possible conflicts while and we strip the '#' from the beginning
    f_ext = f_ext.strip()
    ## User desires a format such as 'number-title.extension'
    # print('{}-{}{}'.format(f_num, f_title, f_ext))
    ##finally got the format we desired, now let's pass it into a variable and rename the file
    new_name = "{}-{}{}".format(f_num, f_title, f_ext)
    os.rename(f, new_name)
