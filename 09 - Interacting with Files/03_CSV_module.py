# CSV stands for 'comma separated values'.
# It allows users to separate the data into different fields using a delimiter. (generally ',' or '-')
# The top line has the headliners, known as fields.
# Let's begin using the regular reader and the regular writer(less convenient approach)...
# Reading a CSV file:
import os
import csv


os.chdir(
    "C:/Users/MSI/Desktop/Records/CS/my_modules/09 - Interacting with Files/sample CSV files"
)  # changing the operations directory to where the CVS files exist.


# By default the 'reader' method expects a separator like ',' because of the 'dialect'.
with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)  # returns the object in memory, not the list we desired.

    # Instead we need to loop over all these lines in the reader;
    # by calling 'next' we can step over our fields to only show the necessary information.
    next(csv_reader)

    for line in csv_reader:
        print(line)  # Each line that we are printing out is a list of all the values.

        # In cases users go by index; '0' is first_name, '1' is last_name and '2' is email.
        print(line[2])  # returns only emails.


# To write a CSV file; users simply may open the original csv file to be read, and use the 'reader' method to assign it into a variable.
# Open a new file for writing; called 'new_names.csv', and then use the 'writer' method to assign it into a variable with '-' as the delimiter.
# Finally iterating through each line in the original csv data; and writing it out to the new file with '-' as the delimiter.
import csv


with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("new_names.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)


# Let's try to read the new csv file that we just created:
import csv


with open("new_names.csv", "r") as csv_file:
    # In cases where users forgot to pass in the delimiter, parsing will be wrong.
    csv_reader = csv.reader(csv_file, delimiter="\t")

    for line in csv_reader:
        print(line)


# Using the dictionary reader and the dictionary writer(more convenient approach)...
# Dictionary Reader:
# While using the 'DictReader' method; the fields in the first line will be the key/s and the rest of the information on the later lines will be their value/s.
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
        fieldnames = ["first_name", "last_name", "email"]

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")
        # with 'DictWriter' users have the option of whether or not to write out 'headers', which are field names in the first row.
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)


# 'DictWriter' method tends to be easier to use in the situations; where users want to only write out the specific parts of the information.
# Let's create a file that contains only the first and last names.
# This will resemble the code above; first we need to remove the 'email' from our 'fieldnames' variable.
# after that; when we are iterating through, before printing out we need to remove the email using:
#'del line['email']'
import csv


with open("names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("only_names.csv", "w") as new_file:
        fieldnames = ["first_name", "last_name"]

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")
        csv_writer.writeheader()

        for line in csv_reader:
            del line["email"]
            csv_writer.writerow(line)
