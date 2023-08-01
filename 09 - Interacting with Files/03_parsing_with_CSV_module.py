# In cases where users need to parse some data within a file;
# string split() method can be used, but it's prone to user mistakes...
# The 'csv' module helps users an awful lot when solving those kind of problems.
# CSV stands for comma separated values, that contain a delimiter; meaning the seperator that allows proper parsing.
# And in fact comma is not the only delimiter, some of the commonly used ones are:
# Colon, semi-colon, dash and tab. (':' ';' '-' '\t')
# The headers in the file that parsing is made based on are called 'fields'.
# So the delimiter separates the data into different fields.


# Let's begin using the regular reader and the regular writer(less convenient approach)...
# Reading a CSV file:
# Users can operate without any necessities if the script and csv file are located in the same directory.
# While in the current case csv file is located in a sub-directory; hence the usage of the 'os' module.
import os


os.chdir(
    "C:/Users/MSI/Desktop/Records/CS/my_modules/09 - Interacting with Files/sample CSV files"
)  # changing the operations directory to where the CVS files exist.

import csv


# Passing the csv file into the '.reader' method:
with open("names.csv", "r") as csv_file:
    # By default the '.reader' method expects a separator like ',' because of the 'dialect'.
    csv_reader = csv.reader(csv_file)  # Variable name 'csv_reader' is not obligatory.
    print(csv_reader)  # returns the object in memory, not the list we desired.

    # Hiding the field names: (optional)
    next(
        csv_reader
    )  # by calling 'next' users can step over the first line that holds the headers.

    # Instead we need to loop over all these lines in the reader, for the desired data to be prompt out.
    for line in csv_reader:
        print(line)  # Each line that we are printing out is a list of all the values.

        # In cases users go by index; '0' is first_name, '1' is last_name and '2' is email.
        print(line[2])  # returns only emails.


# To alter a CSV file; users simply may open the original csv file to be read, and use the 'reader' method to assign it into a variable.
# Within that context manager open a new file for writing; and then use the 'writer' method to assign it into a variable with '\t' as the new delimiter.
# Meaning iterating through each line in the original csv file; and writing it out to the new file with '\t' as the delimiter.
import csv


with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("new_names.csv", "w") as new_file:
        csv_writer = csv.writer(
            new_file, delimiter="\t"
        )  # In cases where users forgot to pass in the delimiter, parsing will be wrong.

        for line in csv_reader:
            csv_writer.writerow(line)


# Using the dictionary reader and the dictionary writer(more convenient approach)...
# Dictionary Reader:
# While using the 'DictReader' method; the fields in the first line will be the keys and the rest of the information on the later lines will be their value pairs.
import csv


with open("names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # print(line)
        print(line["email"])


# Dictionary Writer:
# Users are obliged to provide the field names of their specific file.
import csv


with open("names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("new_names.csv", "w") as new_file:
        fieldnames = [
            "first_name",
            "last_name",
            "email",
        ]  # After being stated, these fieldnames will be passed in as an argument.

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")
        # with 'DictWriter' users have the option of whether or not to print out headers, which are field names in the first line.
        csv_writer.writeheader()  # Adding the headers.

        for line in csv_reader:
            csv_writer.writerow(line)


# 'DictWriter' method tends to be easier to use in the situations; where users want to only write out the specific parts of the information.
# Let's create a file that contains only the first and last names.
# First we need to remove the 'email' from our 'fieldnames' variable.
# After that when we are iterating through, before printing out the desired keys we need to remove the 'email' key using:
#'del line['email']'
import csv


with open("names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("only_names.csv", "w") as new_file:
        fieldnames = ["first_name", "last_name"]

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")
        csv_writer.writeheader()

        for line in csv_reader:
            del line["email"]  # Deletes the 'email' key.
            csv_writer.writerow(line)
