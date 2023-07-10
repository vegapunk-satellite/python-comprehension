"""A content creator shares the names of his contributors every month on his website manually. But lately he has
hard time keeping on with the list as more people contribute. We want to help automate this process so that he won't
miss out on any of these contributors. Luckily 'patreon' sends him a csv_file that has the aforementioned contributors.
The tricky part is some of these members desired to contribute but opted out from having their names to be shown publicly.
Inside this csv_file there is a line that says 'No reward description: (None for no reward)' opted out members are listed
below this statement. We need to write a script that parses out only the desired parts from the original csv_file"""

"""Using the 'split' method on each line can be another approach, but if there is a typo within the given input
such as ',' we wouldn't want to split on that... This approach may result in getting undesired output. """

## First approach: using regular 'reader' method
import csv

html_output = ''
##first we will create the variable that we desired to be our end goal and populate it as we go
names = []
##we also know that we need to capture every name to put into our output, hence the empty list

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    ##We don't want the headers or first line of bad data so we skip the first two lines
    next(csv_data)
    next(csv_data)

#     for line in csv_data:
#         names.append(f'{line[0]} {line[1]}')

# for name in names:
#     print(name)
## We got all the names in the list, but we have to get rid of the opted out ones
## We simply can add a condition that stops upon coming across the opted out members

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f'{line[0]} {line[1]}')

html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'
"""html tags that we added in:
<p> - paragraph, <ul> - unordered list, <li> - list item
plus we used '\n' for new line, '\t' for tab space to make our code look better"""

print(html_output)
#-------------------------------------------------------------------------------------
## Second approach: using 'DictReader' method (more readable code)
import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    ##We don't want first line of bad data for that reason we need to skip a line
    ##no headers this time since they are 'keys'
    next(csv_data)

    for line in csv_data:
        ##With 'DictReader' method we can now use the keys of first name and last name to construct our logic
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'
"""html tags that we added in:
<p> - paragraph, <ul> - unordered list, <li> - list item
plus we used '\n' for new line, '\t' for tab space to make our code look better"""

print(html_output)
