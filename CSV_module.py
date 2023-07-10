##CSV stands for comma separated values
##It allows users to separate the data into different fields using a delimiter(generally ',')
##The top line has our fields
##Let's begin using regular reader and regular writer
##Reading a CSV file:
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)           #by default 'reader' method expects a separator like ',' because it's using 'dialect'
    #print(csv_reader)                           #returns the object in memory, not the list we desired
    #Instead we need to loop over all these lines in the reader

    ##By calling 'next' we can step over our fields to only show the necessary information
    next(csv_reader)

    for line in csv_reader:
        print(line)                             #each line that we printing out is a list of all the values
        ##if we go by index; 0 is first_name, 1 is last_name and 2 is email
        print(line[2])                           #returns only emails
#-------------------------------------------------------------------------------------
## Writing to a CSV file:
## We are opening the original csv file to be read, and using 'reader' method to assign it into a variable
## after we are opening a new file for writing; called 'new_names.csv', and then we use 'writer' method assign it into a variable with the delimiter '-'
## finally we iterate through the each line in the original csv data; and writing it out to the new file with '-'
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
#-------------------------------------------------------------------------------------
##Let's try to read the new csv file that we created,
import csv

with open('new_names.csv', 'r') as csv_file:
    #csv_reader = csv.reader(csv_file)                   #if we do not pass in our delimiter we won't have the correct parsing
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)
#-------------------------------------------------------------------------------------
##Dictionary reader and dictionary writer
##Dictionary Reader
##while using 'DictReader' method; our fields in the first line will be the key/s and the rest of the information on the later lines will be their value/s pairs
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        #print(line)
        print(line['email'])
#-------------------------------------------------------------------------------------
##Dictionary Writer
##Users have to provide the field names of their file
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        ##with 'DictWriter' users have option of whether or not write out 'headers', which are field names in the first row
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
#-------------------------------------------------------------------------------------
##'DictWriter' method tends to be easier to use in the situations; where users want to only write out the specific parts of the information
##Let's create a file that contains only first and last names
##This will really resemble the code above; first we need to remove the 'email' from our 'fieldnames' variable
##after that; when we are iterating through, before printing out we need to remove 'email' via 'del line['email']'
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('only_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        ##with 'DictWriter' users have option of whether or not write out 'headers', which are field names in the first row
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
