"""A content creator shares the names of his contributors every month on his website manually. But lately he has
hard time keeping on with the list as more people contribute. We want to help automate this process so that he won't
miss out on any of these contributors. Luckily the payment company sends him a csv_file that has the list of aforementioned contributors.
The tricky part is some of these members desire to contribute but opted out from having their names to be shown publicly.
Inside this csv_file there is a line that says 'No reward description: (None for no reward)' where the opted out members are listed
below this statement. We need to write a script that parses out only the desired parts from the original csv_file."""


"""Guide to the html tags, which later will be used:
<p> - paragraph, <ul> - unordered list, <li> - list item
plus we used '\n' for new line, '\t' for tab space to make our code look better."""


# Using the 'split' method on each line is prone to mistakes, like in cases where;
# there is a typo within the given input such as ',' we wouldn't want to split on that...
# The functionality of 'reader' and 'DictReader' come in handy in these situations.


import os


os.chdir(
    "C:/Users/MSI/Desktop/Records/CS/my_modules/09 - Interacting with Files/sample CSV files"
)  # changing the operations directory to where the CVS files exist.


# First approach, using regular 'reader' method(less convenient):
import csv


# First we will create the variable that we desired to be our end goal, and populate it as we go.
html_output = ""


# We also know that we need to capture every name to put into our output, hence the empty names list.
names = []


with open("patrons.csv", "r") as data_file:
    csv_data = csv.reader(
        data_file
    )  #'.reader()' method parses the csv file, after storing it in the created variable.

    # Prompting the desired data line by line:
    # for line in csv_data:
    # print(line)

    # As seen above, the list contains some unnecessary data such as;
    # the headers or the first line of instructional data so we skip the those two lines by:
    next(csv_data)
    next(csv_data)

    # Since our goal was to grab contributor names:
    for line in csv_data:
        names.append(
            f"{line[0]} {line[1]}"
        )  # Accessing those through; index 0 for names, index 1 for surnames and appending them to our previously created empty list.

    # Finally, prompting out desired names and removing those who opted out.
    # Users got all the names in the list, but there is the issue to get rid of the opted out ones.
    # Let us add a condition that stops upon coming across the opted out members.
    for line in csv_data:
        if (
            line[0] == "No Reward"
        ):  # The list of names will be prompted until the interpreter reads the line with 'No Reward';
            break  # when it reaches the line with that indication, we will break out the loop.
        names.append(f"{line[0]} {line[1]}")


for name in names:
    print(name)


# Hard part is over. Since all the desired names are accessed;
# let us put them into an unordered html list, so that it can be dropped to a website.
# First let us state how many people contributed. (Opted out members are not included.)
html_output += (
    f"<p>There are currently {len(names)} public contributors. Thank you!</p>"
)


html_output += "\n<ul>"  # Adding an unordered list(<ul>) to our html output. (New line was added for better readability.)


# Adding all names to the html output, again for better readability:
for name in names:
    html_output += f"\n\t<li>{name}</li>"


# Closing out the entire list all together:
html_output += "\n</ul>"


print(html_output)


# Second approach: using 'DictReader' method (more readable code):
# Dictionary reader turns each line into a dictionary instead of a list.
# The dictionary has each field as a key, and then the data as the values.
import csv


# Same logic we used in the reader method applies here as well. Creating empty lists for the final goal and populating as we go:
html_output = ""
names = []


with open("patrons.csv", "r") as data_file:
    csv_data = csv.DictReader(data_file)

    # When using 'DictReader' no headers will be prompted since they are the keys, only their value pairs will be shown.
    # We don't want the first line of bad data for that reason we need to skip a line.
    next(csv_data)

    for line in csv_data:
        # With the 'DictReader' method we can now use the keys to access values.
        # Such as in the current example usage of 'FirstName' and 'LastName' to construct our logic.
        if line["FirstName"] == "No Reward":
            break
        names.append(f"{line['FirstName']} {line['LastName']}")


html_output += (
    f"<p>There are currently {len(names)} public contributors. Thank you!</p>"
)


html_output += "\n<ul>"


for name in names:
    html_output += f"\n\t<li>{name}</li>"


html_output += "\n</ul>"


print(html_output)
